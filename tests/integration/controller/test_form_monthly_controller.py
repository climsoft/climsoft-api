import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_monthly import schema as form_monthly_schema
from tests.datagen import form_monthly as climsoft_form_monthly
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_monthly(session: Session):
    form_monthly = climsoft_models.FormMonthly(**climsoft_form_monthly.get_valid_form_monthly_input().dict())
    session.add(form_monthly)
    session.commit()
    yield form_monthly


@pytest.fixture
def get_form_monthlys(session: Session):
    for _ in range(10):
        form_monthly = climsoft_models.FormMonthly(**climsoft_form_monthly.get_valid_form_monthly_input().dict())
        session.add(form_monthly)
    session.commit()


def test_should_return_first_five_form_monthlys(client: TestClient, get_form_monthlys):
    response = client.get(
        "/climsoft/v1/form_monthlys",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_monthly(client: TestClient, get_form_monthly: climsoft_models.FormMonthly):
    response = client.get(
        f"/climsoft/v1/form_monthlys/{get_form_monthly.stationId}/{get_form_monthly.elementId}/{get_form_monthly.yyyy}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_monthly(client: TestClient):
    form_monthly_data = climsoft_form_monthly.get_valid_form_monthly_input().dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/form_monthlys",
        data=json.dumps(form_monthly_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/form_monthlys",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_monthly(client: TestClient, get_form_monthly):
    form_monthly_data = form_monthly_schema.FormMonthly.from_orm(get_form_monthly).dict(by_alias=True)
    station_id = form_monthly_data.pop("station_id")
    element_id = form_monthly_data.pop("element_id")
    yyyy = form_monthly_data.pop("yyyy")
    updates = {**form_monthly_data, "mm_02": "updated mm_02"}

    response = client.put(
        f"/climsoft/v1/form_monthlys/{station_id}/{element_id}/{yyyy}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()
    print(response_data)
    assert response.status_code == 200
    assert response_data["result"][0]["mm_02"] == updates["mm_02"]


def test_should_delete_form_monthly(client: TestClient, get_form_monthly):
    form_monthly_data = form_monthly_schema.FormMonthly.from_orm(get_form_monthly).dict(by_alias=True)
    station_id = form_monthly_data.pop("station_id")
    element_id = form_monthly_data.pop("element_id")
    yyyy = form_monthly_data.pop("yyyy")

    response = client.delete(
        f"/climsoft/v1/form_monthlys/{station_id}/{element_id}/{yyyy}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/form_monthlys/{station_id}/{element_id}/{yyyy}",
    )
    assert response.status_code == 404
