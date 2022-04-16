import climsoft_api.api.stationelement.schema as stationelement_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import stationelement_service
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


@router.get(
    "/station-elements"
)
@handle_exceptions
def get_station_elements(
    recorded_from: str = None,
    described_by: int = None,
    recorded_with: str = None,
    instrument_code: str = None,
    scheduled_for: str = None,
    height: int = None,
    begin_date: float = None,
    end_date: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, station_elements = stationelement_service.query(
        db_session=db_session,
        recorded_from=recorded_from,
        recorded_with=recorded_with,
        described_by=described_by,
        instrument_code=instrument_code,
        scheduled_for=scheduled_for,
        begin_date=begin_date,
        end_date=end_date,
        height=height,
        limit=limit,
        offset=offset,
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


@router.get(
    "/station-elements/search"
)
@handle_exceptions
def search_station_elements(
    query: str,
    db_session: Session = Depends(deps.get_session),
    limit: int = 25,
    offset: int = 0
):
    total, station_elements = stationelement_service.search(
        db_session=db_session,
        _query=query,
        limit=limit,
        offset=offset,
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


@router.get(
    "/station-elements/{recorded_from}/{described_by}/{recorded_with}/{begin_date}"
)
@handle_exceptions
def get_station_element_by_id(
    recorded_from: str,
    described_by: int,
    recorded_with: str,
    begin_date: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            stationelement_service.get(
                db_session=db_session,
                recorded_from=recorded_from,
                recorded_with=recorded_with,
                described_by=described_by,
                begin_date=begin_date,
            )
        ],
        message=_("Successfully fetched station element."),
        schema=translate_schema(
            _,
            stationelement_schema.StationElementWithChildrenResponse.schema()
        )
    )


@router.post("/station-elements")
@handle_exceptions
def create_station_element(
    data: stationelement_schema.CreateStationElement,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[stationelement_service.create(db_session=db_session,
                                              data=data)],
        message=_("Successfully created station element."),
        schema=translate_schema(
            _,
            stationelement_schema.StationElementResponse.schema()
        )
    )


@router.put(
    "/station-elements/{recorded_from}/{described_by}/{recorded_with}/{begin_date}"
)
@handle_exceptions
def update_station_element(
    recorded_from: str,
    described_by: int,
    recorded_with: str,
    begin_date: str,
    data: stationelement_schema.UpdateStationElement,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            stationelement_service.update(
                db_session=db_session,
                recorded_from=recorded_from,
                recorded_with=recorded_with,
                described_by=described_by,
                begin_date=begin_date,
                updates=data,
            )
        ],
        message=_("Successfully updated station element."),
        schema=translate_schema(
            _,
            stationelement_schema.StationElementResponse.schema()
        )
    )


@router.delete(
    "/station-elements/{recorded_from}/{described_by}/{recorded_with}/{begin_date}"
)
@handle_exceptions
def delete_station_element(
    recorded_from: str,
    described_by: int,
    recorded_with: str,
    begin_date: str,
    db_session: Session = Depends(deps.get_session),
):
    stationelement_service.delete(
        db_session=db_session,
        recorded_from=recorded_from,
        recorded_with=recorded_with,
        described_by=described_by,
        begin_date=begin_date,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted station element."),
        schema=translate_schema(
            _,
            stationelement_schema.StationElementResponse.schema()
        )
    )
