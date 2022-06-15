import climsoft_api.api.form_hourly.schema as form_hourly_schema
from climsoft_api.api import deps
from climsoft_api.services import form_hourly_service
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


@router.get("/form_hourlys")
@handle_exceptions
def get_form_hourlys(
    station_id: str = None,
    element_id: int = None,
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
    signature: str = None,
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_hourlys = form_hourly_service.query(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        mm=mm,
        entry_datetime=entry_datetime,
        dd=dd,
        hh_00=hh_00,
        hh_01=hh_01,
        hh_02=hh_02,
        hh_03=hh_03,
        hh_04=hh_04,
        hh_05=hh_05,
        hh_06=hh_06,
        hh_07=hh_07,
        hh_08=hh_08,
        hh_09=hh_09,
        hh_10=hh_10,
        hh_11=hh_11,
        hh_12=hh_12,
        hh_13=hh_13,
        hh_14=hh_14,
        hh_15=hh_15,
        hh_16=hh_16,
        hh_17=hh_17,
        hh_18=hh_18,
        hh_19=hh_19,
        hh_20=hh_20,
        hh_21=hh_21,
        hh_22=hh_22,
        hh_23=hh_23,
        flag00=flag00,
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
        signature=signature,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_hourlys,
        message=_("Successfully fetched form hourlys."),
        schema=translate_schema(
            _,
            form_hourly_schema.FormHourlyQueryResponse.schema()
        )
    )


@router.get("/form_hourlys/{station_id}/{element_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def get_form_hourly_by_id(
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_hourly_service.get(
                db_session=db_session,
                station_id=station_id,
                element_id=element_id,
                yyyy=yyyy,
                mm=mm,
                dd=dd
            )
        ],
        message=_("Successfully fetched form_hourly."),
        schema=translate_schema(
            _,
            form_hourly_schema.FormHourlyResponse.schema()
        )
    )


@router.post("/form_hourlys")
@handle_exceptions
def create_form_hourly(
    data: form_hourly_schema.CreateFormHourly,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_hourly_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_hourly."),
        schema=translate_schema(
            _,
            form_hourly_schema.FormHourlyResponse.schema()
        )
    )


@router.put("/form_hourlys/{station_id}/{element_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def update_form_hourly(
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int,
    data: form_hourly_schema.UpdateFormHourly,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_hourly_service.update(
                db_session=db_session,
                station_id=station_id,
                element_id=element_id,
                yyyy=yyyy,
                mm=mm,
                dd=dd,
                updates=data,
            )
        ],
        message=_("Successfully updated form_hourly."),
        schema=translate_schema(
            _,
            form_hourly_schema.FormHourlyResponse.schema()
        )
    )


@router.delete("/form_hourlys/{station_id}/{element_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def delete_form_hourly(
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    dd: int,
    db_session: Session = Depends(deps.get_session)
):
    form_hourly_service.delete(
        db_session=db_session,
        station_id=station_id,
        element_id=element_id,
        yyyy=yyyy,
        mm=mm,
        dd=dd
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_hourly."),
        schema=translate_schema(
            _,
            form_hourly_schema.FormHourlyResponse.schema()
        )
    )
