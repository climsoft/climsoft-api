import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_agro1 import schema as form_agro1_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFormAgro1Service")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session, 
    station_id: str,
    yyyy: int, 
    mm: int, 
    dd: int
):
    form_agro1 = (
        db_session.query(models.FormAgro1)
        .filter_by(stationId=station_id)
        .filter_by(yyyy=yyyy)
        .filter_by(mm=mm)
        .filter_by(dd=dd)
        .first()
    )

    if not form_agro1:
        raise HTTPException(
            status_code=404,
            detail=_("FormAgro1 does not exist.")
        )

    return form_agro1


def create(
    db_session: Session,
    data: form_agro1_schema.CreateFormAgro1
) -> form_agro1_schema.FormAgro1:
    form_agro1 = models.FormAgro1(**data.dict())
    db_session.add(form_agro1)
    db_session.commit()
    return form_agro1_schema.FormAgro1.from_orm(form_agro1)


def get(
    db_session: Session,
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int
) -> form_agro1_schema.FormAgro1:
    form_agro1 = get_or_404(
        db_session,
        station_id,
        element_id,
        yyyy,
        mm,
        dd
    )
    return form_agro1_schema.FormAgro1.from_orm(form_agro1)


def query(
    db_session: Session,
    station_id: str = None,
    entry_datetime: datetime.datetime = None,
    yyyy: int = None,
    mm: int = None,
    dd: int = None,
    val_elem101: str = None,
    val_elem102: str = None,
    val_elem103: str = None,
    val_elem105: str = None,
    val_elem002: str = None,
    val_elem003: str = None,
    val_elem099: str = None,
    val_elem072: str = None,
    val_elem073: str = None,
    val_elem074: str = None,
    val_elem554: str = None,
    val_elem075: str = None,
    val_elem076: str = None,
    val_elem561: str = None,
    val_elem562: str = None,
    val_elem563: str = None,
    val_elem513: str = None,
    val_elem005: str = None,
    val_elem504: str = None,
    val_elem532: str = None,
    val_elem137: str = None,
    val_elem018: str = None,
    val_elem518: str = None,
    val_elem511: str = None,
    val_elem512: str = None,
    val_elem503: str = None,
    val_elem515: str = None,
    val_elem564: str = None,
    val_elem565: str = None,
    val_elem566: str = None,
    val_elem531: str = None,
    val_elem530: str = None,
    val_elem541: str = None,
    val_elem542: str = None,
    flag101: str = None,
    flag102: str = None,
    flag103: str = None,
    flag105: str = None,
    flag002: str = None,
    flag003: str = None,
    flag099: str = None,
    flag072: str = None,
    flag073: str = None,
    flag074: str = None,
    flag554: str = None,
    flag075: str = None,
    flag076: str = None,
    flag561: str = None,
    flag562: str = None,
    flag563: str = None,
    flag513: str = None,
    flag005: str = None,
    flag504: str = None,
    flag532: str = None,
    flag137: str = None,
    flag018: str = None,
    flag518: str = None,
    flag511: str = None,
    flag512: str = None,
    flag503: str = None,
    flag515: str = None,
    flag564: str = None,
    flag565: str = None,
    flag566: str = None,
    flag531: str = None,
    flag530: str = None,
    flag541: str = None,
    flag542: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_agro1_schema.FormAgro1]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_agro1s` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormAgro1)

    if station_id is not None:
        q = q.filter_by(stationId=station_id)

    if entry_datetime is not None:
        q = q.filter(models.FormAgro1.entryDatetime > entry_datetime)

    if val_elem101 is not None:
        q = q.filter_by(val_elem101=val_elem101)

    if val_elem102 is not None:
        q = q.filter_by(val_elem102=val_elem102)

    if val_elem103 is not None:
        q = q.filter_by(val_elem103=val_elem102)

    if val_elem105 is not None:
        q = q.filter_by(val_elem105=val_elem105)

    if val_elem002 is not None:
        q = q.filter_by(val_elem002=val_elem002)

    if val_elem003 is not None:
        q = q.filter_by(val_elem003=val_elem003)

    if val_elem099 is not None:
        q = q.filter_by(val_elem099=val_elem099)

    if val_elem072 is not None:
        q = q.filter_by(val_elem072=val_elem072)

    if val_elem073 is not None:
        q = q.filter_by(val_elem073=val_elem073)

    if val_elem074 is not None:
        q = q.filter_by(val_elem074=val_elem074)

    if val_elem075 is not None:
        q = q.filter_by(val_elem075=val_elem075)

    if val_elem076 is not None:
        q = q.filter_by(val_elem076=val_elem076)

    if val_elem554 is not None:
        q = q.filter_by(val_elem554=val_elem554)

    if val_elem561 is not None:
        q = q.filter_by(val_elem561=val_elem561)

    if val_elem562 is not None:
        q = q.filter_by(val_elem562=val_elem562)

    if val_elem563 is not None:
        q = q.filter_by(val_elem563=val_elem563)

    if val_elem513 is not None:
        q = q.filter_by(val_elem513=val_elem513)

    if val_elem005 is not None:
        q = q.filter_by(val_elem005=val_elem005)

    if val_elem504 is not None:
        q = q.filter_by(val_elem504=val_elem504)

    if val_elem532 is not None:
        q = q.filter_by(val_elem532=val_elem532)

    if val_elem137 is not None:
        q = q.filter_by(val_elem137=val_elem137)

    if val_elem018 is not None:
        q = q.filter_by(val_elem018=val_elem018)

    if val_elem518 is not None:
        q = q.filter_by(val_elem518=val_elem518)

    if val_elem511 is not None:
        q = q.filter_by(val_elem511=val_elem511)

    if val_elem512 is not None:
        q = q.filter_by(val_elem512=val_elem512)

    if val_elem503 is not None:
        q = q.filter_by(val_elem503=val_elem503)

    if val_elem515 is not None:
        q = q.filter_by(val_elem515=val_elem515)

    if val_elem564 is not None:
        q = q.filter_by(val_elem564=val_elem564)

    if val_elem565 is not None:
        q = q.filter_by(val_elem565=val_elem565)

    if val_elem566 is not None:
        q = q.filter_by(val_elem566=val_elem566)

    if val_elem531 is not None:
        q = q.filter_by(val_elem531=val_elem531)

    if val_elem530 is not None:
        q = q.filter_by(val_elem530=val_elem530)

    if val_elem541 is not None:
        q = q.filter_by(val_elem541=val_elem541)

    if val_elem542 is not None:
        q = q.filter_by(val_elem542=val_elem542)

    if flag101 is not None:
        q = q.filter_by(flag101=flag101)

    if flag102 is not None:
        q = q.filter_by(flag102=flag102)

    if flag103 is not None:
        q = q.filter_by(flag103=flag102)

    if flag105 is not None:
        q = q.filter_by(flag105=flag105)

    if flag002 is not None:
        q = q.filter_by(flag002=flag002)

    if flag003 is not None:
        q = q.filter_by(flag003=flag003)

    if flag099 is not None:
        q = q.filter_by(flag099=flag099)

    if flag072 is not None:
        q = q.filter_by(flag072=flag072)

    if flag073 is not None:
        q = q.filter_by(flag073=flag073)

    if flag074 is not None:
        q = q.filter_by(flag074=flag074)

    if flag075 is not None:
        q = q.filter_by(flag075=flag075)

    if flag076 is not None:
        q = q.filter_by(flag076=flag076)

    if flag554 is not None:
        q = q.filter_by(flag554=flag554)

    if flag561 is not None:
        q = q.filter_by(flag561=flag561)

    if flag562 is not None:
        q = q.filter_by(flag562=flag562)

    if flag563 is not None:
        q = q.filter_by(flag563=flag563)

    if flag513 is not None:
        q = q.filter_by(flag513=flag513)

    if flag005 is not None:
        q = q.filter_by(flag005=flag005)

    if flag504 is not None:
        q = q.filter_by(flag504=flag504)

    if flag532 is not None:
        q = q.filter_by(flag532=flag532)

    if flag137 is not None:
        q = q.filter_by(flag137=flag137)

    if flag018 is not None:
        q = q.filter_by(flag018=flag018)

    if flag518 is not None:
        q = q.filter_by(flag518=flag518)

    if flag511 is not None:
        q = q.filter_by(flag511=flag511)

    if flag512 is not None:
        q = q.filter_by(flag512=flag512)

    if flag503 is not None:
        q = q.filter_by(flag503=flag503)

    if flag515 is not None:
        q = q.filter_by(flag515=flag515)

    if flag564 is not None:
        q = q.filter_by(flag564=flag564)

    if flag565 is not None:
        q = q.filter_by(flag565=flag565)

    if flag566 is not None:
        q = q.filter_by(flag566=flag566)

    if flag531 is not None:
        q = q.filter_by(flag531=flag531)

    if flag530 is not None:
        q = q.filter_by(flag530=flag530)

    if flag541 is not None:
        q = q.filter_by(flag541=flag541)

    if flag542 is not None:
        q = q.filter_by(flag542=flag542)

    if yyyy is not None:
        q = q.filter_by(yyyy=yyyy)

    if mm is not None:
        q = q.filter_by(mm=mm)

    if dd is not None:
        q = q.filter_by(dd=dd)

    return (
        get_count(q),
        [
            form_agro1_schema.FormAgro1.from_orm(s) for s in q.offset(
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
    updates: form_agro1_schema.UpdateFormAgro1
) -> form_agro1_schema.FormAgro1:
    get_or_404(db_session, station_id, yyyy, mm, dd)
    db_session.query(models.FormAgro1).filter_by(
        stationId=station_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).update(updates.dict())
    db_session.commit()
    updated_form_agro1 = (
        db_session.query(models.FormAgro1)
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
    return form_agro1_schema.FormAgro1.from_orm(updated_form_agro1)


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
    db_session.query(models.FormAgro1).filter_by(
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
