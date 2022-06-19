import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_hourlywind import schema as form_hourly_wind_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session
from climsoft_api.utils.common import remove_nulls_from_dict
logger = logging.getLogger("ClimsoftFormHourlyWindService")
logging.basicConfig(level=logging.INFO)


def search(
    db_session: Session,
    query: str
) -> List[form_hourly_wind_schema.FormHourlyWind]:
    results = (
        db_session.query(models.FormHourlywind)
        .filter(
            models.FormHourlywind.stationId.ilike(f"%{query}%")
            | models.FormHourlywind.yyyy == int(query)
            | models.FormHourlywind.mm == int(query)
            | models.FormHourlywind.dd == int(query)
        ).limit(50).all()
    )

    return [form_hourly_wind_schema.FormHourlyWind.from_orm(r) for r in results]


def get_or_404(
    db_session: Session, 
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int
):
    form_hourly_wind = (
        db_session.query(models.FormHourlywind)
        .filter_by(stationId=station_id)
        .filter_by(yyyy=yyyy)
        .filter_by(mm=mm)
        .filter_by(dd=dd)
        .first()
    )

    if not form_hourly_wind:
        raise HTTPException(
            status_code=404,
            detail=_("FormHourlyWind does not exist.")
        )

    return form_hourly_wind


def create(
    db_session: Session,
    data: form_hourly_wind_schema.CreateFormHourlyWind
) -> form_hourly_wind_schema.FormHourlyWind:
    form_hourly_wind = models.FormHourlywind(**remove_nulls_from_dict(data.dict()))
    db_session.add(form_hourly_wind)
    db_session.commit()
    return form_hourly_wind_schema.FormHourlyWind.from_orm(form_hourly_wind)


def get(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
) -> form_hourly_wind_schema.FormHourlyWind:
    form_hourly_wind = get_or_404(
        db_session,
        station_id,
        yyyy,
        mm,
        dd
    )
    return form_hourly_wind_schema.FormHourlyWind.from_orm(form_hourly_wind)


