import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.obselement import schema as obselement_schema
from tests.datagen import obselement as climsoft_obselement
from fastapi.testclient import TestClient


@pytest.fixture
def get_obselement(session: Session):
    obselement = climsoft_models.Obselement(
        **climsoft_obselement.get_valid_obselement_input().dict()
    )
    session.add(obselement)
    session.commit()
    yield obselement
    session.close()


@pytest.fixture
def get_obselements(session: Session):
    for _ in range(10):
        obselement = climsoft_models.Obselement(
            **climsoft_obselement.get_valid_obselement_input().dict()
        )
        session.add(obselement)
    session.commit()


def test_should_return_first_five_obselements(client: TestClient, get_obselements):
    response = client.get(
        "/climsoft/v1/obselements",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, obselement_schema.ObsElement)


def test_should_return_single_obselement(
    client: TestClient,
    get_obselement: climsoft_models.Obselement,
):
    response = client.get(
        f"/climsoft/v1/obselements/{get_obselement.elementId}",
    )

    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, obselement_schema.ObsElement)


def test_should_create_a_obselement(client: TestClient):
    obselement_data = climsoft_obselement.get_valid_obselement_input().dict(
        by_alias=True
    )
    response = client.post(
        "/climsoft/v1/obselements",
        data=json.dumps(obselement_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, obselement_schema.ObsElement)


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/obselements",
        data=json.dumps({"element_name": "element name"}, default=str),
    )
    assert response.status_code == 422


def test_should_update_obselement(client: TestClient, get_obselement):
    obselement_data = obselement_schema.ObsElement.from_orm(get_obselement).dict(
        by_alias=True
    )
    element_id = obselement_data.pop("element_id")
    updates = {**obselement_data, "element_name": "updated name"}
    response = client.put(
        f"/climsoft/v1/obselements/{element_id}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["element_name"] == updates["element_name"]


def test_should_delete_obselement(client: TestClient, get_obselement):
    obselement_data = obselement_schema.ObsElement.from_orm(get_obselement).dict(
        by_alias=True
    )
    element_id = obselement_data.pop("element_id")

    response = client.delete(
        f"/climsoft/v1/obselements/{element_id}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/obselements/{element_id}",
    )

    assert response.status_code == 404
