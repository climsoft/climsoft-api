import climsoft_api.api.form_hourlywind.schema as form_hourlywind_schema
from climsoft_api.api import deps
from climsoft_api.services import form_hourlywind_service
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


@router.get("/form_hourlywinds")
@handle_exceptions
def get_form_hourlywinds(
    station_id: str = None,
    yyyy: int = None,
    mm: int = None,
    dd: int = None,
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
    signature: str = None,
    entry_datetime: str = None,
    total: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_hourlywinds = form_hourlywind_service.query(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        mm=mm,
        entry_datetime=entry_datetime,
        dd=dd,
        elem_111_00=elem_111_00,
        elem_111_01=elem_111_01,
        elem_111_02=elem_111_02,
        elem_111_03=elem_111_03,
        elem_111_04=elem_111_04,
        elem_111_05=elem_111_05,
        elem_111_06=elem_111_06,
        elem_111_07=elem_111_07,
        elem_111_08=elem_111_08,
        elem_111_09=elem_111_09,
        elem_111_10=elem_111_10,
        elem_111_11=elem_111_11,
        elem_111_12=elem_111_12,
        elem_111_13=elem_111_13,
        elem_111_14=elem_111_14,
        elem_111_15=elem_111_15,
        elem_111_16=elem_111_16,
        elem_111_17=elem_111_17,
        elem_111_18=elem_111_18,
        elem_111_19=elem_111_19,
        elem_111_20=elem_111_20,
        elem_111_21=elem_111_21,
        elem_111_22=elem_111_22,
        elem_111_23=elem_111_23,
        elem_112_00=elem_112_00,
        elem_112_01=elem_112_01,
        elem_112_02=elem_112_02,
        elem_112_03=elem_112_03,
        elem_112_04=elem_112_04,
        elem_112_05=elem_112_05,
        elem_112_06=elem_112_06,
        elem_112_07=elem_112_07,
        elem_112_08=elem_112_08,
        elem_112_09=elem_112_09,
        elem_112_10=elem_112_10,
        elem_112_11=elem_112_11,
        elem_112_12=elem_112_12,
        elem_112_13=elem_112_13,
        elem_112_14=elem_112_14,
        elem_112_15=elem_112_15,
        elem_112_16=elem_112_16,
        elem_112_17=elem_112_17,
        elem_112_18=elem_112_18,
        elem_112_19=elem_112_19,
        elem_112_20=elem_112_20,
        elem_112_21=elem_112_21,
        elem_112_22=elem_112_22,
        elem_112_23=elem_112_23,
        ddflag00=ddflag00,
        ddflag01=ddflag01,
        ddflag02=ddflag02,
        ddflag03=ddflag03,
        ddflag04=ddflag04,
        ddflag05=ddflag05,
        ddflag06=ddflag06,
        ddflag07=ddflag07,
        ddflag08=ddflag08,
        ddflag09=ddflag09,
        ddflag10=ddflag10,
        ddflag11=ddflag11,
        ddflag12=ddflag12,
        ddflag13=ddflag13,
        ddflag14=ddflag14,
        ddflag15=ddflag15,
        ddflag16=ddflag16,
        ddflag17=ddflag17,
        ddflag18=ddflag18,
        ddflag19=ddflag19,
        ddflag20=ddflag20,
        ddflag21=ddflag21,
        ddflag22=ddflag22,
        ddflag23=ddflag23,
        total=total,
        signature=signature,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_hourlywinds,
        message=_("Successfully fetched form hourlywinds."),
        schema=translate_schema(
            _,
            form_hourlywind_schema.FormHourlyWindQueryResponse.schema()
        )
    )


@router.get("/form_hourlywinds/{station_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def get_form_hourlywind_by_id(
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_hourlywind_service.get(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                mm=mm,
                dd=dd
            )
        ],
        message=_("Successfully fetched form_hourlywind."),
        schema=translate_schema(
            _,
            form_hourlywind_schema.FormHourlyWindResponse.schema()
        )
    )


@router.get(
    "/form_hourly_winds/search"
)
@handle_exceptions
def search_elements(
    query: str = None,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, form_hourly_winds = form_hourlywind_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_hourly_winds,
        message=_("Successfully fetched forms."),
        schema=translate_schema(
            _,
            form_hourlywind_schema.FormHourlyWindQueryResponse.schema()
        )
    )


@router.post("/form_hourlywinds")
@handle_exceptions
def create_form_hourlywind(
    data: form_hourlywind_schema.CreateFormHourlyWind,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_hourlywind_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_hourlywind."),
        schema=translate_schema(
            _,
            form_hourlywind_schema.FormHourlyWindResponse.schema()
        )
    )


@router.put("/form_hourlywinds/{station_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def update_form_hourlywind(
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    data: form_hourlywind_schema.UpdateFormHourlyWind,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_hourlywind_service.update(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                mm=mm,
                dd=dd,
                updates=data,
            )
        ],
        message=_("Successfully updated form_hourlywind."),
        schema=translate_schema(
            _,
            form_hourlywind_schema.FormHourlyWindResponse.schema()
        )
    )


@router.delete("/form_hourlywinds/{station_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def delete_form_hourlywind(
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    db_session: Session = Depends(deps.get_session)
):
    form_hourlywind_service.delete(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        mm=mm,
        dd=dd
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_hourlywind."),
        schema=translate_schema(
            _,
            form_hourlywind_schema.FormHourlyWindResponse.schema()
        )
    )
