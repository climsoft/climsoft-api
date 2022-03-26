import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.climsoftuser import schema as climsoftuser_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftUserService")
logging.basicConfig(level=logging.INFO)


def get_or_404(db_session: Session, username: str):
    user = db_session.query(models.ClimsoftUser).filter_by(
        userName=username
    ).first()
    if not user:
        HTTPException(status_code=404, detail=_("Climsoft user not found."))
    return user


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: climsoftuser_schema.CreateClimsoftUser
) -> climsoftuser_schema.ClimsoftUser:
    climsoft_user = models.ClimsoftUser(**data.dict())
    db_session.add(climsoft_user)
    db_session.commit()
    return climsoftuser_schema.ClimsoftUser.from_orm(climsoft_user)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(db_session: Session, username: str) -> climsoftuser_schema.ClimsoftUser:
    climsoft_user = get_or_404(db_session, username)

    return climsoftuser_schema.ClimsoftUser.from_orm(climsoft_user)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    username: str = None,
    role: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[climsoftuser_schema.ClimsoftUser]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `obselement` row skipping
    `offset` number of rows
    :param db_session:
    :param username:
    :param role:
    :param limit:
    :param offset:
    :return:
    """
    q = db_session.query(models.ClimsoftUser)

    if username is not None:
        q = q.filter(models.ClimsoftUser.userName.ilike(f"%{username}%"))

    if role is not None:
        q = q.filter(models.ClimsoftUser.userRole.ilike(f"%{role}%"))

    return (
        get_count(q),
        [
            climsoftuser_schema.ClimsoftUser.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    username: str,
    role: str,
) -> climsoftuser_schema.ClimsoftUser:
    get_or_404(db_session, username)
    db_session.query(
        models.ClimsoftUser
    ).filter_by(userName=username).update(
        {
            "userRole": role
        }
    )
    db_session.commit()
    updated_climsoft_user = (
        db_session.query(models.ClimsoftUser).filter_by(
            userName=username
        ).first()
    )
    return climsoftuser_schema.ClimsoftUser.from_orm(updated_climsoft_user)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, username: str) -> bool:
    get_or_404(db_session, username)
    db_session.query(models.ClimsoftUser).filter_by(
        userName=username
    ).delete()
    db_session.commit()
    return True
