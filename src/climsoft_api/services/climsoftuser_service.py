import logging
from typing import List, Tuple
import backoff
from climsoft_api.api.climsoftuser import schema as climsoftuser_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftUserService")
logging.basicConfig(level=logging.INFO)


def create(
    db_session: Session, data: climsoftuser_schema.CreateClimsoftUser
) -> climsoftuser_schema.ClimsoftUser:
    climsoft_user = models.ClimsoftUser(**data.dict())
    db_session.add(climsoft_user)
    db_session.commit()
    return climsoftuser_schema.ClimsoftUser.from_orm(climsoft_user)


def get(db_session: Session, username: str) -> climsoftuser_schema.ClimsoftUser:
    climsoft_user = (
        db_session.query(models.ClimsoftUser).filter_by(
            userName=username).first()
    )

    if not climsoft_user:
        raise HTTPException(
            status_code=404, detail=_("Climsoft user does not exist.")
        )

    return climsoftuser_schema.ClimsoftUser.from_orm(climsoft_user)


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


def update(
    db_session: Session,
    username: str,
    role: str,
) -> climsoftuser_schema.ClimsoftUser:
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


def delete(db_session: Session, username: str) -> bool:
    db_session.query(models.ClimsoftUser).filter_by(
        userName=username
    ).delete()
    db_session.commit()
    return True
