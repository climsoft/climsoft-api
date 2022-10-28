from datetime import datetime
import json
import uuid

import pytest
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.api.paperarchive import schema as paperarchive_schema
from tests.datagen import (
    paperarchive as climsoft_paper_archive,
    paperarchivedefinition as climsoft_paper_archive_definition,
    station as climsoft_station,
)
from fastapi.testclient import TestClient


@pytest.fixture
def get_station(session: Session):
    station = climsoft_models.Station(
        **climsoft_station.get_valid_station_input().dict()
    )
    session.add(station)
    session.commit()
    yield station
    session.close()


@pytest.fixture
def get_paper_archive_definition(session: Session):
    paper_archive_definition = climsoft_models.Paperarchivedefinition(
        **climsoft_paper_archive_definition.get_valid_paper_archive_definition_input().dict()
    )
    session.add(paper_archive_definition)
    session.commit()
    yield paper_archive_definition
    session.close()


@pytest.fixture
def get_paper_archive(session: Session):
    station = climsoft_models.Station(
        **climsoft_station.get_valid_station_input().dict()
    )
    session.add(station)
    session.flush()

    paper_archive_definition = climsoft_models.Paperarchivedefinition(
        **climsoft_paper_archive_definition.get_valid_paper_archive_definition_input().dict()
    )
    session.add(paper_archive_definition)
    session.flush()
    paper_archive_data = climsoft_paper_archive.get_valid_paper_archive_input(
        station_id=station.stationId,
        paper_archive_definition_id=paper_archive_definition.formId,
    ).dict()
    paper_archive = climsoft_models.Paperarchive(**paper_archive_data)
    session.add(paper_archive)
    session.commit()
    yield paper_archive


@pytest.fixture
def get_paper_archives(session: Session):
    for _ in range(1, 11):
        station = climsoft_models.Station(
            **climsoft_station.get_valid_station_input().dict()
        )
        session.add(station)
        session.flush()

        paper_archive_definition = climsoft_models.Paperarchivedefinition(
            **climsoft_paper_archive_definition.get_valid_paper_archive_definition_input().dict()
        )
        session.add(paper_archive_definition)
        session.flush()

        session.add(
            climsoft_models.Paperarchive(
                **climsoft_paper_archive.get_valid_paper_archive_input(
                    station_id=station.stationId,
                    paper_archive_definition_id=paper_archive_definition.formId,
                ).dict()
            )
        )
    session.commit()


def test_should_return_first_five_paper_archives(
    client: TestClient, get_paper_archives
):
    response = client.get(
        "/test/climsoft/v1/paper-archives",
        params={"limit": 5},
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 5
    for s in response_data["result"]:
        isinstance(s, paperarchive_schema.PaperArchive)


def test_should_return_single_paper_archive(
    client: TestClient,
    get_paper_archive: climsoft_models.Paperarchive,
):
    response = client.get(
        f"/test/climsoft/v1/paper-archives/{get_paper_archive.belongsTo}/{get_paper_archive.formDatetime}/{get_paper_archive.classifiedInto}",
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, paperarchive_schema.PaperArchive)


def test_should_create_a_paper_archive(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_paper_archive_definition: climsoft_models.Paperarchivedefinition,
):
    paper_archive_data = climsoft_paper_archive.get_valid_paper_archive_input(
        station_id=get_station.stationId,
        paper_archive_definition_id=get_paper_archive_definition.formId,
    ).dict(by_alias=True)
    response = client.post(
        "/test/climsoft/v1/paper-archives",
        data=json.dumps(paper_archive_data, default=str),
    )
    assert response.status_code == 200
    response_data = response.json()
    assert len(response_data["result"]) == 1
    for s in response_data["result"]:
        isinstance(s, paperarchive_schema.PaperArchive)


def test_should_raise_validation_error(
    client: TestClient,
    get_station: climsoft_models.Station,
    get_paper_archive_definition: climsoft_models.Paperarchivedefinition,
):
    response = client.post(
        "/test/climsoft/v1/paper-archives",
        data=json.dumps({"form_datetime": datetime.utcnow()}, default=str),
    )
    assert response.status_code == 422


def test_should_update_paper_archive(
    client: TestClient,
    get_paper_archive: climsoft_models.Paperarchive,
):
    updates = {"image": uuid.uuid4().hex}

    response = client.put(
        f"/test/climsoft/v1/paper-archives/{get_paper_archive.belongsTo}/{get_paper_archive.formDatetime}/{get_paper_archive.classifiedInto}",
        data=json.dumps(updates, default=str),
    )
    response_data = response.json()

    assert response.status_code == 200
    assert response_data["result"][0]["image"] == updates["image"]


def test_should_delete_paper_archive(
    client: TestClient,
    get_paper_archive: climsoft_models.Paperarchive,
):
    response = client.delete(
        f"/test/climsoft/v1/paper-archives/{get_paper_archive.belongsTo}/{get_paper_archive.formDatetime}/{get_paper_archive.classifiedInto}",
    )

    assert response.status_code == 200

    response = client.get(
        f"/test/climsoft/v1/paper-archives/{get_paper_archive.belongsTo}/{get_paper_archive.formDatetime}/{get_paper_archive.classifiedInto}",
    )
    assert response.status_code == 404
