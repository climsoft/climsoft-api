import json
import uuid
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.physicalfeature import schema as physicalfeature_schema
from tests.datagen import (
    physicalfeature as climsoft_physical_feature,
    station as climsoft_station,
    physicalfeatureclass as climsoft_physical_feature_class,
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
def get_physical_feature(
    get_station: climsoft_models.Station,
    get_physical_feature_class: climsoft_models.Physicalfeatureclas,
    session: Session,
):
    physical_feature = climsoft_models.Physicalfeature(
        **climsoft_physical_feature.get_valid_physical_feature_input(
            station_id=get_station.stationId,
            feature_class=get_physical_feature_class.featureClass,
        ).dict()
    )
    session.add(physical_feature)
    session.commit()
    yield physical_feature
    session.close()


@pytest.fixture
def get_physical_features(session: Session):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.flush()

        physical_feature_class = climsoft_models.Physicalfeatureclas(
            **climsoft_physical_feature_class.get_valid_physical_feature_class_input(
                station_id=station.stationId
            ).dict()
        )
        session.add(physical_feature_class)
        session.flush()

        session.add(
            climsoft_models.Physicalfeature(
                **climsoft_physical_feature.get_valid_physical_feature_input(
                    station_id=station.stationId,
                    feature_class=physical_feature_class.featureClass,
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_station_location_histories(
    client: TestClient, get_physical_features
):
    response = client.get(
        "/v1/physical-features",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_physical_feature(
    client: TestClient,
    get_physical_feature: climsoft_models.Physicalfeature,
):
    response = client.get(
        f"/v1/physical-features/{get_physical_feature.associatedWith}/{get_physical_feature.beginDate}/{get_physical_feature.classifiedInto}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_physical_feature(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_physical_feature_class: climsoft_models.Physicalfeatureclas,
):
    physical_feature_data = climsoft_physical_feature.get_valid_physical_feature_input(
        station_id=get_station.stationId,
        feature_class=get_physical_feature_class.featureClass,
    ).dict(by_alias=True)
    response = client.post(
        "/v1/physical-features",
        data=json.dumps(physical_feature_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_physical_feature_class: climsoft_models.Physicalfeatureclas,
):
    response = client.post(
        "/v1/physical-features",
        data=json.dumps({"featuer_class": "fail"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_physical_feature(
    client: TestClient,
    get_physical_feature: climsoft_models.Physicalfeature,
):
    physical_feature_data = physicalfeature_schema.PhysicalFeature.from_orm(
        get_physical_feature
    ).dict(by_alias=True)

    associated_with = physical_feature_data.pop("associated_with")
    begin_date = physical_feature_data.pop("begin_date")
    classified_into = physical_feature_data.pop("classified_into")

    updates = {**physical_feature_data, "image": uuid.uuid4().hex}

    response = client.put(
        f"/v1/physical-features/{associated_with}/{begin_date}/{classified_into}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["image"] == updates["image"]


def test_should_delete_physical_feature(client: TestClient, get_physical_feature):
    physical_feature_data = physicalfeature_schema.PhysicalFeature.from_orm(
        get_physical_feature
    ).dict(by_alias=True)

    associated_with = physical_feature_data.pop("associated_with")
    begin_date = physical_feature_data.pop("begin_date")
    classified_into = physical_feature_data.pop("classified_into")

    response = client.delete(
        f"/v1/physical-features/{associated_with}/{begin_date}/{classified_into}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/physical-features/{associated_with}/{begin_date}/{classified_into}",
    )

    assert response.status_code == 404


def test_should_fail_for_different_description(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_physical_feature_class: climsoft_models.Physicalfeatureclas,
    session: Session,
):
    pf_input_data = climsoft_physical_feature.get_valid_physical_feature_input(
        station_id=get_station.stationId,
        feature_class=get_physical_feature_class.featureClass,
    ).dict()

    pf_input_data["description"] = "test description"
    physical_feature1 = climsoft_models.Physicalfeature(
        **pf_input_data
    )
    session.add(physical_feature1)

    pf_input_data["description"] = "test description2"
    physical_feature2 = climsoft_models.Physicalfeature(
        **pf_input_data
    )
    session.add(physical_feature2)
    session.commit()

    session.close()

    with pytest.raises(Exception):
        client.get(
            f"/v1/physical-features/{pf_input_data['associated_with']}/{pf_input_data['begin_date']}/{pf_input_data['classified_into']}",
        )