def query(
    db_session: Session,
    station_id: str = None,
    yyyy: int = None,
    mm: int = None,
    dd: int = None,
    elem_112_00: str = None,
    elem_112_01: str = None,
    elem_112_02: str = None,
    elem_112_03: str = None,
    elem_112_04: str = None,
    elem_112_05: str = None,
    elem_112_06: str = None,
    elem_112_07: str = None,
    elem_112_08: str = None,
    elem_112_09: str = None,
    elem_112_10: str = None,
    elem_112_11: str = None,
    elem_112_12: str = None,
    elem_112_13: str = None,
    elem_112_14: str = None,
    elem_112_15: str = None,
    elem_112_16: str = None,
    elem_112_17: str = None,
    elem_112_18: str = None,
    elem_112_19: str = None,
    elem_112_20: str = None,
    elem_112_21: str = None,
    elem_112_22: str = None,
    elem_112_23: str = None,
    elem_111_00: str = None,
    elem_111_01: str = None,
    elem_111_02: str = None,
    elem_111_03: str = None,
    elem_111_04: str = None,
    elem_111_05: str = None,
    elem_111_06: str = None,
    elem_111_07: str = None,
    elem_111_08: str = None,
    elem_111_09: str = None,
    elem_111_10: str = None,
    elem_111_11: str = None,
    elem_111_12: str = None,
    elem_111_13: str = None,
    elem_111_14: str = None,
    elem_111_15: str = None,
    elem_111_16: str = None,
    elem_111_17: str = None,
    elem_111_18: str = None,
    elem_111_19: str = None,
    elem_111_20: str = None,
    elem_111_21: str = None,
    elem_111_22: str = None,
    elem_111_23: str = None,
    ddflag00: str = None,
    ddflag01: str = None,
    ddflag02: str = None,
    ddflag03: str = None,
    ddflag04: str = None,
    ddflag05: str = None,
    ddflag06: str = None,
    ddflag07: str = None,
    ddflag08: str = None,
    ddflag09: str = None,
    ddflag10: str = None,
    ddflag11: str = None,
    ddflag12: str = None,
    ddflag13: str = None,
    ddflag14: str = None,
    ddflag15: str = None,
    ddflag16: str = None,
    ddflag17: str = None,
    ddflag18: str = None,
    ddflag19: str = None,
    ddflag20: str = None,
    ddflag21: str = None,
    ddflag22: str = None,
    ddflag23: str = None,
    total: str = None,
    signature: str = None,
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_hourly_wind_schema.FormHourlyWind]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_hourly_wind` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormHourlywind)

    if station_id is not None:
        q = q.filter_by(stationId=station_id)

    if yyyy is not None:
        q = q.filter_by(yyyy=yyyy)

    if mm is not None:
        q = q.filter_by(mm=mm)

    if dd is not None:
        q = q.filter_by(dd=dd)

    if elem_112_00 is not None:
        q = q.filter_by(elem_112_00=elem_112_00)

    if elem_112_01 is not None:
        q = q.filter_by(elem_112_01=elem_112_01)

    if elem_112_02 is not None:
        q = q.filter_by(elem_112_02=elem_112_02)

    if elem_112_03 is not None:
        q = q.filter_by(elem_112_03=elem_112_03)

    if elem_112_04 is not None:
        q = q.filter_by(elem_112_04=elem_112_04)

    if elem_112_05 is not None:
        q = q.filter_by(elem_112_05=elem_112_05)

    if elem_112_06 is not None:
        q = q.filter_by(elem_112_06=elem_112_06)

    if elem_112_07 is not None:
        q = q.filter_by(elem_112_07=elem_112_07)

    if elem_112_08 is not None:
        q = q.filter_by(elem_112_08=elem_112_08)

    if elem_112_09 is not None:
        q = q.filter_by(elem_112_09=elem_112_09)

    if elem_112_10 is not None:
        q = q.filter_by(elem_112_10=elem_112_10)

    if elem_112_11 is not None:
        q = q.filter_by(elem_112_11=elem_112_11)

    if elem_112_12 is not None:
        q = q.filter_by(elem_112_12=elem_112_12)

    if elem_112_13 is not None:
        q = q.filter_by(elem_112_13=elem_112_13)

    if elem_112_14 is not None:
        q = q.filter_by(elem_112_14=elem_112_14)

    if elem_112_15 is not None:
        q = q.filter_by(elem_112_15=elem_112_15)

    if elem_112_16 is not None:
        q = q.filter_by(elem_112_16=elem_112_16)

    if elem_112_17 is not None:
        q = q.filter_by(elem_112_17=elem_112_17)

    if elem_112_18 is not None:
        q = q.filter_by(elem_112_18=elem_112_18)

    if elem_112_19 is not None:
        q = q.filter_by(elem_112_19=elem_112_19)

    if elem_112_20 is not None:
        q = q.filter_by(elem_112_20=elem_112_20)

    if elem_112_21 is not None:
        q = q.filter_by(elem_112_21=elem_112_21)

    if elem_112_22 is not None:
        q = q.filter_by(elem_112_22=elem_112_22)

    if elem_112_23 is not None:
        q = q.filter_by(elem_112_23=elem_112_23)

    if elem_111_00 is not None:
        q = q.filter_by(elem_111_00=elem_111_00)

    if elem_111_01 is not None:
        q = q.filter_by(elem_111_01=elem_111_01)

    if elem_111_02 is not None:
        q = q.filter_by(elem_111_02=elem_111_02)

    if elem_111_03 is not None:
        q = q.filter_by(elem_111_03=elem_111_03)

    if elem_111_04 is not None:
        q = q.filter_by(elem_111_04=elem_111_04)

    if elem_111_05 is not None:
        q = q.filter_by(elem_111_05=elem_111_05)

    if elem_111_06 is not None:
        q = q.filter_by(elem_111_06=elem_111_06)

    if elem_111_07 is not None:
        q = q.filter_by(elem_111_07=elem_111_07)

    if elem_111_08 is not None:
        q = q.filter_by(elem_111_08=elem_111_08)

    if elem_111_09 is not None:
        q = q.filter_by(elem_111_09=elem_111_09)

    if elem_111_10 is not None:
        q = q.filter_by(elem_111_10=elem_111_10)

    if elem_111_11 is not None:
        q = q.filter_by(elem_111_11=elem_111_11)

    if elem_111_12 is not None:
        q = q.filter_by(elem_111_12=elem_111_12)

    if elem_111_13 is not None:
        q = q.filter_by(elem_111_13=elem_111_13)

    if elem_111_14 is not None:
        q = q.filter_by(elem_111_14=elem_111_14)

    if elem_111_15 is not None:
        q = q.filter_by(elem_111_15=elem_111_15)

    if elem_111_16 is not None:
        q = q.filter_by(elem_111_16=elem_111_16)

    if elem_111_17 is not None:
        q = q.filter_by(elem_111_17=elem_111_17)

    if elem_111_18 is not None:
        q = q.filter_by(elem_111_18=elem_111_18)

    if elem_111_19 is not None:
        q = q.filter_by(elem_111_19=elem_111_19)

    if elem_111_20 is not None:
        q = q.filter_by(elem_111_20=elem_111_20)

    if elem_111_21 is not None:
        q = q.filter_by(elem_111_21=elem_111_21)

    if elem_111_22 is not None:
        q = q.filter_by(elem_111_22=elem_111_22)

    if elem_111_23 is not None:
        q = q.filter_by(elem_111_23=elem_111_23)

    if ddflag00 is not None:
        q = q.filter_by(ddflag00=ddflag00)

    if ddflag01 is not None:
        q = q.filter_by(ddflag01=ddflag01)

    if ddflag02 is not None:
        q = q.filter_by(ddflag02=ddflag02)

    if ddflag03 is not None:
        q = q.filter_by(ddflag03=ddflag03)

    if ddflag04 is not None:
        q = q.filter_by(ddflag04=ddflag04)

    if ddflag05 is not None:
        q = q.filter_by(ddflag05=ddflag05)

    if ddflag06 is not None:
        q = q.filter_by(ddflag06=ddflag06)

    if ddflag07 is not None:
        q = q.filter_by(ddflag07=ddflag07)

    if ddflag08 is not None:
        q = q.filter_by(ddflag08=ddflag08)

    if ddflag09 is not None:
        q = q.filter_by(ddflag09=ddflag09)

    if ddflag10 is not None:
        q = q.filter_by(ddflag10=ddflag10)

    if ddflag11 is not None:
        q = q.filter_by(ddflag11=ddflag11)

    if ddflag12 is not None:
        q = q.filter_by(ddflag12=ddflag12)

    if ddflag13 is not None:
        q = q.filter_by(ddflag13=ddflag13)

    if ddflag14 is not None:
        q = q.filter_by(ddflag14=ddflag14)

    if ddflag15 is not None:
        q = q.filter_by(ddflag15=ddflag15)

    if ddflag16 is not None:
        q = q.filter_by(ddflag16=ddflag16)

    if ddflag17 is not None:
        q = q.filter_by(ddflag17=ddflag17)

    if ddflag18 is not None:
        q = q.filter_by(ddflag18=ddflag18)

    if ddflag19 is not None:
        q = q.filter_by(ddflag19=ddflag19)

    if ddflag20 is not None:
        q = q.filter_by(ddflag20=ddflag20)

    if ddflag21 is not None:
        q = q.filter_by(ddflag21=ddflag21)

    if ddflag22 is not None:
        q = q.filter_by(ddflag22=ddflag22)

    if ddflag23 is not None:
        q = q.filter_by(ddflag23=ddflag23)

    if total is not None:
        q = q.filter_by(total=total)

    if signature is not None:
        q = q.filter_by(signature=signature)

    if entry_datetime is not None:
        q = q.filter_by(entryDatetime=entry_datetime)

    return (
        get_count(q),
        [
            form_hourly_wind_schema.FormHourlyWind.from_orm(s) for s in q.offset(
                offset
            ).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    updates: form_hourly_wind_schema.UpdateFormHourlyWind
) -> form_hourly_wind_schema.FormHourlyWind:
    get_or_404(db_session, station_id, yyyy, mm, dd)
    db_session.query(models.FormHourlywind).filter_by(
        stationId=station_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).update(remove_nulls_from_dict(updates.dict()))
    db_session.commit()
    updated_form_hourly_wind = get_or_404(db_session, station_id, yyyy, mm, dd)
    return form_hourly_wind_schema.FormHourlyWind.from_orm(
        updated_form_hourly_wind
    )


def delete(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
) -> bool:
    get_or_404(
        db_session,
        station_id,
        yyyy,
        mm,
        dd
    )
    db_session.query(models.FormHourlywind).filter_by(
        stationId=station_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).delete()
    db_session.commit()
    return True
