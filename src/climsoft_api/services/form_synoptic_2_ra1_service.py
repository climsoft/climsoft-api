import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_synoptic_2_ra1 import schema as form_synoptic_2_ra1_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session
from climsoft_api.utils.common import remove_nulls_from_dict
from typing import Optional
from pydantic import constr

logger = logging.getLogger("ClimsoftFormSynoptic2Ra1Service")
logging.basicConfig(level=logging.INFO)


def search(
    db_session: Session,
    _query: str,
    offset: int = 0,
    limit: int = 50
) -> List[form_synoptic_2_ra1_schema.FormSynoptic2Ra1]:
    results = (
        db_session.query(models.FormSynoptic2Ra1)
        .filter(
            models.FormSynoptic2Ra1.stationId.ilike(f"%{_query}%")
            | models.FormSynoptic2Ra1.yyyy == int(_query)
            | models.FormSynoptic2Ra1.mm == int(_query)
            | models.FormSynoptic2Ra1.dd == int(_query)
            | models.FormSynoptic2Ra1.hh == int(_query)
        ).offset(offset).limit(limit).all()
    )

    return [form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(r) for r in results]


def get_or_404(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    hh: int
):
    form_synoptic_2_ra1 = (
        db_session.query(models.FormSynoptic2Ra1)
        .filter_by(stationId=station_id)
        .filter_by(yyyy=yyyy)
        .filter_by(mm=mm)
        .filter_by(dd=dd)
        .filter_by(hh=hh)
        .first()
    )

    if not form_synoptic_2_ra1:
        raise HTTPException(
            status_code=404,
            detail=_("FormSynoptic2Ra1 does not exist.")
        )

    return form_synoptic_2_ra1


def create(
    db_session: Session,
    data: form_synoptic_2_ra1_schema.CreateFormSynoptic2Ra1
) -> form_synoptic_2_ra1_schema.FormSynoptic2Ra1:
    form_synoptic_2_ra1 = models.FormSynoptic2Ra1(**remove_nulls_from_dict(data.dict()))
    db_session.add(form_synoptic_2_ra1)
    db_session.commit()
    return form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(form_synoptic_2_ra1)


def get(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    hh: int
) -> form_synoptic_2_ra1_schema.FormSynoptic2Ra1:
    form_synoptic_2_ra1 = get_or_404(
        db_session,
        station_id,
        yyyy,
        mm,
        dd,
        hh
    )
    return form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(form_synoptic_2_ra1)


