import climsoft_api.api.form_daily2.schema as form_daily2_schema
from climsoft_api.api import deps
from climsoft_api.services import form_daily2_service
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


@router.get("/form_daily2s")
@handle_exceptions
def get_form_daily2s(
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
    db_session: Session = Depends(deps.get_session),
):
    total, form_daily2s = form_daily2_service.query(
        db_session=db_session,
        station_id=station_id,
        element_id=element_id,
        yyyy=yyyy,
        mm=mm,
        hh=hh,
        total=total,
        signature=signature,
        entry_datetime=entry_datetime,
        temperature_units=temperature_units,
        precip_units=precip_units,
        cloud_height_units=cloud_height_units,
        vis_units=vis_units,
        day01=day01,
        day02=day02,
        day03=day03,
        day04=day04,
        day05=day05,
        day06=day06,
        day07=day07,
        day08=day08,
        day09=day09,
        day10=day10,
        day11=day11,
        day12=day12,
        day13=day13,
        day14=day14,
        day15=day15,
        day16=day16,
        day17=day17,
        day18=day18,
        day19=day19,
        day20=day20,
        day21=day21,
        day22=day22,
        day23=day23,
        day24=day24,
        day25=day25,
        day26=day26,
        day27=day27,
        day28=day28,
        day29=day29,
        day30=day30,
        day31=day31,
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
        period01=period01,
        period02=period02,
        period03=period03,
        period04=period04,
        period05=period05,
        period06=period06,
        period07=period07,
        period08=period08,
        period09=period09,
        period10=period10,
        period11=period11,
        period12=period12,
        period13=period13,
        period14=period14,
        period15=period15,
        period16=period16,
        period17=period17,
        period18=period18,
        period19=period19,
        period20=period20,
        period21=period21,
        period22=period22,
        period23=period23,
        period24=period24,
        period25=period25,
        period26=period26,
        period27=period27,
        period28=period28,
        period29=period29,
        period30=period30,
        period31=period31,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_daily2s,
        message=_("Successfully fetched form_daily2s."),
        schema=translate_schema(
            _,
            form_daily2_schema.FormDaily2QueryResponse.schema()
        )
    )


@router.get("/form_daily2s/{station_id}/{element_id}/{yyyy}/{mm}/{hh}")
@handle_exceptions
def get_form_daily2_by_id(
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_daily2_service.get(
                db_session=db_session,
                station_id=station_id,
                element_id=element_id,
                yyyy=yyyy,
                mm=mm,
                hh=hh
            )
        ],
        message=_("Successfully fetched form_daily2."),
        schema=translate_schema(
            _,
            form_daily2_schema.FormDaily2Response.schema()
        )
    )


@router.get(
    "/form_daily2s/search"
)
@handle_exceptions
def search_elements(
    query: str = None,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, form_daily2s = form_daily2_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_daily2s,
        message=_("Successfully fetched forms."),
        schema=translate_schema(
            _,
            form_daily2_schema.FormDaily2QueryResponse.schema()
        )
    )


@router.post("/form_daily2s")
@handle_exceptions
def create_form_daily2(
    data: form_daily2_schema.CreateFormDaily2,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_daily2_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_daily2."),
        schema=translate_schema(
            _,
            form_daily2_schema.FormDaily2Response.schema()
        )
    )


@router.put("/form_daily2s/{station_id}/{element_id}/{yyyy}/{mm}/{hh}")
@handle_exceptions
def update_form_daily2(
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    hh: int,
    data: form_daily2_schema.UpdateFormDaily2,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_daily2_service.update(
                db_session=db_session,
                station_id=station_id,
                element_id=element_id,
                yyyy=yyyy,
                mm=mm,
                hh=hh,
                updates=data,
            )
        ],
        message=_("Successfully updated form_daily2."),
        schema=translate_schema(
            _,
            form_daily2_schema.FormDaily2Response.schema()
        )
    )


@router.delete("/form_daily2s/{station_id}/{element_id}/{yyyy}/{mm}/{hh}")
@handle_exceptions
def delete_form_daily2(
    station_id: str,
    element_id: int,
    yyyy: int,
    mm: int,
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    form_daily2_service.delete(
        db_session=db_session,
        station_id=station_id,
        element_id=element_id,
        yyyy=yyyy,
        mm=mm,
        hh=hh
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_daily2."),
        schema=translate_schema(
            _,
            form_daily2_schema.FormDaily2Response.schema()
        )
    )
