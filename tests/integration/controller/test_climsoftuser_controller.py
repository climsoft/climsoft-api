import json
import random

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.climsoftuser import schema as climsoftuser_schema
from tests.datagen import climsoftuser as climsoft_climsoft_user
from fastapi.testclient import TestClient


@pytest.fixture
def get_climsoft_user(session: Session):
    climsoft_user = climsoft_models.ClimsoftUser(
        **climsoft_climsoft_user.get_valid_climsoft_user_input().dict()
    )
    session.add(climsoft_user)
    session.commit()
    yield climsoft_user


@pytest.fixture
def get_climsoft_users(session: Session):
    for i in range(10):
        cu = climsoft_models.ClimsoftUser(
            **climsoft_climsoft_user.get_valid_climsoft_user_input().dict()
        )
        session.add(cu)
    session.commit()
    yield
    session.close()


def test_should_return_first_five_climsoft_users(
    client: TestClient, session: Session, get_climsoft_users
):
    response = client.get("/climsoft/v1/climsoft-users", params={"limit": 5})
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, climsoftuser_schema.ClimsoftUser)


def test_should_return_single_climsoft_user(
    client: TestClient, get_climsoft_user: climsoft_models.ClimsoftUser
):
    response = client.get(
        f"/climsoft/v1/climsoft-users/{get_climsoft_user.userName}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, climsoftuser_schema.ClimsoftUser)


def test_should_create_a_climsoft_user(client: TestClient):
    climsoft_user_data = (
        climsoft_climsoft_user.get_valid_climsoft_user_input().dict(by_alias=True)
    )
    response = client.post(
        "/climsoft/v1/climsoft-users",
        data=json.dumps(climsoft_user_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, climsoftuser_schema.ClimsoftUser)


def test_should_raise_validation_error(client: TestClient):
    climsoft_user_data = {"code": "asd", "description": "aa aa a"}
    response = client.post(
        "/climsoft/v1/climsoft-users", data=json.dumps(climsoft_user_data, default=str)
    )
    assert response.status_code == 422


def test_should_update_climsoft_user(client: TestClient, get_climsoft_user):
    target_role = random.choice([role.value for role in climsoftuser_schema.ClimsoftUserRole])
    response = client.put(
        f"/climsoft/v1/climsoft-users/{get_climsoft_user.userName}/update-role/{target_role}"
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["role"] == target_role


def test_should_delete_climsoft_user(client: TestClient, get_climsoft_user):
    response = client.delete(f"/climsoft/v1/climsoft-users/{get_climsoft_user.userName}")
    assert response.status_code == 200

    response = client.get(f"/climsoft/v1/climsoft-users/{get_climsoft_user.userName}")
    assert response.status_code == 404
