import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.stationqualifier import schema as stationqualifier_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftStationQualifierService")
logging.basicConfig(level=logging.INFO)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: stationqualifier_schema.CreateStationQualifier
) -> stationqualifier_schema.StationQualifier:
    station_qualifier = models.Stationqualifier(**data.dict())
    db_session.add(station_qualifier)
    db_session.commit()
    return stationqualifier_schema.StationQualifier.from_orm(
        station_qualifier
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(
    db_session: Session,
    qualifier: str,
    qualifier_begin_date: str,
    qualifier_end_date: str,
    belongs_to: str,
) -> stationqualifier_schema.StationQualifier:
    station_qualifier = (
        db_session.query(models.Stationqualifier)
        .filter_by(
            qualifier=qualifier,
            qualifierBeginDate=qualifier_begin_date,
            qualifierEndDate=qualifier_end_date,
            belongsTo=belongs_to,
        )
        .options(joinedload("station"))
        .first()
    )

    if not station_qualifier:
        raise HTTPException(
            status_code=404,
            detail=_("Station qualifier does not exist.")
        )

    return stationqualifier_schema.StationQualifierWithStation.from_orm(
        station_qualifier
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    qualifier: str = None,
    qualifier_begin_date: str = None,
    qualifier_end_date: str = None,
    station_timezone: int = None,
    station_network_type: str = None,
    belongs_to: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[stationqualifier_schema.StationQualifier]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `station_qualifier` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.Stationqualifier)

    if qualifier is not None:
        q = q.filter_by(qualifier=qualifier)

    if qualifier_begin_date is not None:
        q = q.filter_by(qualifierBeginDate=qualifier_begin_date)

    if qualifier_end_date is not None:
        q = q.filter_by(qualifierEndDate=qualifier_end_date)

    if station_timezone is not None:
        q = q.filter_by(stationTimeZone=station_timezone)

    if station_network_type is not None:
        q = q.filter_by(stationNetworkType=station_network_type)

    if belongs_to is not None:
        q = q.filter_by(belongsTo=belongs_to)

    return (
        get_count(q),
        [
            stationqualifier_schema.StationQualifier.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    qualifier: str,
    qualifier_begin_date: str,
    qualifier_end_date: str,
    belongs_to: str,
    updates: stationqualifier_schema.UpdateStationQualifier,
) -> stationqualifier_schema.StationQualifier:
    db_session.query(models.Stationqualifier).filter_by(
        qualifier=qualifier,
        qualifierBeginDate=qualifier_begin_date,
        qualifierEndDate=qualifier_end_date,
        belongsTo=belongs_to,
    ).update(updates.dict())
    db_session.commit()
    updated_station_qualifier = (
        db_session.query(models.Stationqualifier)
            .filter_by(
            qualifier=qualifier,
            qualifierBeginDate=qualifier_begin_date,
            qualifierEndDate=qualifier_end_date,
            belongsTo=belongs_to,
        )
        .first()
    )
    return stationqualifier_schema.StationQualifier.from_orm(
        updated_station_qualifier
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(
    db_session: Session,
    qualifier: str,
    qualifier_begin_date: str,
    qualifier_end_date: str,
    belongs_to: str,
) -> bool:
    db_session.query(models.Stationqualifier).filter_by(
        qualifier=qualifier,
        qualifierBeginDate=qualifier_begin_date,
        qualifierEndDate=qualifier_end_date,
        belongsTo=belongs_to,
    ).delete()
    db_session.commit()
    return True
