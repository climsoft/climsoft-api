import logging
from typing import List, Tuple
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import joinedload
from opencdms.models.climsoft import v4_1_1_core as models
from climsoft_api.api.stationlocationhistory import (
    schema as stationlocationhistory_schema,
)
from fastapi.exceptions import HTTPException
from climsoft_api.utils.query import get_count



logger = logging.getLogger("ClimsoftStationLocationHistoryService")
logging.basicConfig(level=logging.INFO)


class FailedCreatingStationLocationHistory(Exception):
    pass


class FailedGettingStationLocationHistory(Exception):
    pass


class FailedGettingStationLocationHistoryList(Exception):
    pass


class FailedUpdatingStationLocationHistory(Exception):
    pass


class FailedDeletingStationLocationHistory(Exception):
    pass


class StationLocationHistoryDoesNotExist(Exception):
    pass


def create(
    db_session: Session,
    data: stationlocationhistory_schema.CreateStationLocationHistory,
) -> stationlocationhistory_schema.StationLocationHistory:
    try:
        station_location_history = models.Stationlocationhistory(**data.dict())
        db_session.add(station_location_history)
        db_session.commit()
        return stationlocationhistory_schema.StationLocationHistory.from_orm(
            station_location_history
        )
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingStationLocationHistory(
            _("Failed creating station location history.")
        )


def get(
    db_session: Session, belongs_to: str, opening_datetime: str
) -> stationlocationhistory_schema.StationLocationHistory:
    try:
        station_location_history = (
            db_session.query(models.Stationlocationhistory)
            .filter_by(belongsTo=belongs_to, openingDatetime=opening_datetime)
            .options(joinedload("station"))
            .first()
        )

        if not station_location_history:
            raise HTTPException(
                status_code=404,
                detail=_("Station location history does not exist.")
            )

        return stationlocationhistory_schema.StationLocationHistoryWithStation\
            .from_orm(
                station_location_history
            )
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingStationLocationHistory(
            _("Failed getting station location history.")
        )


def query(
    db_session: Session,
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
) -> Tuple[int, List[stationlocationhistory_schema.StationLocationHistory]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `station_location_history` row skipping
    `offset` number of rows
    """
    try:
        q = db_session.query(models.Stationlocationhistory)

        if belongs_to is not None:
            q = q.filter_by(belongsTo=belongs_to)

        if station_type is not None:
            q = q.filter_by(stationType=station_type)

        if geolocation_method is not None:
            q = q.filter_by(geoLocationMethod=geolocation_method)

        if geolocation_accuracy is not None:
            q = q.filter_by(geoLocationAccuracy=geolocation_accuracy)

        if opening_datetime is not None:
            q = q.filter_by(openingDatetime=opening_datetime)

        if closing_datetime is not None:
            q = q.filter_by(closingDatetime=closing_datetime)

        if latitude is not None:
            q = q.filter_by(latitude=latitude)

        if longitude is not None:
            q = q.filter_by(longitude=longitude)

        if elevation is not None:
            q = q.filter_by(elevation=elevation)

        if authority is not None:
            q = q.filter_by(authority=authority)

        if admin_region is not None:
            q = q.filter_by(adminRegion=admin_region)

        if drainage_basin is not None:
            q = q.filter_by(drainageBasin=drainage_basin)

        return (
            get_count(q),
            [
                stationlocationhistory_schema.StationLocationHistory.from_orm(s)
                for s in q.offset(offset).limit(limit).all()
            ]
        )
    except Exception as e:
        logger.exception(e)
        raise FailedGettingStationLocationHistoryList(
            _("Failed getting list of station location histories.")
        )


def update(
    db_session: Session,
    belongs_to: str,
    opening_datetime: str,
    updates: stationlocationhistory_schema.UpdateStationLocationHistory,
) -> stationlocationhistory_schema.StationLocationHistory:
    try:
        db_session.query(models.Stationlocationhistory).filter_by(
            belongsTo=belongs_to,
            openingDatetime=opening_datetime
        ).update(updates.dict())
        db_session.commit()
        updated_station_location_history = (
            db_session.query(models.Stationlocationhistory)
            .filter_by(
                belongsTo=belongs_to,
                openingDatetime=opening_datetime
            )
            .first()
        )
        return stationlocationhistory_schema.StationLocationHistory.from_orm(
            updated_station_location_history
        )
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingStationLocationHistory(
            _("Failed updating station location history")
        )


def delete(db_session: Session, belongs_to: str, opening_datetime: str) -> bool:
    try:
        db_session.query(models.Stationlocationhistory).filter_by(
            belongsTo=belongs_to,
            openingDatetime=opening_datetime
        ).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingStationLocationHistory(
            _("Failed deleting station location history.")
        )
