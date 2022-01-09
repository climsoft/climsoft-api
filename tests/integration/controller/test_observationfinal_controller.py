import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.observationfinal import schema as observationfinal_schema
from tests.datagen import (
    observationfinal as climsoft_observation_final,
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
def get_observation_final(
    get_station: climsoft_models.Station,
    get_obselement: climsoft_models.Obselement,
    session: Session,
):
    observation_final = climsoft_models.Observationfinal(
        **climsoft_observation_final.get_valid_observation_final_input(
            station_id=get_station.stationId, element_id=get_obselement.elementId
        ).dict()
    )
    session.add(observation_final)
    session.commit()
    yield observation_final


@pytest.fixture
def get_observation_finals(
    session: Session,
):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.commit()

        obs_element = climsoft_models.Obselement(
            **climsoft_obselement.get_valid_obselement_input().dict()
        )
        session.add(obs_element)
        session.commit()

        session.add(
            climsoft_models.Observationfinal(
                **climsoft_observation_final.get_valid_observation_final_input(
                    station_id=station.stationId, element_id=obs_element.elementId
                ).dict()
            )
        )
        session.commit()


def test_should_return_first_five_observation_finals(
    client: TestClient, get_observation_finals, session: Session
):
    assert session.query(climsoft_models.Observationfinal).count() == 10
    response = client.get(
        "/v1/observation-finals/",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, observationfinal_schema.ObservationFinal)


def test_should_return_single_observation_final(
    client: TestClient,
    get_observation_final: climsoft_models.Observationfinal,
):
    response = client.get(
        f"/v1/observation-finals/{get_observation_final.recordedFrom}/{get_observation_final.describedBy}/{get_observation_final.obsDatetime}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, observationfinal_schema.ObservationFinal)


def test_should_create_a_observation_final(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_obselement: climsoft_models.Obselement,
):
    observation_final_data = (
        climsoft_observation_final.get_valid_observation_final_input(
            station_id=get_station.stationId, element_id=get_obselement.elementId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/v1/observation-finals/",
        data=json.dumps(
            observation_final_data, default=lambda x: x.strftime("%Y-%m-%d %H:%M:%S")
        ),
    )
    assert response.status_code == 200
    response_data = response.json()
    print(response_data)
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, observationfinal_schema.ObservationFinal)


def test_should_raise_validation_error(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_obselement: climsoft_models.Obselement,
):
    response = client.post(
        "/v1/observation-finals/",
        data=json.dumps({"qc_status": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_observation_final(
    client: TestClient,
    get_observation_final: climsoft_models.Observationfinal,
):
    observation_final_data = (
        climsoft_observation_final.get_valid_observation_final_input(
            station_id=get_observation_final.recordedFrom,
            element_id=get_observation_final.describedBy,
            obs_datetime=str(get_observation_final.obsDatetime),
            qc_status=get_observation_final.qcStatus,
            acquisition_type=get_observation_final.acquisitionType,
        ).dict(by_alias=True, exclude={"recordedFrom", "describedBy", "obsDatetime"})
    )

    updates = {**observation_final_data, "period": 100}
    response = client.put(
        f"/v1/observation-finals/{get_observation_final.recordedFrom}/{get_observation_final.describedBy}/{get_observation_final.obsDatetime}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["period"] == updates["period"]


def test_should_delete_observation_final(
    client: TestClient,
    get_observation_final: climsoft_models.Observationfinal,
):
    response = client.delete(
        f"/v1/observation-finals/{get_observation_final.recordedFrom}/{get_observation_final.describedBy}/{get_observation_final.obsDatetime}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/observation-finals/{get_observation_final.recordedFrom}/{get_observation_final.describedBy}/{get_observation_final.obsDatetime}",
    )

    assert response.status_code == 404
