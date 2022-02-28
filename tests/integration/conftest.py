import pytest
from sqlalchemy import MetaData, text
from opencdms.models.climsoft.v4_1_1_core import Base
from climsoft_api.db import engine


@pytest.fixture(autouse=True)
def setup_db():
    metadata: MetaData = Base.metadata
    metadata.create_all(engine)
    yield
    engine.execute(text("SET foreign_key_checks = 0;"))
    metadata.drop_all(engine)
    engine.execute(text("SET foreign_key_checks = 1;"))
