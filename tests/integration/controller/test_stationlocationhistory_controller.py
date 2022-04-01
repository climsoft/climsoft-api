import json
import uuid

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.stationlocationhistory import (
    schema as stationlocationhistory_schema,
)
from tests.datagen import (
    stationlocationhistory as climsoft_station_location_history,
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
def get_station_location_history(
    get_station: climsoft_models.Station, session: Session
):
    station_location_history = climsoft_models.Stationlocationhistory(
        **climsoft_station_location_history.get_valid_station_location_history_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(station_location_history)
    session.commit()
    yield station_location_history
    session.close()


@pytest.fixture
def get_station_location_histories(session: Session):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.flush()

        session.add(
            climsoft_models.Stationlocationhistory(
                **climsoft_station_location_history.get_valid_station_location_history_input(
                    station_id=station.stationId
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_station_location_histories(
    client: TestClient, get_station_location_histories
):
    response = client.get(
        "/v1/station-location-histories",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_station_location_history(
    client: TestClient,
    get_station_location_history: climsoft_models.Stationlocationhistory,
):
    response = client.get(
        f"/v1/station-location-histories/{get_station_location_history.belongsTo}/{get_station_location_history.openingDatetime}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_station_location_history(
    client: TestClient, get_station: climsoft_models.Station
):
    station_location_history_data = (
        climsoft_station_location_history.get_valid_station_location_history_input(
            station_id=get_station.stationId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/v1/station-location-histories",
        data=json.dumps(station_location_history_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient, get_station: climsoft_models.Station
):
    response = client.post(
        "/v1/station-location-histories",
        data=json.dumps({"geo_location_history": "fail"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_station_location_history(
    client: TestClient,
    get_station_location_history: climsoft_models.Stationlocationhistory,
):
    station_location_history_data = (
        stationlocationhistory_schema.StationLocationHistory.from_orm(
            get_station_location_history
        ).dict(by_alias=True)
    )
    belongs_to = station_location_history_data.pop("belongs_to")
    opening_datetime = station_location_history_data.pop("opening_datetime")
    updates = {**station_location_history_data, "authority": uuid.uuid4().hex}

    response = client.put(
        f"/v1/station-location-histories/{belongs_to}/{opening_datetime}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["authority"] == updates["authority"]


def test_should_delete_station_location_history(
    client: TestClient, get_station_location_history
):
    station_location_history_data = (
        stationlocationhistory_schema.StationLocationHistory.from_orm(
            get_station_location_history
        ).dict(by_alias=True)
    )
    belongs_to = station_location_history_data.pop("belongs_to")
    opening_datetime = station_location_history_data.pop("opening_datetime")

    response = client.delete(
        f"/v1/station-location-histories/{belongs_to}/{opening_datetime}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/station-location-histories/{belongs_to}/{opening_datetime}",
    )

    assert response.status_code == 404
