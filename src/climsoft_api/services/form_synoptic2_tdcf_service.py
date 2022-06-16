import datetime
import logging
from typing import List, Tuple
from climsoft_api.api.form_synoptic2_tdcf import schema as form_synoptic_2_tdcf_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session
from climsoft_api.utils.common import remove_nulls_from_dict
from typing import Optional
from pydantic import constr

logger = logging.getLogger("ClimsoftFormSynoptic2TdcfService")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    hh: int
):
    form_synoptic_2_tdcf = (
        db_session.query(models.FormSynoptic2Tdcf)
        .filter_by(stationId=station_id)
        .filter_by(yyyy=yyyy)
        .filter_by(mm=mm)
        .filter_by(dd=dd)
        .filter_by(hh=hh)
        .first()
    )

    if not form_synoptic_2_tdcf:
        raise HTTPException(
            status_code=404,
            detail=_("FormSynoptic2Tdcf does not exist.")
        )

    return form_synoptic_2_tdcf


def create(
    db_session: Session,
    data: form_synoptic_2_tdcf_schema.CreateFormSynoptic2Tdcf
) -> form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf:
    form_synoptic_2_tdcf = models.FormSynoptic2Tdcf(**remove_nulls_from_dict(data.dict()))
    db_session.add(form_synoptic_2_tdcf)
    db_session.commit()
    return form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf.from_orm(form_synoptic_2_tdcf)


def get(
    db_session: Session,
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    hh: int
) -> form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf:
    form_synoptic_2_tdcf = get_or_404(
        db_session,
        station_id,
        yyyy,
        mm,
        dd,
        hh
    )
    return form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf.from_orm(form_synoptic_2_tdcf)


