import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.observationinitial import schema as observationinitial_schema
from tests.datagen import (
    observationinitial as climsoft_observation_initial,
    obselement as climsoft_obselement,
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
def get_obselement(session: Session):
    obselement = climsoft_models.Obselement(
        **climsoft_obselement.get_valid_obselement_input().dict()
    )
    session.add(obselement)
    session.commit()
    yield obselement


@pytest.fixture
def get_observation_initial(
    get_station: climsoft_models.Station,
    get_obselement: climsoft_models.Obselement,
    session: Session,
):
    observation_initial = climsoft_models.Observationinitial(
        **climsoft_observation_initial.get_valid_observation_initial_input(
            station_id=get_station.stationId, element_id=get_obselement.elementId
        ).dict()
    )
    session.add(observation_initial)
    session.commit()
    yield observation_initial


@pytest.fixture
def get_observation_initials(
    session: Session,
):
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

        session.add(
            climsoft_models.Observationinitial(
                **climsoft_observation_initial.get_valid_observation_initial_input(
                    station_id=station.stationId, element_id=obs_element.elementId
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_observation_initials(
    client: TestClient, get_observation_initials
):
    response = client.get(
        "/v1/observation-initials/",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, observationinitial_schema.ObservationInitial)


def test_should_return_single_observation_initial(
    client: TestClient,
    get_observation_initial: climsoft_models.Observationinitial,
):
    response = client.get(
        f"/v1/observation-initials/{get_observation_initial.recordedFrom}/{get_observation_initial.describedBy}/{get_observation_initial.obsDatetime}/{get_observation_initial.qcStatus}/{get_observation_initial.acquisitionType}",
    )
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, observationinitial_schema.ObservationInitial)


def test_should_create_a_observation_initial(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_obselement: climsoft_models.Obselement,
):
    observation_initial_data = (
        climsoft_observation_initial.get_valid_observation_initial_input(
            station_id=get_station.stationId, element_id=get_obselement.elementId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/v1/observation-initials/",
        data=json.dumps(
            observation_initial_data, default=lambda x: x.strftime("%Y-%m-%d %H:%M:%S")
        ),
    )
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, observationinitial_schema.ObservationInitial)


def test_should_raise_validation_error(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_obselement: climsoft_models.Obselement,
):
    response = client.post(
        "/v1/observation-initials/",
        data=json.dumps({"obs_value": 5}, default=str),
    )
    assert response.status_code == 422


def test_should_update_observation_initial(
    client: TestClient,
    get_observation_initial: climsoft_models.Observationinitial,
):
    observation_initial_data = (
        climsoft_observation_initial.get_valid_observation_initial_input(
            station_id=get_observation_initial.recordedFrom,
            element_id=get_observation_initial.describedBy,
            obs_datetime=str(get_observation_initial.obsDatetime),
            qc_status=get_observation_initial.qcStatus,
            acquisition_type=get_observation_initial.acquisitionType,
        ).dict(
            by_alias=True,
            exclude={
                "acquisitionType",
                "describedBy",
                "obsDatetime",
                "qcStatus",
                "recordedFrom",
            },
        )
    )

    updates = {**observation_initial_data, "period": 100}

    response = client.put(
        f"/v1/observation-initials/{get_observation_initial.recordedFrom}/{get_observation_initial.describedBy}/{get_observation_initial.obsDatetime}/{get_observation_initial.qcStatus}/{get_observation_initial.acquisitionType}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["period"] == updates["period"]


def test_should_delete_observation_initial(
    client: TestClient,
    get_observation_initial: climsoft_models.Observationinitial,
):
    response = client.delete(
        f"/v1/observation-initials/{get_observation_initial.recordedFrom}/{get_observation_initial.describedBy}/{get_observation_initial.obsDatetime}/{get_observation_initial.qcStatus}/{get_observation_initial.acquisitionType}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/observation-initials/{get_observation_initial.recordedFrom}/{get_observation_initial.describedBy}/{get_observation_initial.obsDatetime}/{get_observation_initial.qcStatus}/{get_observation_initial.acquisitionType}",
    )
    assert response.status_code == 404
