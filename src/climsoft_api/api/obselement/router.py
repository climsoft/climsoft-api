import climsoft_api.api.obselement.schema as obselement_schema
from climsoft_api.api.stationelement import schema as stationelement_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import obselement_service, stationelement_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging
from climsoft_api.utils.exception import handle_exceptions


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get("/obselements")
@handle_exceptions
def get_obselements(
    element_id: str = None,
    element_name: str = None,
    abbreviation: str = None,
    description: str = None,
    element_scale: float = None,
    upper_limit: float = None,
    lower_limit: str = None,
    units: str = None,
    element_type: str = None,
    qc_total_required: int = None,
    selected: bool = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, obselements = obselement_service.query(
        db_session=db_session,
        element_id=element_id,
        element_name=element_name,
        abbreviation=abbreviation,
        description=description,
        element_scale=element_scale,
        upper_limit=upper_limit,
        lower_limit=lower_limit,
        units=units,
        element_type=element_type,
        qc_total_required=qc_total_required,
        selected=selected,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=obselements,
        message=_("Successfully fetched obs elements."),
        schema=translate_schema(
            _,
            obselement_schema.ObsElementQueryResponse.schema()
        )
    )


@router.get(
    "/elements/search",
    tags=["Elements", "Obselements", "Station Elements"]
)
@handle_exceptions
def search_elements(
    query: str = None,
    time_period: str = None,
    station_id: str = None,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    if station_id is not None:
        total, station_elements = stationelement_service.query(
            db_session=db_session,
            recorded_from=station_id,
            limit=limit,
            offset=offset
        )
        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=station_elements,
            message=_("Successfully fetched station elements."),
            schema=translate_schema(
                _,
                stationelement_schema.StationElementQueryResponse.schema()
            )
        )

    total, obs_elements = obselement_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset,
        time_period=time_period
    )
    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=obs_elements,
        message=_("Successfully fetched obs elements."),
        schema=translate_schema(
            _,
            obselement_schema.ObsElementQueryResponse.schema()
        )
    )


@router.get(
    "/obselements/{element_id}"
)
@handle_exceptions
def get_obs_element_by_id(
    element_id: str,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            obselement_service.get(
                db_session=db_session,
                element_id=element_id
            )
        ],
        message=_("Successfully fetched obs element."),
        schema=translate_schema(
            _,
            obselement_schema.ObsElementResponse.schema()
        )
    )


@router.post("/obselements")
@handle_exceptions
def create_obs_element(
    data: obselement_schema.CreateObsElement,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[obselement_service.create(
            db_session=db_session,
            data=data
        )],
        message=_("Successfully created obs element."),
        schema=translate_schema(
            _,
            obselement_schema.ObsElementResponse.schema()
        )
    )


@router.put(
    "/obselements/{element_id}"
)
@handle_exceptions
def update_obs_element(
    element_id: str,
    data: obselement_schema.UpdateObsElement,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            obselement_service.update(
                db_session=db_session,
                element_id=element_id,
                updates=data
            )
        ],
        message=_("Successfully updated obs element."),
        schema=translate_schema(
            _,
            obselement_schema.ObsElementResponse.schema()
        )
    )


@router.delete(
    "/obselements/{element_id}"
)
@handle_exceptions
def delete_obs_element(
    element_id: str,
    db_session: Session = Depends(deps.get_session)
):
    obselement_service.delete(
        db_session=db_session,
        element_id=element_id
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted obs element."),
        schema=translate_schema(
            _,
            obselement_schema.ObsElementResponse.schema()
        )
    )
