import climsoft_api.api.form_hourly_time_selection.schema as form_hourly_time_selection_schema
from climsoft_api.api import deps
from climsoft_api.services import form_hourly_time_selection_service
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


@router.get("/form_hourly_time_selections")
@handle_exceptions
def get_form_hourly_time_selections(
    hh: int = None,
    hh_selection: int = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_hourly_time_selections = form_hourly_time_selection_service.query(
        db_session=db_session,
        hh=hh,
        hh_selection=hh_selection,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_hourly_time_selections,
        message=_("Successfully fetched form hourly_time_selections."),
        schema=translate_schema(
            _,
            form_hourly_time_selection_schema.FormHourlyTimeSelectionQueryResponse.schema()
        )
    )


@router.get("/form_hourly_time_selections/{hh}")
@handle_exceptions
def get_form_hourly_time_selection_by_id(
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_hourly_time_selection_service.get(
                db_session=db_session,
                hh=hh
            )
        ],
        message=_("Successfully fetched form_hourly_time_selection."),
        schema=translate_schema(
            _,
            form_hourly_time_selection_schema.FormHourlyTimeSelectionResponse.schema()
        )
    )


@router.get(
    "/form_hourly_time_selections/search"
)
@handle_exceptions
def search_elements(
    query: str = None,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, form_hourly_time_selections = form_hourly_time_selection_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_hourly_time_selections,
        message=_("Successfully fetched forms."),
        schema=translate_schema(
            _,
            form_hourly_time_selection_schema.FormHourlyTimeSelectionQueryResponse.schema()
        )
    )


@router.post("/form_hourly_time_selections")
@handle_exceptions
def create_form_hourly_time_selection(
    data: form_hourly_time_selection_schema.CreateFormHourlyTimeSelection,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_hourly_time_selection_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_hourly_time_selection."),
        schema=translate_schema(
            _,
            form_hourly_time_selection_schema.FormHourlyTimeSelectionResponse.schema()
        )
    )


@router.put("/form_hourly_time_selections/{hh}")
@handle_exceptions
def update_form_hourly_time_selection(
    hh: int,
    data: form_hourly_time_selection_schema.UpdateFormHourlyTimeSelection,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_hourly_time_selection_service.update(
                db_session=db_session,
                hh=hh,
                updates=data,
            )
        ],
        message=_("Successfully updated form_hourly_time_selection."),
        schema=translate_schema(
            _,
            form_hourly_time_selection_schema.FormHourlyTimeSelectionResponse.schema()
        )
    )


@router.delete("/form_hourly_time_selections/{hh}")
@handle_exceptions
def delete_form_hourly_time_selection(
    hh: int,
    db_session: Session = Depends(deps.get_session)
):
    form_hourly_time_selection_service.delete(
        db_session=db_session,
        hh=hh
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_hourly_time_selection."),
        schema=translate_schema(
            _,
            form_hourly_time_selection_schema.FormHourlyTimeSelectionResponse.schema()
        )
    )
