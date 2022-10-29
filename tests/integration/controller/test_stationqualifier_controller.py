import json

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.stationqualifier import schema as stationqualifier_schema
from tests.datagen import (
    stationqualifier as climsoft_station_qualifier,
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
    session.close()


@pytest.fixture
def get_station_qualifier(get_station: climsoft_models.Station, session: Session):
    station_qualifier = climsoft_models.Stationqualifier(
        **climsoft_station_qualifier.get_valid_station_qualifier_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(station_qualifier)
    session.commit()
    yield station_qualifier
    session.close()


@pytest.fixture
def get_station_qualifiers(session: Session):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.commit()

        session.add(
            climsoft_models.Stationqualifier(
                **climsoft_station_qualifier.get_valid_station_qualifier_input(
                    station_id=station.stationId
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_station_qualifiers(
    client: TestClient, get_station_qualifiers
):
    response = client.get(
        "/v1/station-qualifiers",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_station_qualifier(
    client: TestClient,
    get_station_qualifier: climsoft_models.Stationqualifier,
):
    response = client.get(
        f"/v1/station-qualifiers/{get_station_qualifier.qualifier}/{get_station_qualifier.qualifierBeginDate}/{get_station_qualifier.qualifierEndDate}/{get_station_qualifier.belongsTo}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_station_qualifier(
    client: TestClient, get_station: climsoft_models.Station
):
    station_qualifier_data = (
        climsoft_station_qualifier.get_valid_station_qualifier_input(
            station_id=get_station.stationId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/v1/station-qualifiers",
        data=json.dumps(station_qualifier_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient, get_station: climsoft_models.Station
):
    response = client.post(
        "/v1/station-qualifiers",
        data=json.dumps({"station_time_zone": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_station_qualifier(
    client: TestClient,
    get_station_qualifier: climsoft_models.Stationqualifier,
):
    station_qualifier_data = stationqualifier_schema.StationQualifier.from_orm(
        get_station_qualifier
    ).dict(by_alias=True)
    belongs_to = station_qualifier_data.pop("belongs_to")
    qualifier_begin_date = station_qualifier_data.pop("qualifier_begin_date")
    qualifier_end_date = station_qualifier_data.pop("qualifier_end_date")
    qualifier = station_qualifier_data.pop("qualifier")
    updates = {**station_qualifier_data, "station_timezone": 1}

    response = client.put(
        f"/v1/station-qualifiers/{qualifier}/{qualifier_begin_date}/{qualifier_end_date}/{belongs_to}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["station_timezone"] == updates["station_timezone"]


def test_should_delete_station_qualifier(
    client: TestClient,
    get_station_qualifier: stationqualifier_schema.StationQualifier,
):
    station_qualifier_data = stationqualifier_schema.StationQualifier.from_orm(
        get_station_qualifier
    ).dict(by_alias=True)
    belongs_to = station_qualifier_data.pop("belongs_to")
    qualifier_begin_date = station_qualifier_data.pop("qualifier_begin_date")
    qualifier_end_date = station_qualifier_data.pop("qualifier_end_date")
    qualifier = station_qualifier_data.pop("qualifier")
    response = client.delete(
        f"/v1/station-qualifiers/{qualifier}/{qualifier_begin_date}/{qualifier_end_date}/{belongs_to}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/station-qualifiers/{qualifier}/{qualifier_begin_date}/{qualifier_end_date}/{belongs_to}",
    )

    assert response.status_code == 404
