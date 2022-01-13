from sqlalchemy.orm.session import Session
from climsoft_api.db import SessionLocal


def get_session():
    """
    Api dependency to provide database session to a request
    """
    session: Session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()
