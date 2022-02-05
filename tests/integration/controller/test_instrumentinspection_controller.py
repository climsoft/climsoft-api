import json
import uuid

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.instrumentinspection import schema as instrumentinspection_schema
from tests.datagen import (
    instrumentinspection as climsoft_instrument_inspection,
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
def get_instrument_inspection(
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
    session: Session,
):
    instrument_inspection = climsoft_models.Instrumentinspection(
        **climsoft_instrument_inspection.get_valid_instrument_inspection_input(
            station_id=get_station.stationId, instrument_id=get_instrument.instrumentId
        ).dict()
    )
    session.add(instrument_inspection)
    session.commit()
    yield instrument_inspection


@pytest.fixture
def get_instrument_inspections(
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
    session: Session,
):
    for _ in range(10):
        instrument_inspection = climsoft_models.Instrumentinspection(
            **climsoft_instrument_inspection.get_valid_instrument_inspection_input(
                station_id=get_station.stationId,
                instrument_id=get_instrument.instrumentId,
            ).dict()
        )
        session.add(instrument_inspection)
    session.commit()


def test_should_return_first_five_instrument_inspections(
    client: TestClient, get_instrument_inspections
):
    response = client.get(
        "/v1/instrument-inspections/",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_instrument_inspection(
    client: TestClient,
    get_instrument_inspection: climsoft_models.Instrumentinspection,
):
    response = client.get(
        f"/v1/instrument-inspections/{get_instrument_inspection.performedOn}/{get_instrument_inspection.inspectionDatetime}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_instrument_inspection(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
):
    instrument_inspection_data = (
        climsoft_instrument_inspection.get_valid_instrument_inspection_input(
            station_id=get_station.stationId, instrument_id=get_instrument.instrumentId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/v1/instrument-inspections/",
        data=json.dumps(instrument_inspection_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
):
    response = client.post(
        "/v1/instrument-inspections/",
        data=json.dumps({"performed_by": "John"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_instrument_inspection(
    client: TestClient,
    get_instrument_inspection: climsoft_models.Instrumentinspection,
):
    instrument_inspection_data = (
        instrumentinspection_schema.InstrumentInspection.from_orm(
            get_instrument_inspection
        ).dict(by_alias=True)
    )

    performed_on = instrument_inspection_data.pop("performed_on")
    inspection_datetime = instrument_inspection_data.pop("inspection_datetime")

    updates = {**instrument_inspection_data, "status": uuid.uuid4().hex}

    response = client.put(
        f"/v1/instrument-inspections/{performed_on}/{inspection_datetime}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["status"] == updates["status"]


def test_should_delete_instrument_inspection(
    client: TestClient, get_instrument_inspection
):
    instrument_inspection_data = (
        instrumentinspection_schema.InstrumentInspection.from_orm(
            get_instrument_inspection
        ).dict(by_alias=True)
    )

    performed_on = instrument_inspection_data.pop("performed_on")
    inspection_datetime = instrument_inspection_data.pop("inspection_datetime")

    response = client.delete(
        f"/v1/instrument-inspections/{performed_on}/{inspection_datetime}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/instrument-inspections/{performed_on}/{inspection_datetime}",
    )

    assert response.status_code == 404
