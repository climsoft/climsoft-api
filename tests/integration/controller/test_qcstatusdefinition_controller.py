import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.qcstatusdefinition import schema as qcstatusdefinition_schema
from tests.datagen import qcstatusdefinition as climsoft_qcstatusdefinition
from fastapi.testclient import TestClient


@pytest.fixture
def get_qc_status_definition(session: Session):
    qc_status_definition = climsoft_models.Qcstatusdefinition(
        **climsoft_qcstatusdefinition.get_valid_qc_status_definition_input().dict()
    )
    session.add(qc_status_definition)
    session.commit()
    yield qc_status_definition
    session.close()


@pytest.fixture
def get_qc_status_definitions(session: Session):
    for _ in range(1, 11):
        session.add(
            climsoft_models.Qcstatusdefinition(
                **climsoft_qcstatusdefinition.get_valid_qc_status_definition_input().dict()
            )
        )
    session.commit()


def test_should_return_first_five_qc_status_definitions(
    client: TestClient, get_qc_status_definitions
):
    response = client.get(
        "/test/climsoft/v1/qc-status-definitions",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_qc_status_definition(
    client: TestClient,
    get_qc_status_definition: climsoft_models.Qcstatusdefinition,
):
    response = client.get(
        f"/test/climsoft/v1/qc-status-definitions/{get_qc_status_definition.code}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_qc_status_definition(
    client: TestClient,
):
    qc_status_definition_data = (
        climsoft_qcstatusdefinition.get_valid_qc_status_definition_input().dict(
            by_alias=True
        )
    )
    response = client.post(
        "/test/climsoft/v1/qc-status-definitions",
        data=json.dumps(qc_status_definition_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(
    client: TestClient,
):
    qc_status_definition_data = {"aaa": "bbbbbbb"}
    response = client.post(
        "/test/climsoft/v1/qc-status-definitions",
        data=json.dumps(qc_status_definition_data, default=str),
    )
    assert response.status_code == 422


def test_should_update_qc_status_definition(
    client: TestClient,
    get_qc_status_definition,
):
    qc_status_definition_data = qcstatusdefinition_schema.QCStatusDefinition.from_orm(
        get_qc_status_definition
    ).dict(by_alias=True)
    code = qc_status_definition_data.pop("code")
    updates = {**qc_status_definition_data, "description": "updated name"}

    response = client.put(
        f"/test/climsoft/v1/qc-status-definitions/{code}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_qc_status_definition(
    client: TestClient,
    get_qc_status_definition,
):
    qc_status_definition_data = qcstatusdefinition_schema.QCStatusDefinition.from_orm(
        get_qc_status_definition
    ).dict(by_alias=True)
    code = qc_status_definition_data.pop("code")

    response = client.delete(
        f"/test/climsoft/v1/qc-status-definitions/{code}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/test/climsoft/v1/qc-status-definitions/{code}",
    )
    assert response.status_code == 404
