import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.flag import schema as flag_schema
from tests.datagen import flag as climsoft_flag
from fastapi.testclient import TestClient


@pytest.fixture
def get_flag(session: Session):
    flag = climsoft_models.Flag(**climsoft_flag.get_valid_flag_input().dict())
    session.add(flag)
    session.commit()
    yield flag


@pytest.fixture
def get_flags(session: Session):
    for _ in range(10):
        flag = climsoft_models.Flag(**climsoft_flag.get_valid_flag_input().dict())
        session.add(flag)
    session.commit()


def test_should_return_first_five_flags(client: TestClient, get_flags):
    response = client.get(
        "/v1/flags",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_flag(client: TestClient, get_flag: climsoft_models.Flag):
    response = client.get(
        f"/v1/flags/{get_flag.characterSymbol}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_flag(client: TestClient):
    flag_data = climsoft_flag.get_valid_flag_input().dict(by_alias=True)
    response = client.post(
        "/v1/flags",
        data=json.dumps(flag_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/v1/flags",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_flag(client: TestClient, get_flag):
    flag_data = flag_schema.Flag.from_orm(get_flag).dict(by_alias=True)
    character_symbol = flag_data.pop("character_symbol")
    updates = {**flag_data, "description": "updated name"}

    response = client.put(
        f"/v1/flags/{character_symbol}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_flag(client: TestClient, get_flag):
    flag_data = flag_schema.Flag.from_orm(get_flag).dict(by_alias=True)
    character_symbol = flag_data.pop("character_symbol")

    response = client.delete(
        f"/v1/flags/{character_symbol}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/flags/{character_symbol}",
    )
    assert response.status_code == 404
