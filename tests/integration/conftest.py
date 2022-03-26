import pytest
from sqlalchemy import MetaData, text
from opencdms.models.climsoft.v4_1_1_core import Base
from climsoft_api.db import engine


@pytest.fixture(scope="function", autouse=True)
def setup_db():
    engine.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
    engine.execute(text(f"""
        SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
        FROM information_schema.tables
        WHERE table_schema = '{engine.url.database}';
    """))
    engine.execute(text("SET FOREIGN_KEY_CHECKS=1;"))

    metadata: MetaData = Base.metadata
    metadata.create_all(engine)

    yield

    engine.execute(text("SET FOREIGN_KEY_CHECKS=0;"))
    engine.execute(text(f"""
        SELECT concat('DROP TABLE IF EXISTS `', table_name, '`;')
        FROM information_schema.tables
        WHERE table_schema = '{engine.url.database}';
    """))
    engine.execute(text("SET FOREIGN_KEY_CHECKS=1;"))
