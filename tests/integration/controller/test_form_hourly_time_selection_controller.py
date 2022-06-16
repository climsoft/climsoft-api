import json
import random

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_hourly_time_selection import schema as form_hourly_time_selection_schema
from tests.datagen import form_hourly_time_selection as climsoft_form_hourly_time_selection
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_hourly_time_selection(session: Session):
    form_hourly_time_selection = climsoft_models.FormHourlyTimeSelection(**climsoft_form_hourly_time_selection.get_valid_form_hourly_time_selection_input().dict())
    session.add(form_hourly_time_selection)
    session.commit()
    yield form_hourly_time_selection


@pytest.fixture
def get_form_hourly_time_selections(session: Session):
    for _ in range(10):
        form_hourly_time_selection = climsoft_models.FormHourlyTimeSelection(**climsoft_form_hourly_time_selection.get_valid_form_hourly_time_selection_input().dict())
        session.add(form_hourly_time_selection)
    session.commit()


def test_should_return_first_five_form_hourly_time_selections(client: TestClient, get_form_hourly_time_selections):
    response = client.get(
        "/v1/form_hourly_time_selections",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_hourly_time_selection(client: TestClient, get_form_hourly_time_selection: climsoft_models.FormHourlyTimeSelection):
    response = client.get(
        f"/v1/form_hourly_time_selections/{get_form_hourly_time_selection.stationId}/{get_form_hourly_time_selection.elementId}/{get_form_hourly_time_selection.yyyy}/{get_form_hourly_time_selection.mm}/{get_form_hourly_time_selection.dd}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_hourly_time_selection(client: TestClient):
    form_hourly_time_selection_data = climsoft_form_hourly_time_selection.get_valid_form_hourly_time_selection_input().dict(by_alias=True)
    response = client.post(
        "/v1/form_hourly_time_selections",
        data=json.dumps(form_hourly_time_selection_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/v1/form_hourly_time_selections",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_hourly_time_selection(client: TestClient, get_form_hourly_time_selection):
    form_hourly_time_selection_data = form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(get_form_hourly_time_selection).dict(by_alias=True)
    hh = form_hourly_time_selection_data.pop("hh")
    updates = {**form_hourly_time_selection_data, "hh": random.randint(10, 20)}

    response = client.put(
        f"/v1/form_hourly_time_selections/{hh}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    print(response_data)

    assert response.status_code == 200
    assert response_data["result"][0]["hh"] == updates["hh"]


def test_should_delete_form_hourly_time_selection(client: TestClient, get_form_hourly_time_selection):
    form_hourly_time_selection_data = form_hourly_time_selection_schema.FormHourlyTimeSelection.from_orm(get_form_hourly_time_selection).dict(by_alias=True)
    hh = form_hourly_time_selection_data.pop("hh")

    response = client.delete(
        f"/v1/form_hourly_time_selections/{hh}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/form_hourly_time_selections/{hh}",
    )
    assert response.status_code == 404
