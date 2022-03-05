import logging
from typing import List, Tuple
from sqlalchemy.orm.session import Session
from opencdms.models.climsoft import v4_1_1_core as models
from climsoft_api.api.climsoftuser import schema as climsoftuser_schema
from fastapi.exceptions import HTTPException
from climsoft_api.utils.query import get_count



logger = logging.getLogger("ClimsoftUserService")
logging.basicConfig(level=logging.INFO)


class FailedCreatingClimsoftUser(Exception):
    pass


class FailedGettingClimsoftUser(Exception):
    pass


class FailedGettingClimsoftUserList(Exception):
    pass


class FailedUpdatingClimsoftUser(Exception):
    pass


class FailedDeletingClimsoftUser(Exception):
    pass


class ClimsoftUserDoesNotExist(Exception):
    pass


def create(
    db_session: Session, data: climsoftuser_schema.CreateClimsoftUser
) -> climsoftuser_schema.ClimsoftUser:
    try:
        climsoft_user = models.ClimsoftUser(**data.dict())
        db_session.add(climsoft_user)
        db_session.commit()
        return climsoftuser_schema.ClimsoftUser.from_orm(climsoft_user)
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingClimsoftUser(
            _("Failed creating climsoft user.")
        )


def get(db_session: Session, username: str) -> climsoftuser_schema.ClimsoftUser:
    try:
        climsoft_user = (
            db_session.query(models.ClimsoftUser).filter_by(userName=username).first()
        )

        if not climsoft_user:
            raise HTTPException(
                status_code=404, detail=_("Climsoft user does not exist.")
            )

        return climsoftuser_schema.ClimsoftUser.from_orm(climsoft_user)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingClimsoftUser(
            _("Failed getting climsoft user.")
        )


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
    try:
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
    except Exception as e:
        logger.exception(e)
        raise FailedGettingClimsoftUserList(
            "Failed getting list of climsoft users."
        )


def update(
    db_session: Session,
    username: str,
    role: str,
) -> climsoftuser_schema.ClimsoftUser:
    try:
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
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingClimsoftUser(
            _("Failed updating climsoft user.")
        )


def delete(db_session: Session, username: str) -> bool:
    try:
        db_session.query(models.ClimsoftUser).filter_by(
            userName=username
        ).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingClimsoftUser(
            _("Failed deleting climsoft user.")
        )
