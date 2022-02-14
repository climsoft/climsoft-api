from fastapi import APIRouter, Depends
from climsoft_api.services import station_service
import climsoft_api.api.station.schema as station_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get("/", response_model=station_schema.StationQueryResponse)
def get_stations(
    station_id: str = None,
    station_name: str = None,
    wmoid: str = None,
    icaoid: str = None,
    latitude: float = None,
    longitude: float = None,
    qualifier: str = None,
    elevation: str = None,
    geolocation_method: str = None,
    geolocation_accuracy: str = None,
    opening_datetime: str = None,
    closing_datetime: str = None,
    country: str = None,
    authority: str = None,
    admin_region: str = None,
    drainage_basin: str = None,
    waca_selection: bool = None,
    cpt_selection: bool = None,
    station_operational: bool = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, stations = station_service.query(
            db_session=db_session,
            station_id=station_id,
            station_name=station_name,
            wmoid=wmoid,
            icaoid=icaoid,
            latitude=latitude,
            longitude=longitude,
            qualifier=qualifier,
            elevation=elevation,
            geolocation_method=geolocation_method,
            geolocation_accuracy=geolocation_accuracy,
            opening_datetime=opening_datetime,
            closing_datetime=closing_datetime,
            country=country,
            authority=authority,
            admin_region=admin_region,
            drainage_basin=drainage_basin,
            waca_selection=waca_selection,
            cpt_selection=cpt_selection,
            station_operational=station_operational,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=stations, message="Successfully fetched stations."
        )
    except station_service.FailedGettingStationList as e:
        return get_error_response(message=str(e))


@router.get("/{station_id}", response_model=station_schema.StationResponse)
def get_station_by_id(station_id: str, db_session: Session = Depends(deps.get_session)):
    try:
        return get_success_response(
            result=[station_service.get(db_session=db_session, station_id=station_id)],
            message="Successfully fetched station.",
        )
    except station_service.FailedGettingStation as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=station_schema.StationResponse)
def create_station(
    data: station_schema.CreateStation, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[station_service.create(db_session=db_session, data=data)],
            message="Successfully created station.",
        )
    except station_service.FailedCreatingStation as e:
        return get_error_response(message=str(e))


@router.put("/{station_id}", response_model=station_schema.StationResponse)
def update_station(
    station_id: str,
    data: station_schema.UpdateStation,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                station_service.update(
                    db_session=db_session, station_id=station_id, updates=data
                )
            ],
            message="Successfully updated station.",
        )
    except station_service.FailedUpdatingStation as e:
        return get_error_response(message=str(e))


@router.delete("/{station_id}", response_model=station_schema.StationResponse)
def delete_station(station_id: str, db_session: Session = Depends(deps.get_session)):
    try:
        station_service.delete(db_session=db_session, station_id=station_id)
        return get_success_response(result=[], message="Successfully deleted station.")
    except station_service.FailedDeletingStation as e:
        return get_error_response(message=str(e))
