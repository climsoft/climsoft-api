import climsoft_api.api.form_monthly.schema as form_monthly_schema
from climsoft_api.api import deps
from climsoft_api.services import form_monthly_service
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


@router.get("/form_monthlys")
@handle_exceptions
def get_form_monthlys(
    station_id: str = None,
    element_id: int = None,
    yyyy: int = None,
    mm_01: str = None,
    mm_02: str = None,
    mm_03: str = None,
    mm_04: str = None,
    mm_05: str = None,
    mm_06: str = None,
    mm_07: str = None,
    mm_08: str = None,
    mm_09: str = None,
    mm_10: str = None,
    mm_11: str = None,
    mm_12: str = None,
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
    signature: str = None,
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_monthlys = form_monthly_service.query(
        db_session=db_session,
        station_id=station_id,
        element_id=element_id,
        yyyy=yyyy,
        signature=signature,
        entry_datetime=entry_datetime,
        mm_01=mm_01,
        mm_02=mm_02,
        mm_03=mm_03,
        mm_04=mm_04,
        mm_05=mm_05,
        mm_06=mm_06,
        mm_07=mm_07,
        mm_08=mm_08,
        mm_09=mm_09,
        mm_10=mm_10,
        mm_11=mm_11,
        mm_12=mm_12,
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
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_monthlys,
        message=_("Successfully fetched form_monthlys."),
        schema=translate_schema(
            _,
            form_monthly_schema.FormMonthlyQueryResponse.schema()
        )
    )


@router.get("/form_monthlys/{station_id}/{element_id}/{yyyy}")
@handle_exceptions
def get_form_monthly_by_id(
    station_id: str,
    element_id: int,
    yyyy: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_monthly_service.get(
                db_session=db_session,
                station_id=station_id,
                element_id=element_id,
                yyyy=yyyy
            )
        ],
        message=_("Successfully fetched form_monthly."),
        schema=translate_schema(
            _,
            form_monthly_schema.FormMonthlyResponse.schema()
        )
    )


@router.get(
    "/form_monthlys/search"
)
@handle_exceptions
def search_elements(
    query: str = None,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, form_monthlys = form_monthly_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_monthlys,
        message=_("Successfully fetched forms."),
        schema=translate_schema(
            _,
            form_monthly_schema.FormMonthlyQueryResponse.schema()
        )
    )


@router.post("/form_monthlys")
@handle_exceptions
def create_form_monthly(
    data: form_monthly_schema.CreateFormMonthly,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_monthly_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_monthly."),
        schema=translate_schema(
            _,
            form_monthly_schema.FormMonthlyResponse.schema()
        )
    )


@router.put("/form_monthlys/{station_id}/{element_id}/{yyyy}")
@handle_exceptions
def update_form_monthly(
    station_id: str,
    element_id: int,
    yyyy: int,
    data: form_monthly_schema.UpdateFormMonthly,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_monthly_service.update(
                db_session=db_session,
                station_id=station_id,
                element_id=element_id,
                yyyy=yyyy,
                updates=data,
            )
        ],
        message=_("Successfully updated form_monthly."),
        schema=translate_schema(
            _,
            form_monthly_schema.FormMonthlyResponse.schema()
        )
    )


@router.delete("/form_monthlys/{station_id}/{element_id}/{yyyy}")
@handle_exceptions
def delete_form_monthly(
    station_id: str,
    element_id: int,
    yyyy: int,
    db_session: Session = Depends(deps.get_session)
):
    form_monthly_service.delete(
        db_session=db_session,
        station_id=station_id,
        element_id=element_id,
        yyyy=yyyy
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_monthly."),
        schema=translate_schema(
            _,
            form_monthly_schema.FormMonthlyResponse.schema()
        )
    )
