import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.physicalfeatureclass import schema as physicalfeatureclass_schema
from tests.datagen import (
    physicalfeatureclass as climsoft_physical_feature_class,
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
def get_physical_feature_class(get_station: climsoft_models.Station, session: Session):
    physical_feature_class = climsoft_models.Physicalfeatureclas(
        **climsoft_physical_feature_class.get_valid_physical_feature_class_input(
            station_id=get_station.stationId
        ).dict()
    )
    session.add(physical_feature_class)
    session.commit()
    yield physical_feature_class
    session.close()


@pytest.fixture
def get_physical_feature_classes(session: Session):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.flush()

        session.add(
            climsoft_models.Physicalfeatureclas(
                **climsoft_physical_feature_class.get_valid_physical_feature_class_input(
                    station_id=station.stationId
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_physical_feature_class(
    client: TestClient, get_physical_feature_classes
):
    response = client.get(
        "/v1/physical-feature-class/",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_physical_feature_class(
    client: TestClient,
    get_physical_feature_class: climsoft_models.Physicalfeatureclas,
):
    response = client.get(
        f"/v1/physical-feature-class/{get_physical_feature_class.featureClass}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_physical_feature_class(
    client: TestClient, get_station: climsoft_models.Station
):
    physical_feature_class_data = (
        climsoft_physical_feature_class.get_valid_physical_feature_class_input(
            station_id=get_station.stationId
        ).dict(by_alias=True)
    )
    response = client.post(
        "/v1/physical-feature-class/",
        data=json.dumps(physical_feature_class_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient, get_station: climsoft_models.Station
):
    response = client.post(
        "/v1/physical-feature-class/",
        data=json.dumps({"feature_class": "fail"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_physical_feature_class(
    client: TestClient,
    get_physical_feature_class: climsoft_models.Physicalfeatureclas,
):
    physical_feature_class_data = (
        physicalfeatureclass_schema.PhysicalFeatureClass.from_orm(
            get_physical_feature_class
        ).dict(by_alias=True)
    )
    feature_class = physical_feature_class_data.pop("featureClass")
    updates = {**physical_feature_class_data, "description": "updated description"}

    response = client.put(
        f"/v1/physical-feature-class/{feature_class}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_physical_feature_class(
    client: TestClient, get_physical_feature_class
):
    physical_feature_class_data = (
        physicalfeatureclass_schema.PhysicalFeatureClass.from_orm(
            get_physical_feature_class
        ).dict(by_alias=True)
    )
    feature_class = physical_feature_class_data.pop("featureClass")

    response = client.delete(
        f"/v1/physical-feature-class/{feature_class}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/physical-feature-class/{feature_class}",
    )

    assert response.status_code == 404
