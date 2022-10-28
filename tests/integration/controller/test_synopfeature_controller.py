import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.synopfeature import schema as synopfeature_schema
from tests.datagen import synopfeature as climsoft_synopfeature
from fastapi.testclient import TestClient


@pytest.fixture
def get_synop_feature(session: Session):
    synop_feature = climsoft_models.Synopfeature(
        **climsoft_synopfeature.get_valid_synop_feature_input().dict()
    )
    session.add(synop_feature)
    session.commit()
    yield synop_feature
    session.close()


@pytest.fixture
def get_synop_features(session: Session):
    for _ in range(1, 11):
        session.add(
            climsoft_models.Synopfeature(
                **climsoft_synopfeature.get_valid_synop_feature_input().dict()
            )
        )
    session.commit()


def test_should_return_first_five_synop_features(
    client: TestClient, get_synop_features
):
    response = client.get(
        "/test/climsoft/v1/synop-features",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_synop_feature(
    client: TestClient,
    get_synop_feature: climsoft_models.Synopfeature,
):
    response = client.get(
        f"/test/climsoft/v1/synop-features/{get_synop_feature.abbreviation}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_synop_feature(client: TestClient, get_synop_features):
    synop_feature_data = climsoft_synopfeature.get_valid_synop_feature_input().dict(
        by_alias=True
    )
    response = client.post(
        "/test/climsoft/v1/synop-features",
        data=json.dumps(synop_feature_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient, get_synop_features):
    synop_feature_data = {"aaa": "bbbbbbb"}
    response = client.post(
        "/test/climsoft/v1/synop-features",
        data=json.dumps(synop_feature_data, default=str),
    )
    assert response.status_code == 422


def test_should_update_synop_feature(
    client: TestClient, get_synop_feature, get_synop_features
):
    synop_feature_data = synopfeature_schema.SynopFeature.from_orm(
        get_synop_feature
    ).dict(by_alias=True)
    abbreviation = synop_feature_data.pop("abbreviation")
    updates = {**synop_feature_data, "description": "updated name"}

    response = client.put(
        f"/test/climsoft/v1/synop-features/{abbreviation}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_synop_feature(client: TestClient, get_synop_feature):
    synop_feature_data = synopfeature_schema.SynopFeature.from_orm(
        get_synop_feature
    ).dict(by_alias=True)
    abbreviation = synop_feature_data.pop("abbreviation")

    response = client.delete(
        f"/test/climsoft/v1/synop-features/{abbreviation}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/test/climsoft/v1/synop-features/{abbreviation}",
    )
    assert response.status_code == 404
