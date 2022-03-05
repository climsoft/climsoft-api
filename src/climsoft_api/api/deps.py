from climsoft_api.db import SessionLocal
from sqlalchemy.orm.session import Session


async def get_session() -> Session:
    """
    Api dependency to provide database session to a request
    """
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
