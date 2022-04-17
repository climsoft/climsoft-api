from sqlalchemy.orm.session import Session
from fastapi import Request


async def get_session(request: Request) -> Session:
    """
    Api dependency to provide database session to a request
    """
    try:
        request.state.db = request.state.get_session()
        yield request.state.db
    finally:
        request.state.db.close()
