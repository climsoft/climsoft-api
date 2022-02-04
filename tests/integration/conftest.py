import pytest
from sqlalchemy import MetaData
from opencdms.models.climsoft.v4_1_1_core import Base
from climsoft_api.db import engine


@pytest.fixture(autouse=True)
def setup_db():
    metadata: MetaData = Base.metadata
    metadata.create_all(engine)
    yield
    metadata.drop_all(engine)