def query(
    db_session: Session,
    station_id: str = None,
    yyyy: int = None,
    mm: int = None,
    dd: int = None,
    hh: int = None,
    val_elem106: Optional[constr(max_length=6)] = None,
    val_elem107: Optional[constr(max_length=6)] = None,
    val_elem400: Optional[constr(max_length=6)] = None,
    val_elem814: Optional[constr(max_length=6)] = None,
    val_elem399: Optional[constr(max_length=6)] = None,
    val_elem301: Optional[constr(max_length=8)] = None,
    val_elem185: Optional[constr(max_length=6)] = None,
    val_elem101: Optional[constr(max_length=6)] = None,
    val_elem103: Optional[constr(max_length=6)] = None,
    val_elem105: Optional[constr(max_length=6)] = None,
    val_elem110: Optional[constr(max_length=6)] = None,
    val_elem114: Optional[constr(max_length=6)] = None,
    val_elem111: Optional[constr(max_length=6)] = None,
    val_elem112: Optional[constr(max_length=6)] = None,
    val_elem115: Optional[constr(max_length=6)] = None,
    val_elem168: Optional[constr(max_length=6)] = None,
    val_elem192: Optional[constr(max_length=6)] = None,
    val_elem169: Optional[constr(max_length=6)] = None,
    val_elem170: Optional[constr(max_length=6)] = None,
    val_elem171: Optional[constr(max_length=6)] = None,
    val_elem119: Optional[constr(max_length=6)] = None,
    val_elem116: Optional[constr(max_length=6)] = None,
    val_elem117: Optional[constr(max_length=6)] = None,
    val_elem118: Optional[constr(max_length=6)] = None,
    val_elem123: Optional[constr(max_length=6)] = None,
    val_elem120: Optional[constr(max_length=6)] = None,
    val_elem121: Optional[constr(max_length=6)] = None,
    val_elem122: Optional[constr(max_length=6)] = None,
    val_elem127: Optional[constr(max_length=6)] = None,
    val_elem124: Optional[constr(max_length=6)] = None,
    val_elem125: Optional[constr(max_length=6)] = None,
    val_elem126: Optional[constr(max_length=6)] = None,
    val_elem131: Optional[constr(max_length=6)] = None,
    val_elem128: Optional[constr(max_length=6)] = None,
    val_elem129: Optional[constr(max_length=6)] = None,
    val_elem130: Optional[constr(max_length=6)] = None,
    val_elem167: Optional[constr(max_length=6)] = None,
    val_elem197: Optional[constr(max_length=6)] = None,
    val_elem193: Optional[constr(max_length=6)] = None,
    val_elem018: Optional[constr(max_length=6)] = None,
    val_elem532: Optional[constr(max_length=6)] = None,
    val_elem132: Optional[constr(max_length=6)] = None,
    val_elem005: Optional[constr(max_length=6)] = None,
    val_elem174: Optional[constr(max_length=6)] = None,
    val_elem003: Optional[constr(max_length=6)] = None,
    val_elem002: Optional[constr(max_length=6)] = None,
    val_elem084: Optional[constr(max_length=6)] = None,
    val_elem046: Optional[constr(max_length=6)] = None,
    flag106: Optional[constr(max_length=1)] = None,
    flag107: Optional[constr(max_length=1)] = None,
    flag400: Optional[constr(max_length=1)] = None,
    flag814: Optional[constr(max_length=1)] = None,
    flag399: Optional[constr(max_length=1)] = None,
    flag301: Optional[constr(max_length=1)] = None,
    flag185: Optional[constr(max_length=1)] = None,
    flag101: Optional[constr(max_length=1)] = None,
    flag103: Optional[constr(max_length=1)] = None,
    flag105: Optional[constr(max_length=1)] = None,
    flag110: Optional[constr(max_length=1)] = None,
    flag114: Optional[constr(max_length=1)] = None,
    flag111: Optional[constr(max_length=1)] = None,
    flag112: Optional[constr(max_length=1)] = None,
    flag115: Optional[constr(max_length=1)] = None,
    flag168: Optional[constr(max_length=1)] = None,
    flag192: Optional[constr(max_length=1)] = None,
    flag169: Optional[constr(max_length=1)] = None,
    flag170: Optional[constr(max_length=1)] = None,
    flag171: Optional[constr(max_length=1)] = None,
    flag119: Optional[constr(max_length=1)] = None,
    flag116: Optional[constr(max_length=1)] = None,
    flag117: Optional[constr(max_length=1)] = None,
    flag118: Optional[constr(max_length=1)] = None,
    flag123: Optional[constr(max_length=1)] = None,
    flag120: Optional[constr(max_length=1)] = None,
    flag121: Optional[constr(max_length=1)] = None,
    flag122: Optional[constr(max_length=1)] = None,
    flag127: Optional[constr(max_length=1)] = None,
    flag124: Optional[constr(max_length=1)] = None,
    flag125: Optional[constr(max_length=1)] = None,
    flag126: Optional[constr(max_length=1)] = None,
    flag131: Optional[constr(max_length=1)] = None,
    flag128: Optional[constr(max_length=1)] = None,
    flag129: Optional[constr(max_length=1)] = None,
    flag130: Optional[constr(max_length=1)] = None,
    flag167: Optional[constr(max_length=1)] = None,
    flag197: Optional[constr(max_length=1)] = None,
    flag193: Optional[constr(max_length=1)] = None,
    flag018: Optional[constr(max_length=1)] = None,
    flag532: Optional[constr(max_length=1)] = None,
    flag132: Optional[constr(max_length=1)] = None,
    flag005: Optional[constr(max_length=1)] = None,
    flag174: Optional[constr(max_length=1)] = None,
    flag003: Optional[constr(max_length=1)] = None,
    flag002: Optional[constr(max_length=1)] = None,
    flag084: Optional[constr(max_length=1)] = None,
    flag046: Optional[constr(max_length=1)] = None,
    signature: Optional[constr(max_length=6)] = None,
    entry_datetime: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_synoptic_2_ra1_schema.FormSynoptic2Ra1]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_synoptic_2_ra1` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormSynoptic2Ra1)

    if station_id is not None:
        q = q.filter_by(stationId=station_id)

    if yyyy is not None:
        q = q.filter_by(yyyy=yyyy)

    if mm is not None:
        q = q.filter_by(mm=mm)

    if dd is not None:
        q = q.filter_by(dd=dd)

    if hh is not None:
        q = q.filter_by(hh=hh)

    if val_elem106 is not None:
        q = q.filter_by(Val_Elem106=val_elem106)

    if val_elem400 is not None:
        q = q.filter_by(Val_Elem106=val_elem106)

    if val_elem814 is not None:
        q = q.filter_by(Val_Elem106=val_elem106)

    if val_elem107 is not None:
        q = q.filter_by(Val_Elem107=val_elem107)

    if val_elem399 is not None:
        q = q.filter_by(Val_Elem399=val_elem399)

    if val_elem301 is not None:
        q = q.filter_by(Val_Elem301=val_elem301)

    if val_elem185 is not None:
        q = q.filter_by(Val_Elem185=val_elem185)

    if val_elem101 is not None:
        q = q.filter_by(Val_Elem101=val_elem101)

    if val_elem046 is not None:
        q = q.filter_by(Val_Elem046=val_elem046)

    if val_elem103 is not None:
        q = q.filter_by(Val_Elem103=val_elem103)

    if val_elem105 is not None:
        q = q.filter_by(Val_Elem105=val_elem105)

    if val_elem110 is not None:
        q = q.filter_by(Val_Elem110=val_elem110)

    if val_elem114 is not None:
        q = q.filter_by(Val_Elem114=val_elem114)

    if val_elem115 is not None:
        q = q.filter_by(Val_Elem115=val_elem115)

    if val_elem168 is not None:
        q = q.filter_by(Val_Elem168=val_elem168)

    if val_elem192 is not None:
        q = q.filter_by(Val_Elem192=val_elem192)

    if val_elem169 is not None:
        q = q.filter_by(Val_Elem169=val_elem169)

    if val_elem170 is not None:
        q = q.filter_by(Val_Elem170=val_elem170)

    if val_elem171 is not None:
        q = q.filter_by(Val_Elem171=val_elem171)

    if val_elem119 is not None:
        q = q.filter_by(Val_Elem119=val_elem119)

    if val_elem116 is not None:
        q = q.filter_by(Val_Elem116=val_elem116)

    if val_elem117 is not None:
        q = q.filter_by(Val_Elem117=val_elem117)

    if val_elem118 is not None:
        q = q.filter_by(Val_Elem118=val_elem118)

    if val_elem123 is not None:
        q = q.filter_by(Val_Elem123=val_elem123)

    if val_elem120 is not None:
        q = q.filter_by(Val_Elem120=val_elem120)

    if val_elem106 is not None:
        q = q.filter_by(Val_Elem106=val_elem106)

    if val_elem121 is not None:
        q = q.filter_by(Val_Elem121=val_elem121)

    if val_elem122 is not None:
        q = q.filter_by(Val_Elem122=val_elem122)

    if val_elem127 is not None:
        q = q.filter_by(Val_Elem127=val_elem127)

    if val_elem124 is not None:
        q = q.filter_by(Val_Elem124=val_elem124)

    if val_elem125 is not None:
        q = q.filter_by(Val_Elem125=val_elem125)

    if val_elem126 is not None:
        q = q.filter_by(Val_Elem126=val_elem126)

    if val_elem131 is not None:
        q = q.filter_by(Val_Elem131=val_elem131)

    if val_elem128 is not None:
        q = q.filter_by(Val_Elem128=val_elem128)

    if val_elem129 is not None:
        q = q.filter_by(Val_Elem129=val_elem129)

    if val_elem130 is not None:
        q = q.filter_by(Val_Elem130=val_elem130)

    if val_elem167 is not None:
        q = q.filter_by(Val_Elem167=val_elem167)

    if val_elem197 is not None:
        q = q.filter_by(Val_Elem106=val_elem106)

    if val_elem193 is not None:
        q = q.filter_by(Val_Elem193=val_elem193)

    if val_elem018 is not None:
        q = q.filter_by(Val_Elem018=val_elem018)

    if val_elem532 is not None:
        q = q.filter_by(Val_Elem532=val_elem532)

    if val_elem132 is not None:
        q = q.filter_by(Val_Elem132=val_elem132)

    if val_elem005 is not None:
        q = q.filter_by(Val_Elem005=val_elem005)

    if val_elem174 is not None:
        q = q.filter_by(Val_Elem174=val_elem174)

    if val_elem003 is not None:
        q = q.filter_by(Val_Elem003=val_elem003)

    if val_elem002 is not None:
        q = q.filter_by(Val_Elem002=val_elem002)

    if val_elem084 is not None:
        q = q.filter_by(Val_Elem084=val_elem084)

    if val_elem111 is not None:
        q = q.filter_by(Val_Elem111=val_elem111)

    if val_elem112 is not None:
        q = q.filter_by(Val_Elem112=val_elem112)

    if flag106 is not None:
        q = q.filter_by(Flag106=flag106)

    if flag400 is not None:
        q = q.filter_by(Flag106=flag106)

    if flag814 is not None:
        q = q.filter_by(Flag106=flag106)

    if flag107 is not None:
        q = q.filter_by(Flag107=flag107)

    if flag399 is not None:
        q = q.filter_by(Flag399=flag399)

    if flag301 is not None:
        q = q.filter_by(Flag301=flag301)

    if flag185 is not None:
        q = q.filter_by(Flag185=flag185)

    if flag101 is not None:
        q = q.filter_by(Flag101=flag101)

    if flag103 is not None:
        q = q.filter_by(Flag103=flag103)

    if flag105 is not None:
        q = q.filter_by(Flag105=flag105)

    if flag110 is not None:
        q = q.filter_by(Flag110=flag110)

    if flag114 is not None:
        q = q.filter_by(Flag114=flag114)

    if flag115 is not None:
        q = q.filter_by(Flag115=flag115)

    if flag168 is not None:
        q = q.filter_by(Flag168=flag168)

    if flag192 is not None:
        q = q.filter_by(Flag192=flag192)

    if flag169 is not None:
        q = q.filter_by(Flag169=flag169)

    if flag170 is not None:
        q = q.filter_by(Flag170=flag170)

    if flag171 is not None:
        q = q.filter_by(Flag171=flag171)

    if flag119 is not None:
        q = q.filter_by(Flag119=flag119)

    if flag116 is not None:
        q = q.filter_by(Flag116=flag116)

    if flag117 is not None:
        q = q.filter_by(Flag117=flag117)

    if flag118 is not None:
        q = q.filter_by(Flag118=flag118)

    if flag123 is not None:
        q = q.filter_by(Flag123=flag123)

    if flag120 is not None:
        q = q.filter_by(Flag120=flag120)

    if flag106 is not None:
        q = q.filter_by(Flag106=flag106)

    if flag121 is not None:
        q = q.filter_by(Flag121=flag121)

    if flag122 is not None:
        q = q.filter_by(Flag122=flag122)

    if flag127 is not None:
        q = q.filter_by(Flag127=flag127)

    if flag124 is not None:
        q = q.filter_by(Flag124=flag124)

    if flag125 is not None:
        q = q.filter_by(Flag125=flag125)

    if flag126 is not None:
        q = q.filter_by(Flag126=flag126)

    if flag131 is not None:
        q = q.filter_by(Flag131=flag131)

    if flag128 is not None:
        q = q.filter_by(Flag128=flag128)

    if flag129 is not None:
        q = q.filter_by(Flag129=flag129)

    if flag130 is not None:
        q = q.filter_by(Flag130=flag130)

    if flag167 is not None:
        q = q.filter_by(Flag167=flag167)

    if flag197 is not None:
        q = q.filter_by(Flag106=flag106)

    if flag193 is not None:
        q = q.filter_by(Flag193=flag193)

    if flag018 is not None:
        q = q.filter_by(Flag018=flag018)

    if flag532 is not None:
        q = q.filter_by(Flag532=flag532)

    if flag132 is not None:
        q = q.filter_by(Flag132=flag132)

    if flag005 is not None:
        q = q.filter_by(Flag005=flag005)

    if flag174 is not None:
        q = q.filter_by(Flag174=flag174)

    if flag003 is not None:
        q = q.filter_by(Flag003=flag003)

    if flag002 is not None:
        q = q.filter_by(Flag002=flag002)

    if flag084 is not None:
        q = q.filter_by(Flag084=flag084)

    if flag111 is not None:
        q = q.filter_by(Flag111=flag111)

    if flag112 is not None:
        q = q.filter_by(Flag112=flag112)

    if flag046 is not None:
        q = q.filter_by(Flag046=flag046)

    if signature is not None:
        q = q.filter_by(signature=signature)

    if entry_datetime is not None:
        q = q.filter_by(entryDatetime=entry_datetime)

    return (
        get_count(q),
        [
            form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(s) for s in q.offset(
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
    hh: int,
    updates: form_synoptic_2_ra1_schema.UpdateFormSynoptic2Ra1
) -> form_synoptic_2_ra1_schema.FormSynoptic2Ra1:
    get_or_404(db_session, station_id, yyyy, mm, dd, hh)
    db_session.query(models.FormSynoptic2Ra1).filter_by(
        stationId=station_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).filter_by(
        hh=hh
    ).update(updates.dict())
    db_session.commit()
    updated_form_synoptic_2_ra1 = (
        db_session.query(models.FormSynoptic2Ra1)
        .filter_by(
            stationId=station_id
        ).filter_by(
            yyyy=yyyy
        ).filter_by(
            mm=mm
        ).filter_by(
            dd=dd
        ).filter_by(
            hh=hh
        ).first()
    )
    return form_synoptic_2_ra1_schema.FormSynoptic2Ra1.from_orm(updated_form_synoptic_2_ra1)


def delete(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    hh: int
) -> bool:
    get_or_404(
        db_session,
        station_id,
        yyyy,
        mm,
        dd,
        hh
    )
    db_session.query(models.FormSynoptic2Ra1).filter_by(
        stationId=station_id
    ).filter_by(
        yyyy=yyyy
    ).filter_by(
        mm=mm
    ).filter_by(
        dd=dd
    ).filter_by(
        hh=hh
    ).delete()
    db_session.commit()
    return True
