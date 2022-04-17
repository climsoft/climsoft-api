import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.faultresolution import schema as faultresolution_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFaultResolutionService")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session,
    resolved_datetime: str,
    associated_with: str
):
    fault_resolution = (
        db_session.query(models.Faultresolution)
        .filter_by(
            resolvedDatetime=resolved_datetime,
            associatedWith=associated_with
        )
        .first()
    )

    if not fault_resolution:
        raise HTTPException(
            status_code=404, detail=_("Fault resolution does not exist.")
        )

    return fault_resolution


def create(
    db_session: Session, data: faultresolution_schema.CreateFaultResolution
) -> faultresolution_schema.FaultResolution:
    fault_resolution = models.Faultresolution(**data.dict())
    db_session.add(fault_resolution)
    db_session.commit()
    return faultresolution_schema.FaultResolution.from_orm(fault_resolution)


def get(
    db_session: Session, resolved_datetime: str, associated_with: str
) -> faultresolution_schema.FaultResolution:
    fault_resolution = (
        db_session.query(models.Faultresolution)
        .filter_by(
            resolvedDatetime=resolved_datetime,
            associatedWith=associated_with
        )
        .options(joinedload("instrumentfaultreport"))
        .first()
    )

    if not fault_resolution:
        raise HTTPException(
            status_code=404, detail=_("Fault resolution does not exist.")
        )

    return faultresolution_schema.FaultResolutionWithInstrumentFaultReport \
        .from_orm(
            fault_resolution
        )


def query(
    db_session: Session,
    resolved_datetime: str = None,
    associated_with: str = None,
    remarks: str = None,
    resolved_by: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[faultresolution_schema.FaultResolution]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `fault_resolution` row skipping
    `offset` number of rows
    """

    q = db_session.query(models.Faultresolution)

    if resolved_datetime is not None:
        q = q.filter_by(resolvedDatetime=resolved_datetime)

    if associated_with is not None:
        q = q.filter_by(associatedWith=associated_with)

    if resolved_by is not None:
        q = q.filter_by(resolvedBy=resolved_by)

    if remarks is not None:
        q = q.filter_by(remarks=remarks)

    return (
        get_count(q),
        [
            faultresolution_schema.FaultResolution.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    resolved_datetime: str,
    associated_with: str,
    updates: faultresolution_schema.UpdateFaultResolution,
) -> faultresolution_schema.FaultResolution:
    get_or_404(db_session, resolved_datetime, associated_with)
    db_session.query(models.Faultresolution).filter_by(
        resolvedDatetime=resolved_datetime,
        associatedWith=associated_with
    ).update(updates.dict())
    db_session.commit()
    updated_fault_resolution = (
        db_session.query(models.Faultresolution)
        .filter_by(
            resolvedDatetime=resolved_datetime,
            associatedWith=associated_with
        )
        .first()
    )
    return faultresolution_schema.FaultResolution.from_orm(
        updated_fault_resolution
    )


def delete(
    db_session: Session,
    resolved_datetime: str,
    associated_with: str
) -> bool:
    get_or_404(db_session, resolved_datetime, associated_with)
    db_session.query(models.Faultresolution).filter_by(
        resolvedDatetime=resolved_datetime,
        associatedWith=associated_with
    ).delete()
    db_session.commit()
    return True
