import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.physicalfeature import schema as physicalfeature_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftPhysicalFeatureService")
logging.basicConfig(level=logging.INFO)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: physicalfeature_schema.CreatePhysicalFeature
) -> physicalfeature_schema.PhysicalFeature:
    physical_feature = models.Physicalfeature(**data.dict())
    db_session.add(physical_feature)
    db_session.commit()
    return physicalfeature_schema.PhysicalFeature.from_orm(physical_feature)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(
    db_session: Session,
    associated_with: str,
    begin_date: str,
    classified_into: str,
    description: str,
) -> physicalfeature_schema.PhysicalFeature:
    physical_feature = (
        db_session.query(models.Physicalfeature)
            .filter_by(
            associatedWith=associated_with,
            beginDate=begin_date,
            classifiedInto=classified_into,
            description=description,
        )
            .options(joinedload("station"))
            .first()
    )

    if not physical_feature:
        raise HTTPException(
            status_code=404,
            detail=_("Physical feature does not exist.")
        )

    return physicalfeature_schema \
        .PhysicalFeatureWithStationAndPhysicalFeatureClass.from_orm(
            physical_feature
        )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    associated_with: str = None,
    begin_date: str = None,
    end_date: str = None,
    image: str = None,
    description: str = None,
    classified_into: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[physicalfeature_schema.PhysicalFeature]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `physical_feature` row skipping
    `offset` number of rows
    """
    q = db_session.query(models.Physicalfeature)

    if associated_with is not None:
        q = q.filter_by(associatedWith=associated_with)

    if begin_date is not None:
        q = q.filter_by(beginDate=begin_date)

    if end_date is not None:
        q = q.filter_by(endDate=end_date)

    if image is not None:
        q = q.filter_by(image=image)

    if description is not None:
        q = q.filter_by(description=description)

    if classified_into is not None:
        q = q.filter_by(classifiedInto=classified_into)

    return (
        get_count(q),
        [
            physicalfeature_schema.PhysicalFeature.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    associated_with: str,
    begin_date: str,
    classified_into: str,
    description: str,
    updates: physicalfeature_schema.UpdatePhysicalFeature,
) -> physicalfeature_schema.PhysicalFeature:
    db_session.query(models.Physicalfeature).filter_by(
        associatedWith=associated_with,
        beginDate=begin_date,
        classifiedInto=classified_into,
        description=description,
    ).update(updates.dict())
    db_session.commit()
    updated_physical_feature = (
        db_session.query(models.Physicalfeature)
        .filter_by(
            associatedWith=associated_with,
            beginDate=begin_date,
            classifiedInto=classified_into,
            description=description,
        )
        .first()
    )
    return physicalfeature_schema.PhysicalFeature.from_orm(
        updated_physical_feature
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(
    db_session: Session,
    associated_with: str,
    begin_date: str,
    classified_into: str,
    description: str,
) -> bool:
    db_session.query(models.Physicalfeature).filter_by(
        associatedWith=associated_with,
        beginDate=begin_date,
        classifiedInto=classified_into,
        description=description,
    ).delete()
    db_session.commit()
    return True
