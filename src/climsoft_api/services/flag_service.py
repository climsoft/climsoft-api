import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.flag import schema as flag_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFlagService")
logging.basicConfig(level=logging.INFO)


def get_or_404(db_session: Session, character_symbol: str):
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

    return flag


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session,
    data: flag_schema.CreateFlag
) -> flag_schema.Flag:
    flag = models.Flag(**data.dict())
    db_session.add(flag)
    db_session.commit()
    return flag_schema.Flag.from_orm(flag)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(db_session: Session, character_symbol: str) -> flag_schema.Flag:
    flag = get_or_404(db_session, character_symbol)
    return flag_schema.Flag.from_orm(flag)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
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


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    character_symbol: str,
    updates: flag_schema.UpdateFlag
) -> flag_schema.Flag:
    get_or_404(db_session, character_symbol)
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


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, character_symbol: str) -> bool:
    get_or_404(db_session, character_symbol)
    db_session.query(models.Flag).filter_by(
        characterSymbol=character_symbol
    ).delete()
    db_session.commit()
    return True
