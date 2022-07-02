import climsoft_api.api.form_agro1.schema as form_agro1_schema
from climsoft_api.api import deps
from climsoft_api.services import form_agro1_service
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


@router.get("/form_agro1s")
@handle_exceptions
def get_form_agro1s(
    station_id: str = None,
    yyyy: int = None,
    mm: int = None,
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
    entry_datetime: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, form_agro1s = form_agro1_service.query(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        mm=mm,
        entry_datetime=entry_datetime,
        val_elem101=val_elem101,
        val_elem102=val_elem102,
        val_elem103=val_elem103,
        val_elem105=val_elem105,
        val_elem002=val_elem002,
        val_elem003=val_elem003,
        val_elem099=val_elem099,
        val_elem072=val_elem072,
        val_elem073=val_elem073,
        val_elem074=val_elem074,
        val_elem554=val_elem554,
        val_elem075=val_elem075,
        val_elem076=val_elem076,
        val_elem561=val_elem561,
        val_elem562=val_elem562,
        val_elem563=val_elem563,
        val_elem513=val_elem513,
        val_elem005=val_elem005,
        val_elem504=val_elem504,
        val_elem532=val_elem532,
        val_elem137=val_elem137,
        val_elem018=val_elem018,
        val_elem518=val_elem518,
        val_elem511=val_elem511,
        val_elem512=val_elem512,
        val_elem503=val_elem503,
        val_elem515=val_elem515,
        val_elem564=val_elem564,
        val_elem565=val_elem565,
        val_elem566=val_elem566,
        val_elem531=val_elem531,
        val_elem530=val_elem530,
        val_elem541=val_elem541,
        val_elem542=val_elem542,
        flag101=flag101,
        flag102=flag102,
        flag103=flag103,
        flag105=flag105,
        flag002=flag002,
        flag003=flag003,
        flag099=flag099,
        flag072=flag072,
        flag073=flag073,
        flag074=flag074,
        flag554=flag554,
        flag075=flag075,
        flag076=flag076,
        flag561=flag561,
        flag562=flag562,
        flag563=flag563,
        flag513=flag513,
        flag005=flag005,
        flag504=flag504,
        flag532=flag532,
        flag137=flag137,
        flag018=flag018,
        flag518=flag518,
        flag511=flag511,
        flag512=flag512,
        flag503=flag503,
        flag515=flag515,
        flag564=flag564,
        flag565=flag565,
        flag566=flag566,
        flag531=flag531,
        flag530=flag530,
        flag541=flag541,
        flag542=flag542,
        limit=limit,
        offset=offset
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_agro1s,
        message=_("Successfully fetched form agro1s."),
        schema=translate_schema(
            _,
            form_agro1_schema.FormAgro1QueryResponse.schema()
        )
    )


@router.get("/form_agro1s/{station_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def get_form_agro1_by_id(
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            form_agro1_service.get(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                mm=mm,
                dd=dd
            )
        ],
        message=_("Successfully fetched form_agro1."),
        schema=translate_schema(
            _,
            form_agro1_schema.FormAgro1Response.schema()
        )
    )


@router.get(
    "/form_agro1s/search"
)
@handle_exceptions
def search_elements(
    query: str = None,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, form_agro1s = form_agro1_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=form_agro1s,
        message=_("Successfully fetched forms."),
        schema=translate_schema(
            _,
            form_agro1_schema.FormAgro1QueryResponse.schema()
        )
    )


@router.post("/form_agro1s")
@handle_exceptions
def create_form_agro1(
    data: form_agro1_schema.CreateFormAgro1,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[form_agro1_service.create(db_session=db_session, data=data)],
        message=_("Successfully created form_agro1."),
        schema=translate_schema(
            _,
            form_agro1_schema.FormAgro1Response.schema()
        )
    )


@router.put("/form_agro1s/{station_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def update_form_agro1(
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    data: form_agro1_schema.UpdateFormAgro1,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            form_agro1_service.update(
                db_session=db_session,
                station_id=station_id,
                yyyy=yyyy,
                mm=mm,
                dd=dd,
                updates=data,
            )
        ],
        message=_("Successfully updated form_agro1."),
        schema=translate_schema(
            _,
            form_agro1_schema.FormAgro1Response.schema()
        )
    )


@router.delete("/form_agro1s/{station_id}/{yyyy}/{mm}/{dd}")
@handle_exceptions
def delete_form_agro1(
    station_id: str,
    yyyy: int,
    mm: int,
    dd: int,
    db_session: Session = Depends(deps.get_session)
):
    form_agro1_service.delete(
        db_session=db_session,
        station_id=station_id,
        yyyy=yyyy,
        mm=mm,
        dd=dd
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted form_agro1."),
        schema=translate_schema(
            _,
            form_agro1_schema.FormAgro1Response.schema()
        )
    )
