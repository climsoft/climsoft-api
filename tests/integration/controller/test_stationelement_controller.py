from datetime import datetime
import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.stationelement import schema as stationelement_schema
from tests.datagen import (
    stationelement as climsoft_station_element,
    obsscheduleclass as climsoft_obsscheduleclass,
    obselement as climsoft_obselement,
    station as climsoft_station,
    instrument as climsoft_instrument,
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
    session.close()


@pytest.fixture
def get_obs_schedule_class(get_station: climsoft_models.Station, session: Session):
    obs_schedule_class = climsoft_models.Obsscheduleclas(
        **climsoft_obsscheduleclass.get_valid_obs_schedule_class_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(obs_schedule_class)
    session.commit()
    yield obs_schedule_class
    session.close()


@pytest.fixture
def get_obselement(session: Session):
    obselement = climsoft_models.Obselement(
        **climsoft_obselement.get_valid_obselement_input().dict()
    )
    session.add(obselement)
    session.commit()
    yield obselement
    session.close()


@pytest.fixture
def get_instrument(get_station: climsoft_models.Station, session: Session):
    instrument = climsoft_models.Instrument(
        **climsoft_instrument.get_valid_instrument_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(instrument)
    session.commit()
    yield instrument
    session.close()


@pytest.fixture
def get_station_element(
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
    get_obselement: climsoft_models.Obselement,
    get_obs_schedule_class: climsoft_models.Obsscheduleclas,
    session: Session,
):
    station_element = climsoft_models.Stationelement(
        **climsoft_station_element.get_valid_station_element_input(
            station_id=get_station.stationId,
            instrument_id=get_instrument.instrumentId,
            element_id=get_obselement.elementId,
            schedule_class=get_obs_schedule_class.scheduleClass,
        ).dict()
    )
    session.add(station_element)
    session.commit()
    yield station_element
    session.close()


@pytest.fixture
def get_station_elements(session: Session):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.flush()

        obs_element = climsoft_models.Obselement(
            **climsoft_obselement.get_valid_obselement_input().dict()
        )
        session.add(obs_element)
        session.flush()

        obs_schedule_class = climsoft_models.Obsscheduleclas(
            **climsoft_obsscheduleclass.get_valid_obs_schedule_class_input(
                station_id=station.stationId
            ).dict()
        )
        session.add(obs_schedule_class)
        session.flush()

        instrument = climsoft_models.Instrument(
            **climsoft_instrument.get_valid_instrument_input(
                station_id=station.stationId
            ).dict()
        )
        session.add(instrument)
        session.flush()

        session.add(
            climsoft_models.Stationelement(
                **climsoft_station_element.get_valid_station_element_input(
                    station_id=station.stationId,
                    instrument_id=instrument.instrumentId,
                    element_id=obs_element.elementId,
                    schedule_class=obs_schedule_class.scheduleClass,
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_station_elements(
    client: TestClient, get_station_elements
):
    response = client.get(
        "/v1/station-elements/",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, stationelement_schema.StationElement)


def test_should_return_single_station_element(
    client: TestClient,
    get_station_element: climsoft_models.Stationelement,
):
    response = client.get(
        f"/v1/station-elements/{get_station_element.recordedFrom}/{get_station_element.describedBy}/{get_station_element.recordedWith}/{get_station_element.beginDate}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, stationelement_schema.StationElement)


def test_should_create_a_station_element(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_instrument,
    get_obselement,
    get_obs_schedule_class,
):
    station_element_data = climsoft_station_element.get_valid_station_element_input(
        station_id=get_station.stationId,
        element_id=get_obselement.elementId,
        schedule_class=get_obs_schedule_class.scheduleClass,
        instrument_id=get_instrument.instrumentId,
    ).dict(by_alias=True)
    response = client.post(
        "/v1/station-elements/",
        data=json.dumps(station_element_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, stationelement_schema.StationElement)


def test_should_raise_validation_error(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_instrument,
    get_obselement,
    get_obs_schedule_class,
):
    response = client.post(
        "/v1/station-elements/",
        data=json.dumps({"end_date": datetime.utcnow()}, default=str),
    )
    assert response.status_code == 422


def test_should_update_station_element(
    client: TestClient,
    get_station_element: climsoft_models.Stationelement,
):
    station_element_data = climsoft_station_element.get_valid_station_element_input(
        station_id=get_station_element.recordedFrom,
        element_id=get_station_element.describedBy,
        schedule_class=get_station_element.scheduledFor,
        instrument_id=get_station_element.recordedWith,
    ).dict(
        by_alias=True,
        exclude={"beginDate", "describedBy", "recordedFrom", "recordedWith"},
    )

    updates = {**station_element_data, "height": 100}

    response = client.put(
        f"/v1/station-elements/{get_station_element.recordedFrom}/{get_station_element.describedBy}/{get_station_element.recordedWith}/{get_station_element.beginDate}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    print("\n\n\n\n")
    print(response_data)
    print("\n\n\n\n")

    assert response.status_code == 200
    assert response_data["result"][0]["height"] == updates["height"]


def test_should_delete_station_element(
    client: TestClient,
    get_station_element: climsoft_models.Stationelement,
):

    response = client.delete(
        f"/v1/station-elements/{get_station_element.recordedFrom}/{get_station_element.describedBy}/{get_station_element.recordedWith}/{get_station_element.beginDate}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/station-elements/{get_station_element.recordedFrom}/{get_station_element.describedBy}/{get_station_element.recordedWith}/{get_station_element.beginDate}",
    )
    assert response.status_code == 404
