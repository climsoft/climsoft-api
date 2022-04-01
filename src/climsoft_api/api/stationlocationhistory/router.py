import \
    climsoft_api.api.stationlocationhistory.schema as stationlocationhistory_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import stationlocationhistory_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get(
    "/station-location-histories",
)
def get_station_location_history(
    belongs_to: str = None,
    station_type: str = None,
    geolocation_method: str = None,
    geolocation_accuracy: float = None,
    opening_datetime: str = None,
    closing_datetime: str = None,
    latitude: float = None,
    longitude: float = None,
    elevation: int = None,
    authority: str = None,
    admin_region: str = None,
    drainage_basin: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, station_location_history = stationlocationhistory_service.query(
            db_session=db_session,
            belongs_to=belongs_to,
            station_type=station_type,
            geolocation_method=geolocation_method,
            geolocation_accuracy=geolocation_accuracy,
            opening_datetime=opening_datetime,
            closing_datetime=closing_datetime,
            latitude=latitude,
            longitude=longitude,
            elevation=elevation,
            authority=authority,
            admin_region=admin_region,
            drainage_basin=drainage_basin,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=station_location_history,
            message=_("Successfully fetched station location history."),
            schema=translate_schema(
                _,
                stationlocationhistory_schema.StationLocationHistoryQueryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.get(
    "/station-location-histories/{belongs_to}/{opening_datetime}"
)
def get_station_location_history_by_id(
    belongs_to: str,
    opening_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                stationlocationhistory_service.get(
                    db_session=db_session,
                    belongs_to=belongs_to,
                    opening_datetime=opening_datetime,
                )
            ],
            message=_("Successfully fetched station location history."),
            schema=translate_schema(
                _,
                stationlocationhistory_schema.StationLocationHistoryWithStationResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.post(
    "/station-location-histories",
)
def create_station_location_history(
    data: stationlocationhistory_schema.CreateStationLocationHistory,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                stationlocationhistory_service.create(db_session=db_session,
                                                      data=data)
            ],
            message=_("Successfully created station location history."),
            schema=translate_schema(
                _,
                stationlocationhistory_schema.StationLocationHistoryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.put(
    "/station-location-histories/{belongs_to}/{opening_datetime}"
)
def update_station_location_history(
    belongs_to: str,
    opening_datetime: str,
    data: stationlocationhistory_schema.UpdateStationLocationHistory,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                stationlocationhistory_service.update(
                    db_session=db_session,
                    belongs_to=belongs_to,
                    opening_datetime=opening_datetime,
                    updates=data,
                )
            ],
            message=_("Successfully updated station location history."),
            schema=translate_schema(
                _,
                stationlocationhistory_schema.StationLocationHistoryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.delete(
    "/station-location-histories/{belongs_to}/{opening_datetime}"
)
def delete_station_location_history(
    belongs_to: str,
    opening_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        stationlocationhistory_service.delete(
            db_session=db_session,
            belongs_to=belongs_to,
            opening_datetime=opening_datetime,
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted station location history."),
            schema=translate_schema(
                _,
                stationlocationhistory_schema.StationLocationHistoryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )
