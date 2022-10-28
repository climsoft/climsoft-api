import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.obsscheduleclass import schema as obsscheduleclass_schema
from tests.datagen import (
    obsscheduleclass as climsoft_obs_schedule_class,
    station as climsoft_station,
)
from fastapi.testclient import TestClient


@pytest.fixture
def get_station(session: Session):
    station = climsoft_models.Station(
        **climsoft_station.get_valid_station_input().dict()
    )
    session.add(station)
    session.commit()
    yield station


@pytest.fixture
def get_obs_schedule_class(get_station: climsoft_models.Station, session: Session):
    obs_schedule_class = climsoft_models.Obsscheduleclas(
        **climsoft_obs_schedule_class.get_valid_obs_schedule_class_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(obs_schedule_class)
    session.commit()
    yield obs_schedule_class


@pytest.fixture
def get_obs_schedule_classes(session: Session):
    for i in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.flush()

        session.add(
            climsoft_models.Obsscheduleclas(
                **climsoft_obs_schedule_class.get_valid_obs_schedule_class_input(
                    station_id=station.stationId
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_obs_schedule_classs(
    client: TestClient, get_obs_schedule_classes
):
    response = client.get(
        "/test/climsoft/v1/obs-schedule-class",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, obsscheduleclass_schema.ObsScheduleClass)


def test_should_return_single_obs_schedule_class(
    client: TestClient,
    get_obs_schedule_class: climsoft_models.Obsscheduleclas,
):
    response = client.get(
        f"/test/climsoft/v1/obs-schedule-class/{get_obs_schedule_class.scheduleClass}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, obsscheduleclass_schema.ObsScheduleClass)


def test_should_create_a_obs_schedule_class(
    client: TestClient, get_station: climsoft_models.Station
):
    obs_schedule_class_data = (
        climsoft_obs_schedule_class.get_valid_obs_schedule_class_input(
            station_id=get_station.stationId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/test/climsoft/v1/obs-schedule-class",
        data=json.dumps(obs_schedule_class_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, obsscheduleclass_schema.ObsScheduleClass)


def test_should_raise_validation_error(
    client: TestClient, get_station: climsoft_models.Station
):
    response = client.post(
        "/test/climsoft/v1/obs-schedule-class",
        data=json.dumps({"refers_to": 4}, default=str),
    )
    assert response.status_code == 422


def test_should_update_obs_schedule_class(
    client: TestClient,
    get_obs_schedule_class: climsoft_models.Obsscheduleclas,
):
    obs_schedule_class_data = obsscheduleclass_schema.ObsScheduleClass.from_orm(
        get_obs_schedule_class
    ).dict(by_alias=True)
    obs_schedule_class_id = obs_schedule_class_data.pop("schedule_class")
    updates = {**obs_schedule_class_data, "description": "updated description"}
    response = client.put(
        f"/test/climsoft/v1/obs-schedule-class/{obs_schedule_class_id}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_obs_schedule_class(client: TestClient, get_obs_schedule_class):
    obs_schedule_class_data = obsscheduleclass_schema.ObsScheduleClass.from_orm(
        get_obs_schedule_class
    ).dict(by_alias=True)
    obs_schedule_class_id = obs_schedule_class_data.pop("schedule_class")

    response = client.delete(
        f"/test/climsoft/v1/obs-schedule-class/{obs_schedule_class_id}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/test/climsoft/v1/obs-schedule-class/{obs_schedule_class_id}",
    )

    assert response.status_code == 404
