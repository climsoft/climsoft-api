import time

import pytest
from sqlalchemy import MetaData, text
from opencdms.models.climsoft.v4_1_1_core import Base, TARGET_TABLES
from climsoft_api.db import engine


@pytest.fixture(scope="session", autouse=True)
def setup_db():
    for table in TARGET_TABLES:
        engine.execute(text(f"""
            SET FOREIGN_KEY_CHECKS=0;
            DROP TABLE IF EXISTS {table};
            SET FOREIGN_KEY_CHECKS=1;
        """))

    metadata: MetaData = Base.metadata
    metadata.create_all(engine)

    yield

    for table in TARGET_TABLES:
        engine.execute(text(f"""
            SET FOREIGN_KEY_CHECKS=0;
            DROP TABLE IF EXISTS {table};
            SET FOREIGN_KEY_CHECKS=1;
        """))
