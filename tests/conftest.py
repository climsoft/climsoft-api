from fastapi.applications import FastAPI
import pytest
from sqlalchemy.orm.session import Session
from climsoft_api.db import SessionLocal
from climsoft_api.main import get_app
from fastapi.testclient import TestClient


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
