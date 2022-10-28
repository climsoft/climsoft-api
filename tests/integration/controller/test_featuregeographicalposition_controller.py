import datetime
import json
import pytest
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from sqlalchemy.orm.session import Session
from climsoft_api.api.featuregeographicalposition import (
    schema as featuregeographicalposition_schema,
)
from tests.datagen import (
    featuregeographicalposition as climsoft_feature_geographical_position,
    synopfeature as climsoft_synop_feature,
)
from fastapi.testclient import TestClient


@pytest.fixture
def get_synop_feature(session: Session):
    synop_feature = climsoft_models.Synopfeature(
        **climsoft_synop_feature.get_valid_synop_feature_input().dict()
    )
    session.add(synop_feature)
    session.commit()
    yield synop_feature


@pytest.fixture
def get_feature_geographical_position(
    get_synop_feature: climsoft_models.Synopfeature, session: Session
):
    feature_geographical_position = climsoft_models.Featuregeographicalposition(
        **climsoft_feature_geographical_position.get_valid_feature_geographical_position_input(
            synop_feature_abbreviation=get_synop_feature.abbreviation
        ).dict()
    )
    session.add(feature_geographical_position)
    session.commit()
    yield feature_geographical_position


@pytest.fixture
def get_feature_geographical_positions(
    get_synop_feature: climsoft_models.Synopfeature, session: Session
):
    for _ in range(10):
        feature_geographical_position = climsoft_models.Featuregeographicalposition(
            **climsoft_feature_geographical_position.get_valid_feature_geographical_position_input(
                synop_feature_abbreviation=get_synop_feature.abbreviation
            ).dict()
        )
        session.add(feature_geographical_position)
    session.commit()
    yield feature_geographical_position


def test_should_return_first_five_feature_geographical_positions(
    client: TestClient, get_feature_geographical_positions
):
    response = client.get(
        "/test/climsoft/v1/feature-geographical-positions",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_feature_geographical_position(
    client: TestClient,
    get_feature_geographical_position: climsoft_models.Featuregeographicalposition,
):
    response = client.get(
        f"/test/climsoft/v1/feature-geographical-positions/{get_feature_geographical_position.belongsTo}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_feature_geographical_position(
    client: TestClient,
    get_synop_feature: climsoft_models.Synopfeature,
):
    feature_geographical_position_data = climsoft_feature_geographical_position.get_valid_feature_geographical_position_input(
        synop_feature_abbreviation=get_synop_feature.abbreviation
    ).dict(
        by_alias=True
    )
    response = client.post(
        "/test/climsoft/v1/feature-geographical-positions",
        data=json.dumps(feature_geographical_position_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient,
    get_synop_feature: climsoft_models.Synopfeature,
):
    response = client.post(
        "/test/climsoft/v1/feature-geographical-positions",
        data=json.dumps({"belongs_to": get_synop_feature.abbreviation}, default=str),
    )
    assert response.status_code == 422


def test_should_update_feature_geographical_position(
    client: TestClient,
    get_feature_geographical_position: climsoft_models.Featuregeographicalposition,
):
    feature_geographical_position_data = (
        featuregeographicalposition_schema.FeatureGeographicalPosition.from_orm(
            get_feature_geographical_position
        ).dict(by_alias=True)
    )
    belongs_to = feature_geographical_position_data.pop("belongs_to")
    updates = {
        **feature_geographical_position_data,
        "observed_on": datetime.datetime.utcnow().isoformat(),
    }

    response = client.put(
        f"/test/climsoft/v1/feature-geographical-positions/{belongs_to}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["observed_on"] == updates["observed_on"]


def test_should_delete_feature_geographical_position(
    client: TestClient, get_feature_geographical_position
):
    feature_geographical_position_data = (
        featuregeographicalposition_schema.FeatureGeographicalPosition.from_orm(
            get_feature_geographical_position
        ).dict(by_alias=True)
    )
    belongs_to = feature_geographical_position_data.pop("belongs_to")

    response = client.delete(
        f"/test/climsoft/v1/feature-geographical-positions/{belongs_to}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/test/climsoft/v1/feature-geographical-positions/{belongs_to}",
    )

    assert response.status_code == 404
