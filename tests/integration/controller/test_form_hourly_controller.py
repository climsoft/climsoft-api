import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_hourly import schema as form_hourly_schema
from tests.datagen import form_hourly as climsoft_form_hourly
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_hourly(session: Session):
    form_hourly = climsoft_models.FormHourly(**climsoft_form_hourly.get_valid_form_hourly_input().dict())
    session.add(form_hourly)
    session.commit()
    yield form_hourly


@pytest.fixture
def get_form_hourlys(session: Session):
    for _ in range(10):
        form_hourly = climsoft_models.FormHourly(**climsoft_form_hourly.get_valid_form_hourly_input().dict())
        session.add(form_hourly)
    session.commit()


def test_should_return_first_five_form_hourlys(client: TestClient, get_form_hourlys):
    response = client.get(
        "/climsoft/v1/form_hourlys",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_hourly(client: TestClient, get_form_hourly: climsoft_models.FormHourly):
    response = client.get(
        f"/climsoft/v1/form_hourlys/{get_form_hourly.stationId}/{get_form_hourly.elementId}/{get_form_hourly.yyyy}/{get_form_hourly.mm}/{get_form_hourly.dd}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_hourly(client: TestClient):
    form_hourly_data = climsoft_form_hourly.get_valid_form_hourly_input().dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/form_hourlys",
        data=json.dumps(form_hourly_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/form_hourlys",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_hourly(client: TestClient, get_form_hourly):
    form_hourly_data = form_hourly_schema.FormHourly.from_orm(get_form_hourly).dict(by_alias=True)
    station_id = form_hourly_data.pop("station_id")
    element_id = form_hourly_data.pop("element_id")
    yyyy = form_hourly_data.pop("yyyy")
    mm = form_hourly_data.pop("mm")
    dd = form_hourly_data.pop("dd")
    updates = {**form_hourly_data, "hh_01": "updated hh_01"}

    response = client.put(
        f"/climsoft/v1/form_hourlys/{station_id}/{element_id}/{yyyy}/{mm}/{dd}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    print(response_data)

    assert response.status_code == 200
    assert response_data["result"][0]["hh_01"] == updates["hh_01"]


def test_should_delete_form_hourly(client: TestClient, get_form_hourly):
    form_hourly_data = form_hourly_schema.FormHourly.from_orm(get_form_hourly).dict(by_alias=True)
    station_id = form_hourly_data.pop("station_id")
    element_id = form_hourly_data.pop("element_id")
    yyyy = form_hourly_data.pop("yyyy")
    mm = form_hourly_data.pop("mm")
    dd = form_hourly_data.pop("dd")

    response = client.delete(
        f"/climsoft/v1/form_hourlys/{station_id}/{element_id}/{yyyy}/{mm}/{dd}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/form_hourlys/{station_id}/{element_id}/{yyyy}/{mm}/{dd}",
    )
    assert response.status_code == 404
