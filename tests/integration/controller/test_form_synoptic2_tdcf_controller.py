import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.form_synoptic2_tdcf import schema as form_synoptic2_tdcf_schema
from tests.datagen import form_synoptic2_tdcf as climsoft_form_synoptic2_tdcf
from fastapi.testclient import TestClient


@pytest.fixture
def get_form_synoptic2_tdcf(session: Session):
    form_synoptic2_tdcf = climsoft_models.FormSynoptic2Tdcf(**climsoft_form_synoptic2_tdcf.get_valid_form_synoptic2_tdcf_input().dict())
    session.add(form_synoptic2_tdcf)
    session.commit()
    yield form_synoptic2_tdcf


@pytest.fixture
def get_form_synoptic2_tdcfs(session: Session):
    for _ in range(10):
        form_synoptic2_tdcf = climsoft_models.FormSynoptic2Tdcf(**climsoft_form_synoptic2_tdcf.get_valid_form_synoptic2_tdcf_input().dict())
        session.add(form_synoptic2_tdcf)
    session.commit()


def test_should_return_first_five_form_synoptic2_tdcfs(client: TestClient, get_form_synoptic2_tdcfs):
    response = client.get(
        "/climsoft/v1/form_synoptic2_tdcfs",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_form_synoptic2_tdcf(client: TestClient, get_form_synoptic2_tdcf: climsoft_models.FormSynoptic2Tdcf):
    response = client.get(
        f"/climsoft/v1/form_synoptic2_tdcfs/{get_form_synoptic2_tdcf.stationId}/{get_form_synoptic2_tdcf.yyyy}/{get_form_synoptic2_tdcf.mm}/{get_form_synoptic2_tdcf.dd}/{get_form_synoptic2_tdcf.hh}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_form_synoptic2_tdcf(client: TestClient):
    form_synoptic2_tdcf_data = climsoft_form_synoptic2_tdcf.get_valid_form_synoptic2_tdcf_input().dict(by_alias=True)
    response = client.post(
        "/climsoft/v1/form_synoptic2_tdcfs",
        data=json.dumps(form_synoptic2_tdcf_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    response = client.post(
        "/climsoft/v1/form_synoptic2_tdcfs",
        data=json.dumps({"num_symbol": 3}, default=str),
    )
    assert response.status_code == 422


def test_should_update_form_synoptic2_tdcf(client: TestClient, get_form_synoptic2_tdcf):
    form_synoptic2_tdcf_data = form_synoptic2_tdcf_schema.FormSynoptic2Tdcf.from_orm(get_form_synoptic2_tdcf).dict(by_alias=True)
    station_id = form_synoptic2_tdcf_data.pop("station_id")
    yyyy = form_synoptic2_tdcf_data.pop("yyyy")
    mm = form_synoptic2_tdcf_data.pop("mm")
    dd = form_synoptic2_tdcf_data.pop("dd")
    hh = form_synoptic2_tdcf_data.pop("hh")
    updates = {**form_synoptic2_tdcf_data, "flag1": "B"}

    response = client.put(
        f"/climsoft/v1/form_synoptic2_tdcfs/{station_id}/{yyyy}/{mm}/{dd}/{hh}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()
    assert response.status_code == 200
    assert response_data["result"][0]["flag1"] == updates["flag1"]


def test_should_delete_form_synoptic2_tdcf(client: TestClient, get_form_synoptic2_tdcf):
    form_synoptic2_tdcf_data = form_synoptic2_tdcf_schema.FormSynoptic2Tdcf.from_orm(get_form_synoptic2_tdcf).dict(by_alias=True)
    station_id = form_synoptic2_tdcf_data.pop("station_id")
    yyyy = form_synoptic2_tdcf_data.pop("yyyy")
    mm = form_synoptic2_tdcf_data.pop("mm")
    dd = form_synoptic2_tdcf_data.pop("dd")
    hh = form_synoptic2_tdcf_data.pop("hh")

    response = client.delete(
        f"/climsoft/v1/form_synoptic2_tdcfs/{station_id}/{yyyy}/{mm}/{dd}/{hh}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/climsoft/v1/form_synoptic2_tdcfs/{station_id}/{yyyy}/{mm}/{dd}/{hh}",
    )
    assert response.status_code == 404
