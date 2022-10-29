import json
import uuid

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.faultresolution import schema as faultresolution_schema
from tests.datagen import (
    faultresolution as climsoft_fault_resolution,
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
def get_fault_resolution(
    get_instrument_fault_report: climsoft_models.Instrumentfaultreport, session: Session
):
    fault_resolution = climsoft_models.Faultresolution(
        **climsoft_fault_resolution.get_valid_fault_resolution_input(
            instrument_fault_report_id=get_instrument_fault_report.reportId
        ).dict()
    )
    session.add(fault_resolution)
    session.commit()
    yield fault_resolution


@pytest.fixture
def get_fault_resolutions(
    session: Session, get_instrument_fault_report: climsoft_models.Instrumentfaultreport
):
    for _ in range(10):
        fault_resolution = climsoft_models.Faultresolution(
            **climsoft_fault_resolution.get_valid_fault_resolution_input(
                instrument_fault_report_id=get_instrument_fault_report.reportId
            ).dict()
        )
        session.add(fault_resolution)
    session.commit()


def test_should_return_first_five_station_location_histories(
    client: TestClient, get_fault_resolutions
):
    response = client.get(
        "/climsoft/v1/fault-resolutions",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_fault_resolution(
    client: TestClient,
    get_fault_resolution: climsoft_models.Faultresolution,
):
    response = client.get(
        f"/climsoft/v1/fault-resolutions/{get_fault_resolution.resolvedDatetime}/{get_fault_resolution.associatedWith}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_fault_resolution(
    client: TestClient,
    get_instrument_fault_report: climsoft_models.Instrumentfaultreport,
):
    fault_resolution_data = climsoft_fault_resolution.get_valid_fault_resolution_input(
        instrument_fault_report_id=get_instrument_fault_report.reportId
    ).dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/fault-resolutions",
        data=json.dumps(fault_resolution_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient,
    get_instrument_fault_report: climsoft_models.Instrumentfaultreport,
):
    response = client.post(
        "/climsoft/v1/fault-resolutions",
        data=json.dumps(
            {"report_id": get_instrument_fault_report.reportId}, default=str
        ),
    )
    assert response.status_code == 422


def test_should_update_fault_resolution(
    client: TestClient,
    get_fault_resolution: climsoft_models.Faultresolution,
):
    fault_resolution_data = faultresolution_schema.FaultResolution.from_orm(
        get_fault_resolution
    ).dict(by_alias=True)

    resolved_datetime = fault_resolution_data.pop("resolved_datetime")
    associated_with = fault_resolution_data.pop("associated_with")

    updates = {**fault_resolution_data, "remarks": uuid.uuid4().hex}

    response = client.put(
        f"/climsoft/v1/fault-resolutions/{resolved_datetime}/{associated_with}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["remarks"] == updates["remarks"]


def test_should_delete_fault_resolution(client: TestClient, get_fault_resolution):
    fault_resolution_data = faultresolution_schema.FaultResolution.from_orm(
        get_fault_resolution
    ).dict(by_alias=True)

    resolved_datetime = fault_resolution_data.pop("resolved_datetime")
    associated_with = fault_resolution_data.pop("associated_with")

    response = client.delete(
        f"/climsoft/v1/fault-resolutions/{resolved_datetime}/{associated_with}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/fault-resolutions/{resolved_datetime}/{associated_with}",
    )

    assert response.status_code == 404
