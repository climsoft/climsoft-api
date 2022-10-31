import json
import uuid

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.instrumentfaultreport import (
    schema as instrumentfaultreport_schema,
)
from tests.datagen import (
    instrumentfaultreport as climsoft_instrument_fault_report,
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
def get_instrument_fault_report(
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
    session: Session,
):
    instrument_fault_report = climsoft_models.Instrumentfaultreport(
        **climsoft_instrument_fault_report.get_valid_instrument_fault_report_input(
            station_id=get_station.stationId, instrument_id=get_instrument.instrumentId
        ).dict()
    )
    session.add(instrument_fault_report)
    session.commit()
    yield instrument_fault_report


@pytest.fixture
def get_instrument_fault_reports(
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
    session: Session,
):
    for _ in range(10):
        instrument_fault_report = climsoft_models.Instrumentfaultreport(
            **climsoft_instrument_fault_report.get_valid_instrument_fault_report_input(
                station_id=get_station.stationId,
                instrument_id=get_instrument.instrumentId,
            ).dict()
        )
        session.add(instrument_fault_report)
    session.commit()


def test_should_return_first_five_station_location_histories(
    client: TestClient, get_instrument_fault_reports
):
    response = client.get(
        "/climsoft/v1/instrument-fault-reports",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_instrument_fault_report(
    client: TestClient,
    get_instrument_fault_report: climsoft_models.Instrumentfaultreport,
):
    response = client.get(
        f"/climsoft/v1/instrument-fault-reports/{get_instrument_fault_report.reportId}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_instrument_fault_report(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_instrument: climsoft_models.Instrument,
):
    instrument_fault_report_data = (
        climsoft_instrument_fault_report.get_valid_instrument_fault_report_input(
            station_id=get_station.stationId, instrument_id=get_instrument.instrumentId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/climsoft/v1/instrument-fault-reports",
        data=json.dumps(instrument_fault_report_data, default=str),
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
        "/climsoft/v1/instrument-fault-reports",
        data=json.dumps({"fault_description": "failed"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_instrument_fault_report(
    client: TestClient,
    get_instrument_fault_report: climsoft_models.Instrumentfaultreport,
):
    instrument_fault_report_data = (
        instrumentfaultreport_schema.InstrumentFaultReport.from_orm(
            get_instrument_fault_report
        ).dict(by_alias=True)
    )
    report_id = instrument_fault_report_data.pop("report_id")

    updates = {**instrument_fault_report_data, "reported_by": uuid.uuid4().hex}

    response = client.put(
        f"/climsoft/v1/instrument-fault-reports/{report_id}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["reported_by"] == updates["reported_by"]


def test_should_delete_instrument_fault_report(
    client: TestClient, get_instrument_fault_report
):
    instrument_fault_report_data = (
        instrumentfaultreport_schema.InstrumentFaultReport.from_orm(
            get_instrument_fault_report
        ).dict(by_alias=True)
    )
    report_id = instrument_fault_report_data.pop("report_id")

    response = client.delete(
        f"/climsoft/v1/instrument-fault-reports/{report_id}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/instrument-fault-reports/{report_id}",
    )

    assert response.status_code == 404
