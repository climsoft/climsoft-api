from opencdms.models.climsoft.v4_1_1_core import Base
from climsoft_api.db import engine


Base.metadata.create_all(engine)
