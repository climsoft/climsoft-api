import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models

from climsoft_api.api.acquisition_type import schema as acquisitiontype_schema
from tests.datagen import acquisitiontype as climsoft_acquisition_type
from fastapi.testclient import TestClient


@pytest.fixture
def get_acquisition_type(session: Session):
    acquisition_type = climsoft_models.Acquisitiontype(
        **climsoft_acquisition_type.get_valid_acquisition_type_input().dict()
    )
    session.add(acquisition_type)
    session.commit()
    yield acquisition_type


@pytest.fixture
def get_acquisition_types(session: Session):
    for i in range(10):
        at = climsoft_models.Acquisitiontype(code=i, description=f"description{i}")
        session.add(at)
    session.commit()
    yield


def test_should_return_first_five_acquisition_types(
    client: TestClient, session: Session, get_acquisition_types
):
    assert session.query(climsoft_models.Acquisitiontype).count() == 10
    response = client.get("/v1/acquisition-types", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, acquisitiontype_schema.AcquisitionType)


def test_should_return_single_acquisition_type(
    client: TestClient, get_acquisition_type: climsoft_models.Acquisitiontype
):
    response = client.get(
        f"/v1/acquisition-types/{get_acquisition_type.code}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, acquisitiontype_schema.AcquisitionType)


def test_should_create_a_acquisition_type(client: TestClient):
    acquisition_type_data = (
        climsoft_acquisition_type.get_valid_acquisition_type_input().dict(by_alias=True)
    )
    response = client.post(
        "/v1/acquisition-types/",
        data=json.dumps(acquisition_type_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, acquisitiontype_schema.AcquisitionType)


def test_should_raise_validation_error(client: TestClient):
    acquisition_type_data = {"code": "asd", "description": "aa aa a"}
    response = client.post(
        "/v1/acquisition-types/", data=json.dumps(acquisition_type_data, default=str)
    )
    assert response.status_code == 422


def test_should_update_acquisition_type(client: TestClient, get_acquisition_type):
    acquisition_type_data = acquisitiontype_schema.AcquisitionType.from_orm(
        get_acquisition_type
    ).dict(by_alias=True)
    code = acquisition_type_data.pop("code")
    updates = {**acquisition_type_data, "description": "updated description"}

    response = client.put(
        f"/v1/acquisition-types/{code}", data=json.dumps(updates, default=str)
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_acquisition_type(client: TestClient, get_acquisition_type):
    acquisition_type_data = acquisitiontype_schema.AcquisitionType.from_orm(
        get_acquisition_type
    ).dict(by_alias=True)
    code = acquisition_type_data.pop("code")

    response = client.delete(f"/v1/acquisition-types/{code}")
    assert response.status_code == 200

    response = client.get(f"/v1/acquisition-types/{code}")
    assert response.status_code == 404
