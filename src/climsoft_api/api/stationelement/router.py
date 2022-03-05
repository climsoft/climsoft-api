from fastapi import APIRouter, Depends
from climsoft_api.services import stationelement_service
import climsoft_api.api.stationelement.schema as stationelement_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps




router = APIRouter()


@router.get(
    "/",
    response_model=stationelement_schema.StationElementQueryResponse
)
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
    try:
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
            message=_("Successfully fetched station elements.")
        )
    except stationelement_service.FailedGettingStationElementList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{recorded_from}/{described_by}/{recorded_with}/{begin_date}",
    response_model=stationelement_schema.StationElementWithChildrenResponse,
)
def get_station_element_by_id(
    recorded_from: str,
    described_by: int,
    recorded_with: str,
    begin_date: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
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
        )
    except stationelement_service.FailedGettingStationElement as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=stationelement_schema.StationElementResponse)
def create_station_element(
    data: stationelement_schema.CreateStationElement,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[stationelement_service.create(db_session=db_session, data=data)],
            message=_("Successfully created station element."),
        )
    except stationelement_service.FailedCreatingStationElement as e:
        return get_error_response(message=str(e))


@router.put(
    "/{recorded_from}/{described_by}/{recorded_with}/{begin_date}",
    response_model=stationelement_schema.StationElementResponse,
)
def update_station_element(
    recorded_from: str,
    described_by: int,
    recorded_with: str,
    begin_date: str,
    data: stationelement_schema.UpdateStationElement,
    db_session: Session = Depends(deps.get_session),
):
    try:
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
        )
    except stationelement_service.FailedUpdatingStationElement as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{recorded_from}/{described_by}/{recorded_with}/{begin_date}",
    response_model=stationelement_schema.StationElementResponse,
)
def delete_station_element(
    recorded_from: str,
    described_by: int,
    recorded_with: str,
    begin_date: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        stationelement_service.delete(
            db_session=db_session,
            recorded_from=recorded_from,
            recorded_with=recorded_with,
            described_by=described_by,
            begin_date=begin_date,
        )
        return get_success_response(
            result=[], message=_("Successfully deleted station element.")
        )
    except stationelement_service.FailedDeletingStationElement as e:
        return get_error_response(message=str(e))
