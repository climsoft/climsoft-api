import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.qctype import schema as qctype_schema
from tests.datagen import qctype as climsoft_qctype
from fastapi.testclient import TestClient


@pytest.fixture
def get_qc_type(session: Session):
    qc_type = climsoft_models.Qctype(**climsoft_qctype.get_valid_qc_type_input().dict())
    session.add(qc_type)
    session.commit()
    yield qc_type
    session.close()


@pytest.fixture
def get_qc_types(session: Session):
    for _ in range(1, 11):
        session.add(
            climsoft_models.Qctype(**climsoft_qctype.get_valid_qc_type_input().dict())
        )
    session.commit()


def test_should_return_first_five_qc_types(client: TestClient, get_qc_types):
    response = client.get("/test/climsoft/v1/qc-types", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_qc_type(
    client: TestClient, get_qc_type: climsoft_models.Qctype
):
    response = client.get(f"/test/climsoft/v1/qc-types/{get_qc_type.code}")
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_qc_type(client: TestClient):
    qc_type_data = climsoft_qctype.get_valid_qc_type_input().dict(by_alias=True)
    response = client.post("/test/climsoft/v1/qc-types", data=json.dumps(qc_type_data, default=str))
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    qc_type_data = {"aaa": "bbbbbbb"}
    response = client.post("/test/climsoft/v1/qc-types", data=json.dumps(qc_type_data, default=str))
    assert response.status_code == 422


def test_should_update_qc_type(client: TestClient, get_qc_type):
    qc_type_data = qctype_schema.QCType.from_orm(get_qc_type).dict(by_alias=True)
    code = qc_type_data.pop("code")
    updates = {**qc_type_data, "description": "updated name"}

    response = client.put(f"/test/climsoft/v1/qc-types/{code}", data=json.dumps(updates, default=str))
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_qc_type(client: TestClient, get_qc_type):
    qc_type_data = qctype_schema.QCType.from_orm(get_qc_type).dict(by_alias=True)
    code = qc_type_data.pop("code")

    response = client.delete(f"/test/climsoft/v1/qc-types/{code}")
    assert response.status_code == 200

    response = client.get(f"/test/climsoft/v1/qc-types/{code}")
    assert response.status_code == 404
