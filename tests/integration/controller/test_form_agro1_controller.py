import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_agro1 import schema as form_agro1_schema
from tests.datagen import form_agro1 as climsoft_form_agro1
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_agro1(session: Session):
    form_agro1 = climsoft_models.FormAgro1(**climsoft_form_agro1.get_valid_form_agro1_input().dict())
    session.add(form_agro1)
    session.commit()
    yield form_agro1


@pytest.fixture
def get_form_agro1s(session: Session):
    for _ in range(10):
        form_agro1 = climsoft_models.FormAgro1(**climsoft_form_agro1.get_valid_form_agro1_input().dict())
        session.add(form_agro1)
    session.commit()


def test_should_return_first_five_form_agro1s(client: TestClient, get_form_agro1s):
    response = client.get(
        "/v1/form_agro1s",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_agro1(client: TestClient, get_form_agro1: climsoft_models.FormAgro1):
    response = client.get(
        f"/v1/form_agro1s/{get_form_agro1.stationId}/{get_form_agro1.yyyy}/{get_form_agro1.mm}/{get_form_agro1.dd}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_agro1(client: TestClient):
    form_agro1_data = climsoft_form_agro1.get_valid_form_agro1_input().dict(by_alias=True)
    response = client.post(
        "/v1/form_agro1s",
        data=json.dumps(form_agro1_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/v1/form_agro1s",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_agro1(client: TestClient, get_form_agro1):
    form_agro1_data = form_agro1_schema.FormAgro1.from_orm(get_form_agro1).dict(by_alias=True)
    station_id = form_agro1_data.pop("station_id")
    yyyy = form_agro1_data.pop("yyyy")
    mm = form_agro1_data.pop("mm")
    dd = form_agro1_data.pop("dd")
    updates = {**form_agro1_data, "flag513": "B"}

    response = client.put(
        f"/v1/form_agro1s/{station_id}/{yyyy}/{mm}/{dd}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["flag513"] == updates["flag513"]


def test_should_delete_form_agro1(client: TestClient, get_form_agro1):
    form_agro1_data = form_agro1_schema.FormAgro1.from_orm(get_form_agro1).dict(by_alias=True)
    station_id = form_agro1_data.pop("station_id")
    yyyy = form_agro1_data.pop("yyyy")
    mm = form_agro1_data.pop("mm")
    dd = form_agro1_data.pop("dd")

    response = client.delete(
        f"/v1/form_agro1s/{station_id}/{yyyy}/{mm}/{dd}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/form_agro1s/{station_id}/{yyyy}/{mm}/{dd}",
    )
    assert response.status_code == 404
