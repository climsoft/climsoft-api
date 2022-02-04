import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.instrument import schema as instrument_schema
from tests.datagen import instrument as climsoft_instrument, station as climsoft_station
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
def get_instrument(get_station: climsoft_models.Station, session: Session):
    instrument = climsoft_models.Instrument(
        **climsoft_instrument.get_valid_instrument_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(instrument)
    session.commit()
    yield instrument


@pytest.fixture
def get_instruments(get_station: climsoft_models.Station, session: Session):
    for _ in range(10):
        instrument = climsoft_models.Instrument(
            **climsoft_instrument.get_valid_instrument_input(
                station_id=get_station.stationId
            ).dict()
        )
        session.add(instrument)
    session.commit()


def test_should_return_first_five_instruments(client: TestClient, get_instruments):
    response = client.get("/v1/instruments/", params={"limit": 5}, headers={})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_instrument(
    client: TestClient, get_instrument: climsoft_models.Instrument
):
    response = client.get(f"/v1/instruments/{get_instrument.instrumentId}", headers={})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_instrument(
    client: TestClient, get_station: climsoft_models.Station
):
    instrument_data = climsoft_instrument.get_valid_instrument_input(
        station_id=get_station.stationId
    ).dict(by_alias=True)
    response = client.post(
        "/v1/instruments/", data=json.dumps(instrument_data, default=str), headers={}
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient, get_station: climsoft_models.Station
):
    response = client.post(
        "/v1/instruments/",
        data=json.dumps({"instrument_name": "some name"}, default=str),
        headers={},
    )
    assert response.status_code == 422


def test_should_update_instrument(
    client: TestClient, get_instrument: climsoft_models.Instrument
):
    instrument_data = instrument_schema.Instrument.from_orm(get_instrument).dict(
        by_alias=True
    )
    instrument_id = instrument_data.pop("instrument_id")
    updates = {**instrument_data, "instrument_name": "updated name"}

    response = client.put(
        f"/v1/instruments/{instrument_id}",
        data=json.dumps(updates, default=str),
        headers={},
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["instrument_name"] == updates["instrument_name"]


def test_should_delete_instrument(client: TestClient, get_instrument):
    instrument_data = instrument_schema.Instrument.from_orm(get_instrument).dict(
        by_alias=True
    )
    instrument_id = instrument_data.pop("instrument_id")

    response = client.delete(f"/v1/instruments/{instrument_id}", headers={})
    assert response.status_code == 200

    response = client.get(f"/v1/instruments/{instrument_id}", headers={})

    assert response.status_code == 404
