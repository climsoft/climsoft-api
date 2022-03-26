import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.instrumentinspection import (
    schema as instrumentinspection_schema
)
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftInstrumentInspectionService")
logging.basicConfig(level=logging.INFO)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session,
    data: instrumentinspection_schema.CreateInstrumentInspection
) -> instrumentinspection_schema.InstrumentInspection:
    instrument_inspection = models.Instrumentinspection(**data.dict())
    db_session.add(instrument_inspection)
    db_session.commit()
    return instrumentinspection_schema.InstrumentInspection.from_orm(
        instrument_inspection
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(
    db_session: Session, performed_on: str, inspection_datetime: str
) -> instrumentinspection_schema.InstrumentInspection:
    instrument_inspection = (
        db_session.query(models.Instrumentinspection)
        .filter_by(
            performedOn=performed_on,
            inspectionDatetime=inspection_datetime
        )
        .options(joinedload("station"))
            .first()
    )

    if not instrument_inspection:
        raise HTTPException(
            status_code=404,
            detail=_("Instrument inspection does not exist.")
        )

    return instrumentinspection_schema \
        .InstrumentInspectionWithStationAndInstrument.from_orm(
            instrument_inspection
        )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    performed_on: str = None,
    inspection_datetime: str = None,
    performed_by: str = None,
    status: str = None,
    remarks: str = None,
    performed_at: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[instrumentinspection_schema.InstrumentInspection]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `instrument_inspection` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.Instrumentinspection)

    if performed_on is not None:
        q = q.filter_by(performedOn=performed_on)

    if inspection_datetime is not None:
        q = q.filter_by(inspectionDatetime=inspection_datetime)

    if performed_by is not None:
        q = q.filter_by(performedBy=performed_by)

    if status is not None:
        q = q.filter_by(status=status)

    if remarks is not None:
        q = q.filter_by(remarks=remarks)

    if performed_at is not None:
        q = q.filter_by(performedAt=performed_at)

    return (
        get_count(q),
        [
            instrumentinspection_schema.InstrumentInspection.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    performed_on: str,
    inspection_datetime: str,
    updates: instrumentinspection_schema.UpdateInstrumentInspection,
) -> instrumentinspection_schema.InstrumentInspection:
    db_session.query(models.Instrumentinspection).filter_by(
        performedOn=performed_on, inspectionDatetime=inspection_datetime
    ).update(updates.dict())
    db_session.commit()
    updated_instrument_inspection = (
        db_session.query(models.Instrumentinspection)
        .filter_by(
            performedOn=performed_on,
            inspectionDatetime=inspection_datetime
        )
        .first()
    )
    return instrumentinspection_schema.InstrumentInspection.from_orm(
        updated_instrument_inspection
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(
    db_session: Session,
    performed_on: str,
    inspection_datetime: str
) -> bool:
    db_session.query(models.Instrumentinspection).filter_by(
        performedOn=performed_on, inspectionDatetime=inspection_datetime
    ).delete()
    db_session.commit()
    return True
