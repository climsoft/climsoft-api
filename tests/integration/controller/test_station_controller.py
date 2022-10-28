import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.station import schema as station_schema
from tests.datagen import station as climsoft_station
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
def get_stations(session: Session):
    for _ in range(1, 11):
        session.add(
            climsoft_models.Station(**climsoft_station.get_valid_station_input().dict())
        )
    session.commit()


def test_should_return_first_five_stations(client: TestClient, get_stations):
    response = client.get("/test/climsoft/v1/stations", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, station_schema.Station)


def test_should_return_single_station(
    client: TestClient, get_station: climsoft_models.Station
):
    response = client.get(
        f"/test/climsoft/v1/stations/{get_station.stationId}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, station_schema.Station)


def test_should_create_a_station(client: TestClient):
    station_data = climsoft_station.get_valid_station_input().dict(by_alias=True)
    response = client.post(
        "/test/climsoft/v1/stations",
        data=json.dumps(station_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, station_schema.Station)


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/test/climsoft/v1/stations",
        data=json.dumps({"station_name": "fail"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_station(client: TestClient, get_station):
    station_data = station_schema.Station.from_orm(get_station).dict(by_alias=True)
    station_id = station_data.pop("station_id")
    updates = {**station_data, "station_name": "updated name"}

    response = client.put(
        f"/test/climsoft/v1/stations/{station_id}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["station_name"] == updates["station_name"]


def test_should_delete_station(client: TestClient, get_station):
    station_data = station_schema.Station.from_orm(get_station).dict(by_alias=True)
    station_id = station_data.pop("station_id")

    response = client.delete(
        f"/test/climsoft/v1/stations/{station_id}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/test/climsoft/v1/stations/{station_id}",
    )
    assert response.status_code == 404
