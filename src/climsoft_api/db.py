from climsoft_api.config import settings
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from climsoft_api.utils.deployment import load_deployment_configs


engine: Engine = create_engine(settings.DATABASE_URI)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_engine(deployment_key):
    deployment_configs = load_deployment_configs()
    if deployment_key and deployment_configs[deployment_key].get("DATABASE_URI"):
        return create_engine(deployment_configs[deployment_key].get("DATABASE_URI"))
    else:
        return create_engine(settings.DATABASE_URI)


def get_session_local(deployment_key: str = None):
    return sessionmaker(get_engine(deployment_key))


def get_session(deployment_key: str = None):
    """
    Api dependency to provide climsoft database session to a request
    """
    return get_session_local(deployment_key)()
