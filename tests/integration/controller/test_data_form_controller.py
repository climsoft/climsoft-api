import json
import random

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from tests.datagen import data_form as climsoft_data_form
from climsoft_api.api.data_form import schema as data_form_schema
from fastapi.testclient import TestClient


@pytest.fixture
def get_data_form(session: Session):
    data_form = climsoft_models.DataForm(
        **climsoft_data_form.get_valid_data_form_input().dict()
    )
    session.add(data_form)
    session.commit()
    yield data_form
    session.close()


@pytest.fixture
def get_data_forms(session: Session):
    for i in range(10):
        form_id = random.randint(1000, 10000000)
        data_form = climsoft_models.DataForm(
            id=form_id,
            order_num=f"order{form_id}",
            table_name="table",
            form_name=f"form {form_id}",
            description="description",
            selected=True,
            elem_code_location="location",
            sequencer="sequencer",
        )
        session.add(data_form)
    session.commit()


def test_should_return_first_five_data_forms(
    client: TestClient, session: Session, get_data_forms
):
    response = client.get(
        "/v1/data-forms",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, data_form_schema.DataForm)


def test_should_return_single_data_form(
    client: TestClient, get_data_form: climsoft_models.DataForm
):
    response = client.get(
        f"/v1/data-forms/{get_data_form.form_name}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, data_form_schema.DataForm)


def test_should_create_a_data_form(client: TestClient):
    data_form_data = climsoft_data_form.get_valid_data_form_input().dict(by_alias=True)
    response = client.post(
        "/v1/data-forms",
        data=json.dumps(data_form_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, data_form_schema.DataForm)


def test_should_raise_validation_error(client: TestClient):
    data_form_data = (
        climsoft_data_form.get_valid_data_form_input().dict().pop("form_name")
    )
    response = client.post(
        "/v1/data-forms",
        data=json.dumps(data_form_data, default=str),
    )
    assert response.status_code == 422


def test_should_update_data_form(client: TestClient, get_data_form):
    data_form_data = data_form_schema.DataForm.from_orm(get_data_form).dict()
    form_name = data_form_data.pop("form_name")
    updates = {**data_form_data, "table_name": "updated name"}

    response = client.put(
        f"/v1/data-forms/{form_name}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["table_name"] == updates["table_name"]


def test_should_delete_data_form(client: TestClient, get_data_form):
    data_form_data = data_form_schema.DataForm.from_orm(get_data_form).dict()
    form_name = data_form_data.pop("form_name")

    response = client.delete(
        f"/v1/data-forms/{form_name}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/data-forms/{form_name}",
    )
    assert response.status_code == 404
