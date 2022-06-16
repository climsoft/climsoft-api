import climsoft_api.api.form_synoptic_2_ra1.schema as form_synoptic_2_ra1_schema
from climsoft_api.api import deps
from climsoft_api.services import form_synoptic_2_ra1_service
from climsoft_api.utils.response import get_success_response, \
    get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging
from climsoft_api.utils.exception import handle_exceptions
from pydantic import constr
from typing import Optional


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get("/form_synoptic_2_ra1s")
@handle_exceptions
def get_form_synoptic_2_ra1s(
    station_id: str = None,
    yyyy: int = None,
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
    signature: str = None,
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_synoptic_2_ra1s = form_synoptic_2_ra1_service.query(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        dd=dd,
        hh=hh,
        signature=signature,
        entry_datetime=entry_datetime,
        val_elem106=val_elem106,
        val_elem107=val_elem107,
        val_elem400=val_elem400,
        val_elem814=val_elem814,
        val_elem399=val_elem399,
        val_elem301=val_elem301,
        val_elem185=val_elem185,
        val_elem101=val_elem101,
        val_elem103=val_elem103,
        val_elem105=val_elem105,
        val_elem110=val_elem110,
        val_elem114=val_elem114,
        val_elem111=val_elem111,
        val_elem112=val_elem112,
        val_elem115=val_elem115,
        val_elem168=val_elem168,
        val_elem192=val_elem192,
        val_elem169=val_elem169,
        val_elem170=val_elem170,
        val_elem171=val_elem171,
        val_elem119=val_elem119,
        val_elem116=val_elem116,
        val_elem117=val_elem117,
        val_elem118=val_elem118,
        val_elem123=val_elem123,
        val_elem120=val_elem120,
        val_elem121=val_elem121,
        val_elem122=val_elem122,
        val_elem127=val_elem127,
        val_elem124=val_elem124,
        val_elem125=val_elem125,
        val_elem126=val_elem126,
        val_elem131=val_elem131,
        val_elem128=val_elem128,
        val_elem129=val_elem129,
        val_elem130=val_elem130,
        val_elem167=val_elem167,
        val_elem197=val_elem197,
        val_elem193=val_elem193,
        val_elem018=val_elem018,
        val_elem532=val_elem532,
        val_elem132=val_elem132,
        val_elem005=val_elem005,
        val_elem174=val_elem174,
        val_elem003=val_elem003,
        val_elem002=val_elem002,
        val_elem084=val_elem084,
        val_elem046=val_elem046,
        flag106=flag106,
        flag107=flag107,
        flag400=flag400,
        flag814=flag814,
        flag399=flag399,
        flag301=flag301,
        flag185=flag185,
        flag101=flag101,
        flag103=flag103,
        flag105=flag105,
        flag110=flag110,
        flag114=flag114,
        flag111=flag111,
        flag112=flag112,
        flag115=flag115,
        flag168=flag168,
        flag192=flag192,
        flag169=flag169,
        flag170=flag170,
        flag171=flag171,
        flag119=flag119,
        flag116=flag116,
        flag117=flag117,
        flag118=flag118,
        flag123=flag123,
        flag120=flag120,
        flag121=flag121,
        flag122=flag122,
        flag127=flag127,
        flag124=flag124,
        flag125=flag125,
        flag126=flag126,
        flag131=flag131,
        flag128=flag128,
        flag129=flag129,
        flag130=flag130,
        flag167=flag167,
        flag197=flag197,
        flag193=flag193,
        flag018=flag018,
        flag532=flag532,
        flag132=flag132,
        flag005=flag005,
        flag174=flag174,
        flag003=flag003,
        flag002=flag002,
        flag084=flag084,
        flag046=flag046,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_synoptic_2_ra1s,
        message=_("Successfully fetched form_synoptic_2_ra1s."),
        schema=translate_schema(
            _,
            form_synoptic_2_ra1_schema.FormSynoptic2Ra1QueryResponse.schema()
        )
    )


@router.get("/form_synoptic_2_ra1s/{station_id}/{yyyy}/{dd}/{hh}")
@handle_exceptions
def get_form_synoptic_2_ra1_by_id(
    station_id: str,
    yyyy: int,
    dd: int,
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_synoptic_2_ra1_service.get(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                dd=dd,
                hh=hh,
            )
        ],
        message=_("Successfully fetched form_synoptic_2_ra1."),
        schema=translate_schema(
            _,
            form_synoptic_2_ra1_schema.FormSynoptic2Ra1Response.schema()
        )
    )


@router.post("/form_synoptic_2_ra1s")
@handle_exceptions
def create_form_synoptic_2_ra1(
    data: form_synoptic_2_ra1_schema.CreateFormSynoptic2Ra1,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_synoptic_2_ra1_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_synoptic_2_ra1."),
        schema=translate_schema(
            _,
            form_synoptic_2_ra1_schema.FormSynoptic2Ra1Response.schema()
        )
    )


@router.put("/form_synoptic_2_ra1s/{station_id}/{yyyy}/{dd}/{hh}")
@handle_exceptions
def update_form_synoptic_2_ra1(
    station_id: str,
    yyyy: int,
    dd: int,
    hh: int,
    data: form_synoptic_2_ra1_schema.UpdateFormSynoptic2Ra1,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_synoptic_2_ra1_service.update(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                dd=dd,
                hh=hh,
                updates=data,
            )
        ],
        message=_("Successfully updated form_synoptic_2_ra1."),
        schema=translate_schema(
            _,
            form_synoptic_2_ra1_schema.FormSynoptic2Ra1Response.schema()
        )
    )


@router.delete("/form_synoptic_2_ra1s/{station_id}/{yyyy}/{dd}/{hh}")
@handle_exceptions
def delete_form_synoptic_2_ra1(
    station_id: str,
    yyyy: int,
    dd: int,
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    form_synoptic_2_ra1_service.delete(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        dd=dd,
        hh=hh,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_synoptic_2_ra1."),
        schema=translate_schema(
            _,
            form_synoptic_2_ra1_schema.FormSynoptic2Ra1Response.schema()
        )
    )
