import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_hourly import schema as form_hourly_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFormHourlyService")
logging.basicConfig(level=logging.INFO)


def search(
    db_session: Session,
    _query: str,
    offset: int = 0,
    limit: int = 50
) -> List[form_hourly_schema.FormHourly]:
    results = (
        db_session.query(models.FormHourly)
        .filter(
            models.FormHourly.stationId.ilike(f"%{_query}%")
            | models.FormHourly.elementId == int(_query)
            | models.FormHourly.yyyy == int(_query)
            | models.FormHourly.mm == int(_query)
            | models.FormHourly.dd == int(_query)
        ).offset(offset).limit(limit).all()
    )

    return [form_hourly_schema.FormHourly.from_orm(r) for r in results]


def get_or_404(
    db_session: Session, 
    station_id: str,
    element_id: int,
    yyyy: int, 
    mm: int, 
    dd: int
):
    form_hourly = (
        db_session.query(models.FormHourly)
        .filter_by(stationId=station_id)
        .filter_by(elementId=element_id)
        .filter_by(yyyy=yyyy)
        .filter_by(mm=mm)
        .filter_by(dd=dd)
        .first()
    )

    if not form_hourly:
        raise HTTPException(
            status_code=404,
            detail=_("FormHourly does not exist.")
        )

    return form_hourly


def create(
    db_session: Session,
    data: form_hourly_schema.CreateFormHourly
) -> form_hourly_schema.FormHourly:
    form_hourly = models.FormHourly(**data.dict())
    db_session.add(form_hourly)
    db_session.commit()
    return form_hourly_schema.FormHourly.from_orm(form_hourly)


def get(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int
) -> form_hourly_schema.FormHourly:
    form_hourly = get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy,
        mm,
        dd
    )
    return form_hourly_schema.FormHourly.from_orm(form_hourly)


def query(
    db_session: Session,
    station_id: str = None,
    element_id: int = None,
    entry_datetime: datetime.datetime = None,
    yyyy: int = None,
    mm: int = None,
    dd: int = None,
    hh_00: str = None,
    hh_01: str = None,
    hh_02: str = None,
    hh_03: str = None,
    hh_04: str = None,
    hh_05: str = None,
    hh_06: str = None,
    hh_07: str = None,
    hh_08: str = None,
    hh_09: str = None,
    hh_10: str = None,
    hh_11: str = None,
    hh_12: str = None,
    hh_13: str = None,
    hh_14: str = None,
    hh_15: str = None,
    hh_16: str = None,
    hh_17: str = None,
    hh_18: str = None,
    hh_19: str = None,
    hh_20: str = None,
    hh_21: str = None,
    hh_22: str = None,
    hh_23: str = None,
    flag00: str = None,
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
    flag13: str = None,
    flag14: str = None,
    flag15: str = None,
    flag16: str = None,
    flag17: str = None,
    flag18: str = None,
    flag19: str = None,
    flag20: str = None,
    flag21: str = None,
    flag22: str = None,
    flag23: str = None,
    total: str = None,
    signature: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_hourly_schema.FormHourly]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_hourly` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormHourly)

    if station_id is not None:
        q = q.filter_by(stationId=station_id)

    if element_id is not None:
        q = q.filter_by(elementId=element_id)

    if entry_datetime is not None:
        q = q.filter(models.FormHourly.entryDatetime > entry_datetime)

    if hh_00 is not None:
        q = q.filter_by(hh_00=hh_00)

    if hh_01 is not None:
        q = q.filter_by(hh_01=hh_01)

    if hh_02 is not None:
        q = q.filter_by(hh_02=hh_02)

    if hh_03 is not None:
        q = q.filter_by(hh_03=hh_03)

    if hh_04 is not None:
        q = q.filter_by(hh_04=hh_04)

    if hh_05 is not None:
        q = q.filter_by(hh_05=hh_05)

    if hh_06 is not None:
        q = q.filter_by(hh_06=hh_06)

    if hh_07 is not None:
        q = q.filter_by(hh_07=hh_07)

    if hh_08 is not None:
        q = q.filter_by(hh_08=hh_08)

    if hh_09 is not None:
        q = q.filter_by(hh_09=hh_09)

    if hh_10 is not None:
        q = q.filter_by(hh_10=hh_10)

    if hh_11 is not None:
        q = q.filter_by(hh_11=hh_11)

    if hh_12 is not None:
        q = q.filter_by(hh_12=hh_12)

    if hh_13 is not None:
        q = q.filter_by(hh_13=hh_13)

    if hh_14 is not None:
        q = q.filter_by(hh_14=hh_14)

    if hh_15 is not None:
        q = q.filter_by(hh_15=hh_15)

    if hh_16 is not None:
        q = q.filter_by(hh_16=hh_16)

    if hh_17 is not None:
        q = q.filter_by(hh_17=hh_17)

    if hh_18 is not None:
        q = q.filter_by(hh_18=hh_18)

    if hh_19 is not None:
        q = q.filter_by(hh_19=hh_19)

    if hh_20 is not None:
        q = q.filter_by(hh_20=hh_20)

    if hh_21 is not None:
        q = q.filter_by(hh_21=hh_21)

    if hh_22 is not None:
        q = q.filter_by(hh_22=hh_22)

    if hh_23 is not None:
        q = q.filter_by(hh_23=hh_23)

    if flag00 is not None:
        q = q.filter_by(flag00=flag00)

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

    if flag13 is not None:
        q = q.filter_by(flag13=flag13)

    if flag14 is not None:
        q = q.filter_by(flag14=flag12)

    if flag15 is not None:
        q = q.filter_by(flag15=flag15)

    if flag16 is not None:
        q = q.filter_by(flag16=flag16)

    if flag17 is not None:
        q = q.filter_by(flag17=flag17)

    if flag18 is not None:
        q = q.filter_by(flag18=flag18)

    if flag19 is not None:
        q = q.filter_by(flag19=flag19)

    if flag20 is not None:
        q = q.filter_by(flag20=flag20)

    if flag21 is not None:
        q = q.filter_by(flag21=flag21)

    if flag22 is not None:
        q = q.filter_by(flag22=flag22)

    if flag23 is not None:
        q = q.filter_by(flag23=flag23)

    if yyyy is not None:
        q = q.filter_by(yyyy=yyyy)

    if mm is not None:
        q = q.filter_by(mm=mm)

    if dd is not None:
        q = q.filter_by(dd=dd)

    if total is not None:
        q = q.filter_by(total=total)

    if signature is not None:
        q = q.filter_by(signature=signature)

    return (
        get_count(q),
        [
            form_hourly_schema.FormHourly.from_orm(s) for s in q.offset(
                offset
            ).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int,
    updates: form_hourly_schema.UpdateFormHourly
) -> form_hourly_schema.FormHourly:
    get_or_404(db_session, station_id, element_id, yyyy, mm, dd)
    db_session.query(models.FormHourly).filter_by(
        stationId=station_id
    ).filter_by(
        elementId=element_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).update(updates.dict())
    db_session.commit()
    updated_form_hourly = (
        db_session.query(models.FormHourly)
        .filter_by(
            stationId=station_id
        ).filter_by(
            yyyy=yyyy
        ).filter_by(
            mm=mm
        ).filter_by(
            dd=dd
        ).first()
    )
    return form_hourly_schema.FormHourly.from_orm(updated_form_hourly)


def delete(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int,
) -> bool:
    get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy,
        mm,
        dd
    )
    db_session.query(models.FormHourly).filter_by(
        stationId=station_id
    ).filter_by(
        elementId=element_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).delete()
    db_session.commit()
    return True
