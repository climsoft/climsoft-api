import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_monthly import schema as form_monthly_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session
from climsoft_api.utils.common import remove_nulls_from_dict

logger = logging.getLogger("ClimsoftFormMonthlyService")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session, 
    station_id: str,
    element_id: int,
    yyyy: int
):
    form_monthly = (
        db_session.query(models.FormMonthly)
        .filter_by(stationId=station_id)
        .filter_by(elementId=element_id)
        .filter_by(yyyy=yyyy)
        .first()
    )

    if not form_monthly:
        raise HTTPException(
            status_code=404,
            detail=_("FormMonthly does not exist.")
        )

    return form_monthly


def create(
    db_session: Session,
    data: form_monthly_schema.CreateFormMonthly
) -> form_monthly_schema.FormMonthly:
    form_monthly = models.FormMonthly(**remove_nulls_from_dict(data.dict()))
    db_session.add(form_monthly)
    db_session.commit()
    return form_monthly_schema.FormMonthly.from_orm(form_monthly)


def get(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int
) -> form_monthly_schema.FormMonthly:
    form_monthly = get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy
    )
    return form_monthly_schema.FormMonthly.from_orm(form_monthly)


def query(
    db_session: Session,
    station_id: str = None,
    element_id: int = None,
    yyyy: int = None,
    mm_01: str = None,
    mm_02: str = None,
    mm_03: str = None,
    mm_04: str = None,
    mm_05: str = None,
    mm_06: str = None,
    mm_07: str = None,
    mm_08: str = None,
    mm_09: str = None,
    mm_10: str = None,
    mm_11: str = None,
    mm_12: str = None,
    flag01: str = None,
    flag02: str = None,
    flag03: str = None,
    flag04: str = None,
    flag05: str = None,
    flag06: str = None,
    flag07: str = None,
    flag08: str = None,
    flag09: str = None,
    flag10: str = None,
    flag11: str = None,
    flag12: str = None,
    period01: str = None,
    period02: str = None,
    period03: str = None,
    period04: str = None,
    period05: str = None,
    period06: str = None,
    period07: str = None,
    period08: str = None,
    period09: str = None,
    period10: str = None,
    period11: str = None,
    period12: str = None,
    signature: str = None,
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_monthly_schema.FormMonthly]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_monthly` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormMonthly)

    if station_id is not None:
        q = q.filter_by(stationId=station_id)

    if element_id is not None:
        q = q.filter_by(elementId=element_id)

    if yyyy is not None:
        q = q.filter_by(yyyy=yyyy)

    if mm_01 is not None:
        q = q.filter_by(mm_01=mm_01)

    if mm_02 is not None:
        q = q.filter_by(mm_02=mm_02)

    if mm_03 is not None:
        q = q.filter_by(mm_03=mm_03)

    if mm_04 is not None:
        q = q.filter_by(mm_04=mm_04)

    if mm_05 is not None:
        q = q.filter_by(mm_05=mm_05)

    if mm_06 is not None:
        q = q.filter_by(mm_06=mm_06)

    if mm_07 is not None:
        q = q.filter_by(mm_07=mm_07)

    if mm_08 is not None:
        q = q.filter_by(mm_08=mm_08)

    if mm_09 is not None:
        q = q.filter_by(mm_09=mm_09)

    if mm_10 is not None:
        q = q.filter_by(mm_10=mm_10)

    if mm_11 is not None:
        q = q.filter_by(mm_11=mm_11)

    if mm_12 is not None:
        q = q.filter_by(mm_12=mm_12)

    if flag01 is not None:
        q = q.filter_by(flag01=flag01)

    if flag02 is not None:
        q = q.filter_by(flag02=flag02)

    if flag03 is not None:
        q = q.filter_by(flag03=flag03)

    if flag04 is not None:
        q = q.filter_by(flag04=flag04)

    if flag05 is not None:
        q = q.filter_by(flag05=flag05)

    if flag06 is not None:
        q = q.filter_by(flag06=flag06)

    if flag07 is not None:
        q = q.filter_by(flag07=flag07)

    if flag08 is not None:
        q = q.filter_by(flag08=flag08)

    if flag09 is not None:
        q = q.filter_by(flag09=flag09)

    if flag10 is not None:
        q = q.filter_by(flag10=flag10)

    if flag11 is not None:
        q = q.filter_by(flag11=flag11)

    if flag12 is not None:
        q = q.filter_by(flag12=flag12)

    if period01 is not None:
        q = q.filter_by(period01=period01)

    if period02 is not None:
        q = q.filter_by(period02=period02)

    if period03 is not None:
        q = q.filter_by(period03=period03)

    if period04 is not None:
        q = q.filter_by(period04=period04)

    if period05 is not None:
        q = q.filter_by(period05=period05)

    if period06 is not None:
        q = q.filter_by(period06=period06)

    if period07 is not None:
        q = q.filter_by(period07=period07)

    if period08 is not None:
        q = q.filter_by(period08=period08)

    if period09 is not None:
        q = q.filter_by(period09=period09)

    if period10 is not None:
        q = q.filter_by(period10=period10)

    if period11 is not None:
        q = q.filter_by(period11=period11)

    if period12 is not None:
        q = q.filter_by(period12=period12)

    if signature is not None:
        q = q.filter_by(signature=signature)

    if entry_datetime is not None:
        q = q.filter_by(entryDatetime=entry_datetime)

    return (
        get_count(q),
        [
            form_monthly_schema.FormMonthly.from_orm(s) for s in q.offset(
                offset
            ).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    updates: form_monthly_schema.UpdateFormMonthly
) -> form_monthly_schema.FormMonthly:
    get_or_404(db_session, station_id, element_id, yyyy)
    db_session.query(models.FormMonthly).filter_by(
        station_id=station_id
    ).filter_by(
        element_id=element_id
    ).filter_by(
        yyyy=yyyy
    ).update(updates.dict())
    db_session.commit()
    updated_form_monthly = (
        db_session.query(models.FormMonthly)
        .filter_by(
            station_id=station_id
        ).filter_by(
            element_id=element_id
        ).filter_by(
            yyyy=yyyy
        ).first()
    )
    return form_monthly_schema.FormMonthly.from_orm(updated_form_monthly)


def delete(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
) -> bool:
    get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy
    )
    db_session.query(models.FormMonthly).filter_by(
        station_id=station_id
    ).filter_by(
        element_id=element_id
    ).filter_by(
        yyyy=yyyy
    ).delete()
    db_session.commit()
    return True
