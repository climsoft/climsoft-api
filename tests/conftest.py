from fastapi.applications import FastAPI
import pytest

from sqlalchemy.orm.session import Session
from sqlalchemy import MetaData
from climsoft_api.db import SessionLocal
from climsoft_api.main import get_app
from fastapi.testclient import TestClient
from opencdms.models.climsoft.v4_1_1_core import Base
from climsoft_api.db import engine


@pytest.fixture(autouse=True)
def setup_db():
    metadata: MetaData = Base.metadata
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)


@pytest.fixture
def app() -> FastAPI:
    return get_app()


@pytest.fixture
def client(app: FastAPI) -> TestClient:
    return TestClient(app)


@pytest.fixture
def session() -> Session:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
