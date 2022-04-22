import logging
from typing import List, Tuple
from climsoft_api.api.form_daily2 import schema as form_daily2_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFormDaily2Service")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session, 
    station_id: str, 
    element_id: int, 
    yyyy: int, 
    mm: int, 
    hh: int
):
    form_daily2 = (
        db_session.query(models.FormDaily2)
        .filter_by(stationId=station_id)
        .filter_by(elementId=element_id)
        .filter_by(yyyy=yyyy)
        .filter_by(mm=mm)
        .filter_by(hh=hh)
        .first()
    )

    if not form_daily2:
        raise HTTPException(
            status_code=404,
            detail=_("FormDaily2 does not exist.")
        )

    return form_daily2


def create(
    db_session: Session,
    data: form_daily2_schema.CreateFormDaily2
) -> form_daily2_schema.FormDaily2:
    form_daily2 = models.FormDaily2(**data.dict())
    db_session.add(form_daily2)
    db_session.commit()
    return form_daily2_schema.FormDaily2.from_orm(form_daily2)


def get(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    hh: int
) -> form_daily2_schema.FormDaily2:
    form_daily2 = get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy,
        mm,
        hh
    )
    return form_daily2_schema.FormDaily2.from_orm(form_daily2)


def query(
    db_session: Session,
    station_id: str = None,
    element_id: int = None,
    yyyy: int = None,
    mm: int = None,
    hh: int = None,
    day01: str = None,
    day02: str = None,
    day03: str = None,
    day04: str = None,
    day05: str = None,
    day06: str = None,
    day07: str = None,
    day08: str = None,
    day09: str = None,
    day10: str = None,
    day11: str = None,
    day12: str = None,
    day13: str = None,
    day14: str = None,
    day15: str = None,
    day16: str = None,
    day17: str = None,
    day18: str = None,
    day19: str = None,
    day20: str = None,
    day21: str = None,
    day22: str = None,
    day23: str = None,
    day24: str = None,
    day25: str = None,
    day26: str = None,
    day27: str = None,
    day28: str = None,
    day29: str = None,
    day30: str = None,
    day31: str = None,
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
    flag24: str = None,
    flag25: str = None,
    flag26: str = None,
    flag27: str = None,
    flag28: str = None,
    flag29: str = None,
    flag30: str = None,
    flag31: str = None,
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
    period13: str = None,
    period14: str = None,
    period15: str = None,
    period16: str = None,
    period17: str = None,
    period18: str = None,
    period19: str = None,
    period20: str = None,
    period21: str = None,
    period22: str = None,
    period23: str = None,
    period24: str = None,
    period25: str = None,
    period26: str = None,
    period27: str = None,
    period28: str = None,
    period29: str = None,
    period30: str = None,
    period31: str = None,
    total: str = None,
    signature: str = None,
    entry_datetime: str = None,
    temperature_units: str = None,
    precip_units: str = None,
    cloud_height_units: str = None,
    vis_units: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_daily2_schema.FormDaily2]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_daily2s` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormDaily2)

    if station_id is not None:
        q = q.filter_by(stationId=station_id)

    if element_id is not None:
        q = q.filter_by(elementId=element_id)

    if yyyy is not None:
        q = q.filter_by(yyyy=yyyy)

    if mm is not None:
        q = q.filter_by(mm=mm)

    if hh is not None:
        q = q.filter_by(hh=hh)

    if day01 is not None:
        q = q.filter_by(day01=day01)

    if day02 is not None:
        q = q.filter_by(day02=day02)

    if day03 is not None:
        q = q.filter_by(day03=day03)

    if day04 is not None:
        q = q.filter_by(day04=day04)

    if day05 is not None:
        q = q.filter_by(day05=day05)

    if day06 is not None:
        q = q.filter_by(day06=day06)

    if day07 is not None:
        q = q.filter_by(day07=day07)

    if day08 is not None:
        q = q.filter_by(day08=day08)

    if day09 is not None:
        q = q.filter_by(day09=day09)

    if day10 is not None:
        q = q.filter_by(day10=day10)

    if day11 is not None:
        q = q.filter_by(day11=day11)

    if day12 is not None:
        q = q.filter_by(day12=day12)

    if day13 is not None:
        q = q.filter_by(day13=day13)

    if day14 is not None:
        q = q.filter_by(day14=day14)

    if day15 is not None:
        q = q.filter_by(day15=day15)

    if day16 is not None:
        q = q.filter_by(day16=day16)

    if day17 is not None:
        q = q.filter_by(day17=day17)

    if day18 is not None:
        q = q.filter_by(day18=day18)

    if day19 is not None:
        q = q.filter_by(day19=day19)

    if day20 is not None:
        q = q.filter_by(day20=day20)

    if day21 is not None:
        q = q.filter_by(day21=day21)

    if day22 is not None:
        q = q.filter_by(day22=day22)

    if day23 is not None:
        q = q.filter_by(day23=day23)

    if day24 is not None:
        q = q.filter_by(day24=day24)

    if day25 is not None:
        q = q.filter_by(day25=day25)

    if day26 is not None:
        q = q.filter_by(day26=day26)

    if day27 is not None:
        q = q.filter_by(day27=day27)

    if day28 is not None:
        q = q.filter_by(day28=day28)

    if day29 is not None:
        q = q.filter_by(day29=day29)

    if day30 is not None:
        q = q.filter_by(day30=day30)

    if day31 is not None:
        q = q.filter_by(day31=day31)

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
        q = q.filter_by(flag14=flag14)

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

    if flag24 is not None:
        q = q.filter_by(flag24=flag24)

    if flag25 is not None:
        q = q.filter_by(flag25=flag25)

    if flag26 is not None:
        q = q.filter_by(flag26=flag26)

    if flag27 is not None:
        q = q.filter_by(flag27=flag27)

    if flag28 is not None:
        q = q.filter_by(flag28=flag28)

    if flag29 is not None:
        q = q.filter_by(flag29=flag29)

    if flag30 is not None:
        q = q.filter_by(flag30=flag30)

    if flag31 is not None:
        q = q.filter_by(flag31=flag31)

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

    if period13 is not None:
        q = q.filter_by(period13=period13)

    if period14 is not None:
        q = q.filter_by(period14=period14)

    if period15 is not None:
        q = q.filter_by(period15=period15)

    if period16 is not None:
        q = q.filter_by(period16=period16)

    if period17 is not None:
        q = q.filter_by(period17=period17)

    if period18 is not None:
        q = q.filter_by(period18=period18)

    if period19 is not None:
        q = q.filter_by(period19=period19)

    if period20 is not None:
        q = q.filter_by(period20=period20)

    if period21 is not None:
        q = q.filter_by(period21=period21)

    if period22 is not None:
        q = q.filter_by(period22=period22)

    if period23 is not None:
        q = q.filter_by(period23=period23)

    if period24 is not None:
        q = q.filter_by(period24=period24)

    if period25 is not None:
        q = q.filter_by(period25=period25)

    if period26 is not None:
        q = q.filter_by(period26=period26)

    if period27 is not None:
        q = q.filter_by(period27=period27)

    if period28 is not None:
        q = q.filter_by(period28=period28)

    if period29 is not None:
        q = q.filter_by(period29=period29)

    if period30 is not None:
        q = q.filter_by(period30=period30)

    if period31 is not None:
        q = q.filter_by(period31=period31)

    if total is not None:
        q = q.filter_by(total=total)

    if signature is not None:
        q = q.filter_by(signature=signature)

    if entry_datetime is not None:
        q = q.filter_by(entryDatetime=entry_datetime)

    if temperature_units is not None:
        q = q.filter_by(temperatureUnits=temperature_units)

    if precip_units is not None:
        q = q.filter_by(precipUnits=precip_units)

    if cloud_height_units is not None:
        q = q.filter_by(cloudHeightUnits=cloud_height_units)

    if vis_units is not None:
        q = q.filter_by(visUnits=vis_units)

    return (
        get_count(q),
        [
            form_daily2_schema.FormDaily2.from_orm(s) for s in q.offset(
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
    hh: int,
    updates: form_daily2_schema.UpdateFormDaily2
) -> form_daily2_schema.FormDaily2:
    get_or_404(db_session, station_id, element_id, yyyy, mm, hh)
    db_session.query(models.FormDaily2).filter_by(
        stationId=station_id
    ).filter_by(
        elementId=element_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        hh=hh
    ).update(updates.dict())
    db_session.commit()
    updated_form_daily2 = (
        db_session.query(models.FormDaily2)
        .filter_by(
            stationId=station_id
        ).filter_by(
            elementId=element_id
        ).filter_by(
            yyyy=yyyy
        ).filter_by(
            mm=mm
        ).filter_by(
            hh=hh
        ).first()
    )
    return form_daily2_schema.FormDaily2.from_orm(updated_form_daily2)


def delete(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    hh: int,
) -> bool:
    get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy,
        mm,
        hh
    )
    db_session.query(models.FormDaily2).filter_by(
        stationId=station_id
    ).filter_by(
        elementId=element_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        hh=hh
    ).delete()
    db_session.commit()
    return True
