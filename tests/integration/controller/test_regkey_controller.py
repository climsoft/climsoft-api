import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.regkey import schema as regkey_schema
from tests.datagen import regkey as climsoft_regkey
from fastapi.testclient import TestClient


@pytest.fixture
def get_reg_key(session: Session):
    reg_key = climsoft_models.Regkey(**climsoft_regkey.get_valid_reg_key_input().dict())
    session.add(reg_key)
    session.commit()
    yield reg_key
    session.close()


@pytest.fixture
def get_reg_keys(session: Session):
    for _ in range(1, 11):
        session.add(
            climsoft_models.Regkey(**climsoft_regkey.get_valid_reg_key_input().dict())
        )
    session.commit()


def test_should_return_first_five_reg_keys(client: TestClient, get_reg_keys):
    response = client.get(
        "/v1/reg-keys",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_reg_key(
    client: TestClient, get_reg_key: climsoft_models.Regkey
):
    response = client.get(
        f"/v1/reg-keys/{get_reg_key.keyName}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_reg_key(client: TestClient):
    reg_key_data = climsoft_regkey.get_valid_reg_key_input().dict(by_alias=True)
    response = client.post(
        "/v1/reg-keys",
        data=json.dumps(reg_key_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    reg_key_data = {"aaa": "bbbbbbb"}
    response = client.post(
        "/v1/reg-keys",
        data=json.dumps(reg_key_data, default=str),
    )
    assert response.status_code == 422


def test_should_update_reg_key(client: TestClient, get_reg_key):
    reg_key_data = regkey_schema.RegKey.from_orm(get_reg_key).dict(by_alias=True)
    key_name = reg_key_data.pop("key_name")
    updates = {**reg_key_data, "key_description": "updated name"}

    response = client.put(
        f"/v1/reg-keys/{key_name}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["key_description"] == updates["key_description"]


def test_should_delete_reg_key(client: TestClient, get_reg_key):
    reg_key_data = regkey_schema.RegKey.from_orm(get_reg_key).dict(by_alias=True)
    key_name = reg_key_data.pop("key_name")

    response = client.delete(
        f"/v1/reg-keys/{key_name}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/reg-keys/{key_name}",
    )
    assert response.status_code == 404
