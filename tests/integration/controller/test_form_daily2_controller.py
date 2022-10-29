import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_daily2 import schema as form_daily2_schema
from tests.datagen import form_daily2 as climsoft_form_daily2
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_daily2(session: Session):
    form_daily2 = climsoft_models.FormDaily2(**climsoft_form_daily2.get_valid_form_daily2_input().dict())
    session.add(form_daily2)
    session.commit()
    yield form_daily2


@pytest.fixture
def get_form_daily2s(session: Session):
    for _ in range(10):
        form_daily2 = climsoft_models.FormDaily2(**climsoft_form_daily2.get_valid_form_daily2_input().dict())
        session.add(form_daily2)
    session.commit()


def test_should_return_first_five_form_daily2s(client: TestClient, get_form_daily2s):
    response = client.get(
        "/climsoft/v1/form_daily2s",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_daily2(client: TestClient, get_form_daily2: climsoft_models.FormDaily2):
    response = client.get(
        f"/climsoft/v1/form_daily2s/{get_form_daily2.stationId}/{get_form_daily2.elementId}/{get_form_daily2.yyyy}/{get_form_daily2.mm}/{get_form_daily2.hh}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_daily2(client: TestClient):
    form_daily2_data = climsoft_form_daily2.get_valid_form_daily2_input().dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/form_daily2s",
        data=json.dumps(form_daily2_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/form_daily2s",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_daily2(client: TestClient, get_form_daily2):
    form_daily2_data = form_daily2_schema.FormDaily2.from_orm(get_form_daily2).dict(by_alias=True)
    station_id = form_daily2_data.pop("station_id")
    element_id = form_daily2_data.pop("element_id")
    yyyy = form_daily2_data.pop("yyyy")
    mm = form_daily2_data.pop("mm")
    hh = form_daily2_data.pop("hh")
    updates = {**form_daily2_data, "day02": "updated day02"}

    response = client.put(
        f"/climsoft/v1/form_daily2s/{station_id}/{element_id}/{yyyy}/{mm}/{hh}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["day02"] == updates["day02"]


def test_should_delete_form_daily2(client: TestClient, get_form_daily2):
    form_daily2_data = form_daily2_schema.FormDaily2.from_orm(get_form_daily2).dict(by_alias=True)
    station_id = form_daily2_data.pop("station_id")
    element_id = form_daily2_data.pop("element_id")
    yyyy = form_daily2_data.pop("yyyy")
    mm = form_daily2_data.pop("mm")
    hh = form_daily2_data.pop("hh")

    response = client.delete(
        f"/climsoft/v1/form_daily2s/{station_id}/{element_id}/{yyyy}/{mm}/{hh}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/form_daily2s/{station_id}/{element_id}/{yyyy}/{mm}/{hh}",
    )
    assert response.status_code == 404
