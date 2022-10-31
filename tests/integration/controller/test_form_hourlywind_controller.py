import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_hourlywind import schema as form_hourlywind_schema
from tests.datagen import form_hourlywind as climsoft_form_hourlywind
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_hourlywind(session: Session):
    form_hourlywind = climsoft_models.FormHourlywind(**climsoft_form_hourlywind.get_valid_form_hourlywind_input().dict())
    session.add(form_hourlywind)
    session.commit()
    yield form_hourlywind


@pytest.fixture
def get_form_hourlywinds(session: Session):
    for _ in range(10):
        form_hourlywind = climsoft_models.FormHourlywind(**climsoft_form_hourlywind.get_valid_form_hourlywind_input().dict())
        session.add(form_hourlywind)
    session.commit()


def test_should_return_first_five_form_hourlywinds(client: TestClient, get_form_hourlywinds):
    response = client.get(
        "/climsoft/v1/form_hourlywinds",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_hourlywind(client: TestClient, get_form_hourlywind: climsoft_models.FormHourlywind):
    response = client.get(
        f"/climsoft/v1/form_hourlywinds/{get_form_hourlywind.stationId}/{get_form_hourlywind.yyyy}/{get_form_hourlywind.mm}/{get_form_hourlywind.dd}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_hourlywind(client: TestClient):
    form_hourlywind_data = climsoft_form_hourlywind.get_valid_form_hourlywind_input().dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/form_hourlywinds",
        data=json.dumps(form_hourlywind_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/form_hourlywinds",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_hourlywind(client: TestClient, get_form_hourlywind):
    form_hourlywind_data = form_hourlywind_schema.FormHourlyWind.from_orm(get_form_hourlywind).dict(by_alias=True)
    station_id = form_hourlywind_data.pop("station_id")
    yyyy = form_hourlywind_data.pop("yyyy")
    mm = form_hourlywind_data.pop("mm")
    dd = form_hourlywind_data.pop("dd")
    updates = {**form_hourlywind_data, "elem_111_01": "updated hh_01"}

    response = client.put(
        f"/climsoft/v1/form_hourlywinds/{station_id}/{yyyy}/{mm}/{dd}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["elem_111_01"] == updates["elem_111_01"]


def test_should_delete_form_hourlywind(client: TestClient, get_form_hourlywind):
    form_hourlywind_data = form_hourlywind_schema.FormHourlyWind.from_orm(get_form_hourlywind).dict(by_alias=True)
    station_id = form_hourlywind_data.pop("station_id")
    yyyy = form_hourlywind_data.pop("yyyy")
    mm = form_hourlywind_data.pop("mm")
    dd = form_hourlywind_data.pop("dd")

    response = client.delete(
        f"/climsoft/v1/form_hourlywinds/{station_id}/{yyyy}/{mm}/{dd}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/form_hourlywinds/{station_id}/{yyyy}/{mm}/{dd}",
    )
    assert response.status_code == 404
