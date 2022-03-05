import logging
from typing import List, Tuple

from climsoft_api.api.flag import schema as flag_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFlagService")
logging.basicConfig(level=logging.INFO)


class FailedCreatingFlag(Exception):
    pass


class FailedGettingFlag(Exception):
    pass


class FailedGettingFlagList(Exception):
    pass


class FailedUpdatingFlag(Exception):
    pass


class FailedDeletingFlag(Exception):
    pass


class FlagDoesNotExist(Exception):
    pass


def create(db_session: Session,
           data: flag_schema.CreateFlag) -> flag_schema.Flag:
    try:
        flag = models.Flag(**data.dict())
        db_session.add(flag)
        db_session.commit()
        return flag_schema.Flag.from_orm(flag)
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingFlag(
            _("Failed to create flag.")
        )


def get(db_session: Session, character_symbol: str) -> flag_schema.Flag:
    try:
        flag = (
            db_session.query(models.Flag)
                .filter_by(characterSymbol=character_symbol)
                .first()
        )

        if not flag:
            raise HTTPException(
                status_code=404,
                detail=_("Flag does not exist.")
            )

        return flag_schema.Flag.from_orm(flag)
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingFlag(
            _("Failed to get flag.")
        )


def query(
    db_session: Session,
    character_symbol: str = None,
    num_symbol: int = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[flag_schema.Flag]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `flags` row skipping
    `offset` number of rows

    """
    try:
        q = db_session.query(models.Flag)

        if character_symbol is not None:
            q = q.filter_by(characterSymbol=character_symbol)

        if num_symbol is not None:
            q = q.filter_by(numSymbol=num_symbol)

        if description is not None:
            q = q.filter(models.Flag.description.ilike(f"%{description}%"))

        return (
            get_count(q),
            [
                flag_schema.Flag.from_orm(s) for s in q.offset(
                offset
            ).limit(limit).all()
            ]
        )
    except Exception as e:
        logger.exception(e)
        raise FailedGettingFlagList(
            _("Failed to get list of flags.")
        )


def update(
    db_session: Session,
    character_symbol: str,
    updates: flag_schema.UpdateFlag
) -> flag_schema.Flag:
    try:
        db_session.query(models.Flag).filter_by(
            characterSymbol=character_symbol
        ).update(updates.dict())
        db_session.commit()
        updated_flag = (
            db_session.query(models.Flag)
                .filter_by(characterSymbol=character_symbol)
                .first()
        )
        return flag_schema.Flag.from_orm(updated_flag)
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingFlag(
            _("Failed to update flag.")
        )


def delete(db_session: Session, character_symbol: str) -> bool:
    try:
        db_session.query(models.Flag).filter_by(
            characterSymbol=character_symbol
        ).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingFlag(
            _("Failed to delete flag.")
        )
