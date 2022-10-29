import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_synoptic_2_ra1 import schema as form_synoptic_2_ra1_schema
from tests.datagen import form_synoptic_2_ra1 as climsoft_form_synoptic_2_ra1
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_synoptic_2_ra1(session: Session):
    form_synoptic_2_ra1 = climsoft_models.FormSynoptic2Ra1(**climsoft_form_synoptic_2_ra1.get_valid_form_synoptic_2_ra1_input().dict())
    session.add(form_synoptic_2_ra1)
    session.commit()
    yield form_synoptic_2_ra1


@pytest.fixture
def get_form_synoptic_2_ra1s(session: Session):
    for _ in range(10):
        form_synoptic_2_ra1 = climsoft_models.FormSynoptic2Ra1(**climsoft_form_synoptic_2_ra1.get_valid_form_synoptic_2_ra1_input().dict())
        session.add(form_synoptic_2_ra1)
    session.commit()


def test_should_return_first_five_form_synoptic_2_ra1s(client: TestClient, get_form_synoptic_2_ra1s):
    response = client.get(
        "/climsoft/v1/form_synoptic_2_ra1s",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_synoptic_2_ra1(client: TestClient, get_form_synoptic_2_ra1: climsoft_models.FormSynoptic2Ra1):
    response = client.get(
        f"/climsoft/v1/form_synoptic_2_ra1s/{get_form_synoptic_2_ra1.stationId}/{get_form_synoptic_2_ra1.yyyy}/{get_form_synoptic_2_ra1.mm}/{get_form_synoptic_2_ra1.dd}/{get_form_synoptic_2_ra1.hh}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_synoptic_2_ra1(client: TestClient):
    form_synoptic_2_ra1_data = climsoft_form_synoptic_2_ra1.get_valid_form_synoptic_2_ra1_input().dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/form_synoptic_2_ra1s",
        data=json.dumps(form_synoptic_2_ra1_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/form_synoptic_2_ra1s",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_synoptic_2_ra1(client: TestClient, get_form_synoptic_2_ra1):
    form_synoptic_2_ra1_data = form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(get_form_synoptic_2_ra1).dict(by_alias=True)
    station_id = form_synoptic_2_ra1_data.pop("station_id")
    yyyy = form_synoptic_2_ra1_data.pop("yyyy")
    mm = form_synoptic_2_ra1_data.pop("mm")
    dd = form_synoptic_2_ra1_data.pop("dd")
    hh = form_synoptic_2_ra1_data.pop("hh")
    updates = {**form_synoptic_2_ra1_data, "flag301": "B"}

    response = client.put(
        f"/climsoft/v1/form_synoptic_2_ra1s/{station_id}/{yyyy}/{mm}/{dd}/{hh}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()
    print(response_data)
    assert response.status_code == 200
    assert response_data["result"][0]["flag301"] == updates["flag301"]


def test_should_delete_form_synoptic_2_ra1(client: TestClient, get_form_synoptic_2_ra1):
    form_synoptic_2_ra1_data = form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(get_form_synoptic_2_ra1).dict(by_alias=True)
    station_id = form_synoptic_2_ra1_data.pop("station_id")
    yyyy = form_synoptic_2_ra1_data.pop("yyyy")
    mm = form_synoptic_2_ra1_data.pop("mm")
    dd = form_synoptic_2_ra1_data.pop("dd")
    hh = form_synoptic_2_ra1_data.pop("hh")

    response = client.delete(
        f"/climsoft/v1/form_synoptic_2_ra1s/{station_id}/{yyyy}/{mm}/{dd}/{hh}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/form_synoptic_2_ra1s/{station_id}/{yyyy}/{mm}/{dd}/{hh}",
    )
    print(response.json())
    assert response.status_code == 404
