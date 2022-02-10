from climsoft_api.config import settings
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base


engine: Engine = create_engine(settings.DATABASE_URI)


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()
