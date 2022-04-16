from sqlalchemy.orm.session import Session
from fastapi import Request


async def get_session(request: Request) -> Session:
    """
    Api dependency to provide database session to a request
    """
    return request.state.db
