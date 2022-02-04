import json
import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.paperarchivedefinition import (
    schema as paperarchivedefinition_schema,
)
from tests.datagen import paperarchivedefinition as climsoft_paperarchivedefinition
from fastapi.testclient import TestClient


@pytest.fixture
def get_paper_archive_definition(session: Session):
    paper_archive_definition = climsoft_models.Paperarchivedefinition(
        **climsoft_paperarchivedefinition.get_valid_paper_archive_definition_input().dict()
    )
    session.add(paper_archive_definition)
    session.commit()
    yield paper_archive_definition
    session.close()


@pytest.fixture
def get_paper_archive_definitions(session: Session):
    for _ in range(1, 11):
        session.add(
            climsoft_models.Paperarchivedefinition(
                **climsoft_paperarchivedefinition.get_valid_paper_archive_definition_input().dict()
            )
        )
    session.commit()


def test_should_return_first_five_paper_archive_definitions(
    client: TestClient, get_paper_archive_definitions
):
    response = client.get(
        "/v1/paper-archive-definitions/",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5


def test_should_return_single_paper_archive_definition(
    client: TestClient,
    get_paper_archive_definition: climsoft_models.Paperarchivedefinition,
):
    response = client.get(
        f"/v1/paper-archive-definitions/{get_paper_archive_definition.formId}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_create_a_paper_archive_definition(client: TestClient):
    paper_archive_definition_data = (
        climsoft_paperarchivedefinition.get_valid_paper_archive_definition_input().dict(
            by_alias=True
        )
    )
    response = client.post(
        "/v1/paper-archive-definitions/",
        data=json.dumps(paper_archive_definition_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1


def test_should_raise_validation_error(client: TestClient):
    paper_archive_definition_data = {"form_id": "bbbbbbb"}
    response = client.post(
        "/v1/paper-archive-definitions/",
        data=json.dumps(paper_archive_definition_data, default=str),
    )
    assert response.status_code == 422


def test_should_update_paper_archive_definition(
    client: TestClient, get_paper_archive_definition
):
    paper_archive_definition_data = (
        paperarchivedefinition_schema.PaperArchiveDefinition.from_orm(
            get_paper_archive_definition
        ).dict(by_alias=True)
    )
    form_id = paper_archive_definition_data.pop("form_id")
    updates = {**paper_archive_definition_data, "description": "updated name"}

    response = client.put(
        f"/v1/paper-archive-definitions/{form_id}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["description"] == updates["description"]


def test_should_delete_paper_archive_definition(
    client: TestClient, get_paper_archive_definition
):
    paper_archive_definition_data = (
        paperarchivedefinition_schema.PaperArchiveDefinition.from_orm(
            get_paper_archive_definition
        ).dict(by_alias=True)
    )
    form_id = paper_archive_definition_data.pop("form_id")

    response = client.delete(
        f"/v1/paper-archive-definitions/{form_id}",
    )
    assert response.status_code == 200

    response = client.get(
        f"/v1/paper-archive-definitions/{form_id}",
    )
    assert response.status_code == 404
