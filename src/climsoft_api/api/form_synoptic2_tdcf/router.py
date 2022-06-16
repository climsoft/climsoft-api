import climsoft_api.api.form_synoptic2_tdcf.schema as form_synoptic2_tdcf_schema
from climsoft_api.api import deps
from climsoft_api.services import form_synoptic2_tdcf_service
from climsoft_api.utils.response import get_success_response, \
    get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging
from climsoft_api.utils.exception import handle_exceptions


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get("/form_synoptic2_tdcfs")
@handle_exceptions
def get_form_synoptic2_tdcfs(
    station_id: str = None,
    yyyy: int = None,
    dd: int = None,
    hh: int = None,
    _106: str = None,
    _107: str = None,
    _399: str = None,
    _301: str = None,
    _185: str = None,
    _101: str = None,
    _103: str = None,
    _105: str = None,
    _110: str = None,
    _114: str = None,
    _115: str = None,
    _168: str = None,
    _192: str = None,
    _169: str = None,
    _170: str = None,
    _171: str = None,
    _119: str = None,
    _116: str = None,
    _117: str = None,
    _118: str = None,
    _123: str = None,
    _120: str = None,
    _121: str = None,
    _122: str = None,
    _127: str = None,
    _124: str = None,
    _125: str = None,
    _126: str = None,
    _131: str = None,
    _128: str = None,
    _129: str = None,
    _130: str = None,
    _167: str = None,
    _197: str = None,
    _193: str = None,
    _18: str = None,
    _532: str = None,
    _132: str = None,
    _5: str = None,
    _174: str = None,
    _3: str = None,
    _2: str = None,
    _85: str = None,
    _111: str = None,
    _112: str = None,
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
    flag32: str = None,
    flag33: str = None,
    flag34: str = None,
    flag35: str = None,
    flag36: str = None,
    flag37: str = None,
    flag38: str = None,
    flag39: str = None,
    flag40: str = None,
    flag41: str = None,
    flag42: str = None,
    flag43: str = None,
    flag44: str = None,
    flag45: str = None,
    signature: str = None,
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_synoptic2_tdcfs = form_synoptic2_tdcf_service.query(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        dd=dd,
        hh=hh,
        signature=signature,
        entry_datetime=entry_datetime,
        flag01=flag01,
        flag02=flag02,
        flag03=flag03,
        flag04=flag04,
        flag05=flag05,
        flag06=flag06,
        flag07=flag07,
        flag08=flag08,
        flag09=flag09,
        flag10=flag10,
        flag11=flag11,
        flag12=flag12,
        flag13=flag13,
        flag14=flag14,
        flag15=flag15,
        flag16=flag16,
        flag17=flag17,
        flag18=flag18,
        flag19=flag19,
        flag20=flag20,
        flag21=flag21,
        flag22=flag22,
        flag23=flag23,
        flag24=flag24,
        flag25=flag25,
        flag26=flag26,
        flag27=flag27,
        flag28=flag28,
        flag29=flag29,
        flag30=flag30,
        flag31=flag31,
        flag32=flag32,
        flag33=flag33,
        flag34=flag34,
        flag35=flag35,
        flag36=flag36,
        flag37=flag37,
        flag38=flag38,
        flag39=flag39,
        flag40=flag40,
        flag41=flag41,
        flag42=flag42,
        flag43=flag43,
        flag44=flag44,
        flag45=flag45,
        _106=_106,
        _107=_107,
        _399=_399,
        _301=_301,
        _185=_185,
        _101=_101,
        _103=_103,
        _105=_105,
        _110=_110,
        _114=_114,
        _115=_115,
        _168=_168,
        _192=_192,
        _169=_169,
        _170=_170,
        _171=_171,
        _119=_119,
        _116=_116,
        _117=_117,
        _118=_118,
        _123=_123,
        _120=_120,
        _121=_121,
        _122=_122,
        _127=_127,
        _124=_124,
        _125=_125,
        _126=_126,
        _131=_131,
        _128=_128,
        _129=_129,
        _130=_130,
        _167=_167,
        _197=_197,
        _193=_193,
        _18=_18,
        _532=_532,
        _132=_132,
        _5=_5,
        _174=_174,
        _3=_3,
        _2=_2,
        _85=_85,
        _111=_111,
        _112=_112,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_synoptic2_tdcfs,
        message=_("Successfully fetched form_synoptic2_tdcfs."),
        schema=translate_schema(
            _,
            form_synoptic2_tdcf_schema.FormSynoptic2TdcfQueryResponse.schema()
        )
    )


@router.get("/form_synoptic2_tdcfs/{station_id}/{yyyy}/{dd}/{hh}")
@handle_exceptions
def get_form_synoptic2_tdcf_by_id(
    station_id: str,
    yyyy: int,
    dd: int,
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_synoptic2_tdcf_service.get(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                dd=dd,
                hh=hh,
            )
        ],
        message=_("Successfully fetched form_synoptic2_tdcf."),
        schema=translate_schema(
            _,
            form_synoptic2_tdcf_schema.FormSynoptic2TdcfResponse.schema()
        )
    )


@router.post("/form_synoptic2_tdcfs")
@handle_exceptions
def create_form_synoptic2_tdcf(
    data: form_synoptic2_tdcf_schema.CreateFormSynoptic2Tdcf,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_synoptic2_tdcf_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_synoptic2_tdcf."),
        schema=translate_schema(
            _,
            form_synoptic2_tdcf_schema.FormSynoptic2TdcfResponse.schema()
        )
    )


@router.put("/form_synoptic2_tdcfs/{station_id}/{yyyy}/{dd}/{hh}")
@handle_exceptions
def update_form_synoptic2_tdcf(
    station_id: str,
    yyyy: int,
    dd: int,
    hh: int,
    data: form_synoptic2_tdcf_schema.UpdateFormSynoptic2Tdcf,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_synoptic2_tdcf_service.update(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                dd=dd,
                hh=hh,
                updates=data,
            )
        ],
        message=_("Successfully updated form_synoptic2_tdcf."),
        schema=translate_schema(
            _,
            form_synoptic2_tdcf_schema.FormSynoptic2TdcfResponse.schema()
        )
    )


@router.delete("/form_synoptic2_tdcfs/{station_id}/{yyyy}/{dd}/{hh}")
@handle_exceptions
def delete_form_synoptic2_tdcf(
    station_id: str,
    yyyy: int,
    dd: int,
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    form_synoptic2_tdcf_service.delete(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        dd=dd,
        hh=hh,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_synoptic2_tdcf."),
        schema=translate_schema(
            _,
            form_synoptic2_tdcf_schema.FormSynoptic2TdcfResponse.schema()
        )
    )