def query(
    db_session: Session,
    station_id: str = None,
    yyyy: int = None,
    mm: int = None,
    dd: int = None,
    hh: int = None,
    _106: Optional[constr(max_length=6)] = None,
    _107: Optional[constr(max_length=6)] = None,
    _399: Optional[constr(max_length=5)] = None,
    _301: Optional[constr(max_length=8)] = None,
    _185: Optional[constr(max_length=6)] = None,
    _101: Optional[constr(max_length=5)] = None,
    _103: Optional[constr(max_length=5)] = None,
    _105: Optional[constr(max_length=50)] = None,
    _110: Optional[constr(max_length=5)] = None,
    _114: Optional[constr(max_length=5)] = None,
    _115: Optional[constr(max_length=5)] = None,
    _168: Optional[constr(max_length=5)] = None,
    _192: Optional[constr(max_length=5)] = None,
    _169: Optional[constr(max_length=5)] = None,
    _170: Optional[constr(max_length=5)] = None,
    _171: Optional[constr(max_length=5)] = None,
    _119: Optional[constr(max_length=5)] = None,
    _116: Optional[constr(max_length=5)] = None,
    _117: Optional[constr(max_length=5)] = None,
    _118: Optional[constr(max_length=5)] = None,
    _123: Optional[constr(max_length=5)] = None,
    _120: Optional[constr(max_length=5)] = None,
    _121: Optional[constr(max_length=5)] = None,
    _122: Optional[constr(max_length=5)] = None,
    _127: Optional[constr(max_length=5)] = None,
    _124: Optional[constr(max_length=5)] = None,
    _125: Optional[constr(max_length=5)] = None,
    _126: Optional[constr(max_length=5)] = None,
    _131: Optional[constr(max_length=5)] = None,
    _128: Optional[constr(max_length=5)] = None,
    _129: Optional[constr(max_length=5)] = None,
    _130: Optional[constr(max_length=5)] = None,
    _167: Optional[constr(max_length=5)] = None,
    _197: Optional[constr(max_length=50)] = None,
    _193: Optional[constr(max_length=5)] = None,
    _18: Optional[constr(max_length=6)] = None,
    _532: Optional[constr(max_length=6)] = None,
    _132: Optional[constr(max_length=6)] = None,
    _5: Optional[constr(max_length=6)] = None,
    _174: Optional[constr(max_length=50)] = None,
    _3: Optional[constr(max_length=5)] = None,
    _2: Optional[constr(max_length=5)] = None,
    _85: Optional[constr(max_length=50)] = None,
    _111: Optional[constr(max_length=5)] = None,
    _112: Optional[constr(max_length=5)] = None,
    flag01: Optional[constr(max_length=1)] = None,
    flag02: Optional[constr(max_length=1)] = None,
    flag03: Optional[constr(max_length=1)] = None,
    flag04: Optional[constr(max_length=1)] = None,
    flag05: Optional[constr(max_length=1)] = None,
    flag06: Optional[constr(max_length=1)] = None,
    flag07: Optional[constr(max_length=1)] = None,
    flag08: Optional[constr(max_length=1)] = None,
    flag09: Optional[constr(max_length=1)] = None,
    flag10: Optional[constr(max_length=1)] = None,
    flag11: Optional[constr(max_length=1)] = None,
    flag12: Optional[constr(max_length=1)] = None,
    flag13: Optional[constr(max_length=1)] = None,
    flag14: Optional[constr(max_length=1)] = None,
    flag15: Optional[constr(max_length=1)] = None,
    flag16: Optional[constr(max_length=1)] = None,
    flag17: Optional[constr(max_length=1)] = None,
    flag18: Optional[constr(max_length=1)] = None,
    flag19: Optional[constr(max_length=1)] = None,
    flag20: Optional[constr(max_length=1)] = None,
    flag21: Optional[constr(max_length=1)] = None,
    flag22: Optional[constr(max_length=1)] = None,
    flag23: Optional[constr(max_length=1)] = None,
    flag24: Optional[constr(max_length=1)] = None,
    flag25: Optional[constr(max_length=1)] = None,
    flag26: Optional[constr(max_length=1)] = None,
    flag27: Optional[constr(max_length=1)] = None,
    flag28: Optional[constr(max_length=1)] = None,
    flag29: Optional[constr(max_length=1)] = None,
    flag30: Optional[constr(max_length=1)] = None,
    flag31: Optional[constr(max_length=1)] = None,
    flag32: Optional[constr(max_length=1)] = None,
    flag33: Optional[constr(max_length=1)] = None,
    flag34: Optional[constr(max_length=1)] = None,
    flag35: Optional[constr(max_length=1)] = None,
    flag36: Optional[constr(max_length=1)] = None,
    flag37: Optional[constr(max_length=1)] = None,
    flag38: Optional[constr(max_length=1)] = None,
    flag39: Optional[constr(max_length=1)] = None,
    flag40: Optional[constr(max_length=1)] = None,
    flag41: Optional[constr(max_length=1)] = None,
    flag42: Optional[constr(max_length=1)] = None,
    flag43: Optional[constr(max_length=1)] = None,
    flag44: Optional[constr(max_length=1)] = None,
    flag45: Optional[constr(max_length=1)] = None,
    signature: Optional[constr(max_length=50)] = None,
    entry_datetime: Optional[str] = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `form_synoptic_2_tdcf` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.FormSynoptic2Tdcf)

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

    if _106 is not None:
        q = q.filter_by(_106=_106)

    if _107 is not None:
        q = q.filter_by(_107=_107)

    if _399 is not None:
        q = q.filter_by(_399=_399)

    if _301 is not None:
        q = q.filter_by(_301=_301)

    if _185 is not None:
        q = q.filter_by(_185=_185)

    if _101 is not None:
        q = q.filter_by(_101=_101)

    if _103 is not None:
        q = q.filter_by(_103=_103)

    if _105 is not None:
        q = q.filter_by(_105=_105)

    if _110 is not None:
        q = q.filter_by(_110=_110)

    if _114 is not None:
        q = q.filter_by(_114=_114)

    if _115 is not None:
        q = q.filter_by(_115=_115)

    if _168 is not None:
        q = q.filter_by(_168=_168)

    if _192 is not None:
        q = q.filter_by(_192=_192)

    if _169 is not None:
        q = q.filter_by(_169=_169)

    if _170 is not None:
        q = q.filter_by(_170=_170)

    if _171 is not None:
        q = q.filter_by(_171=_171)

    if _119 is not None:
        q = q.filter_by(_119=_119)

    if _116 is not None:
        q = q.filter_by(_116=_116)

    if _117 is not None:
        q = q.filter_by(_117=_117)

    if _118 is not None:
        q = q.filter_by(_118=_118)

    if _123 is not None:
        q = q.filter_by(_123=_123)

    if _120 is not None:
        q = q.filter_by(_120=_120)

    if _106 is not None:
        q = q.filter_by(_106=_106)

    if _121 is not None:
        q = q.filter_by(_121=_121)

    if _122 is not None:
        q = q.filter_by(_122=_122)

    if _127 is not None:
        q = q.filter_by(_127=_127)

    if _124 is not None:
        q = q.filter_by(_124=_124)

    if _125 is not None:
        q = q.filter_by(_125=_125)

    if _126 is not None:
        q = q.filter_by(_126=_126)

    if _131 is not None:
        q = q.filter_by(_131=_131)

    if _128 is not None:
        q = q.filter_by(_128=_128)

    if _129 is not None:
        q = q.filter_by(_129=_129)

    if _130 is not None:
        q = q.filter_by(_130=_130)

    if _167 is not None:
        q = q.filter_by(_167=_167)

    if _197 is not None:
        q = q.filter_by(_106=_106)

    if _193 is not None:
        q = q.filter_by(_193=_193)

    if _18 is not None:
        q = q.filter_by(_18=_18)

    if _532 is not None:
        q = q.filter_by(_532=_532)

    if _132 is not None:
        q = q.filter_by(_132=_132)

    if _5 is not None:
        q = q.filter_by(_5=_5)

    if _174 is not None:
        q = q.filter_by(_174=_174)

    if _3 is not None:
        q = q.filter_by(_3=_3)

    if _2 is not None:
        q = q.filter_by(_2=_2)

    if _85 is not None:
        q = q.filter_by(_85=_85)

    if _111 is not None:
        q = q.filter_by(_111=_111)

    if _112 is not None:
        q = q.filter_by(_112=_112)

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

    if flag21 is not None:
        q = q.filter_by(flag21=flag21)

    if flag22 is not None:
        q = q.filter_by(flag22=flag22)

    if flag23 is not None:
        q = q.filter_by(flag23=flag23)

    if flag24 is not None:
        q = q.filter_by(flag04=flag04)

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

    if flag32 is not None:
        q = q.filter_by(flag32=flag32)

    if flag33 is not None:
        q = q.filter_by(flag33=flag33)

    if flag34 is not None:
        q = q.filter_by(flag34=flag34)

    if flag35 is not None:
        q = q.filter_by(flag35=flag35)

    if flag36 is not None:
        q = q.filter_by(flag36=flag36)

    if flag37 is not None:
        q = q.filter_by(flag37=flag37)

    if flag38 is not None:
        q = q.filter_by(flag38=flag38)

    if flag39 is not None:
        q = q.filter_by(flag39=flag39)

    if flag40 is not None:
        q = q.filter_by(flag40=flag40)

    if flag41 is not None:
        q = q.filter_by(flag41=flag41)

    if flag42 is not None:
        q = q.filter_by(flag42=flag42)

    if flag43 is not None:
        q = q.filter_by(flag43=flag43)

    if flag44 is not None:
        q = q.filter_by(flag44=flag44)

    if flag45 is not None:
        q = q.filter_by(flag45=flag45)

    if signature is not None:
        q = q.filter_by(signature=signature)

    if entry_datetime is not None:
        q = q.filter_by(entryDatetime=entry_datetime)

    return (
        get_count(q),
        [
            form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf.from_orm(s) for s in q.offset(
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
    updates: form_synoptic_2_tdcf_schema.UpdateFormSynoptic2Tdcf
) -> form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf:
    get_or_404(db_session, station_id, yyyy, mm, dd, hh)
    db_session.query(models.FormSynoptic2Tdcf).filter_by(
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
    updated_form_synoptic_2_tdcf = (
        db_session.query(models.FormSynoptic2Tdcf)
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
    return form_synoptic_2_tdcf_schema.FormSynoptic2Tdcf.from_orm(updated_form_synoptic_2_tdcf)


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
    db_session.query(models.FormSynoptic2Tdcf).filter_by(
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
