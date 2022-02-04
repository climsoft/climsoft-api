import os
import pytest

#
# @pytest.fixture(autouse=True)
# def setup_environment():
#     snapshot_db_uri = os.getenv(
#         "CLIMSOFT_SNAPSHOT_DB_URI",
#         "mysql+mysqldb://root:password@127.0.0.1/mariadb_climsoft_db_v4"
#     )
#     os.environ["CLIMSOFT_DATABASE_URI"] = snapshot_db_uri
#
