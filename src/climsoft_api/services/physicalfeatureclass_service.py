import logging
from typing import List, Tuple
import backoff
from climsoft_api.api.physicalfeatureclass import (
    schema as physicalfeatureclass_schema
)
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftPhysicalFeatureClassService")
logging.basicConfig(level=logging.INFO)


def create(
    db_session: Session,
    data: physicalfeatureclass_schema.CreatePhysicalFeatureClass
) -> physicalfeatureclass_schema.PhysicalFeatureClass:
    try:
        physical_feature_class = models.Physicalfeatureclas(**data.dict())
        db_session.add(physical_feature_class)
        db_session.commit()
        return physicalfeatureclass_schema.PhysicalFeatureClass.from_orm(
            physical_feature_class
        )
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingPhysicalFeatureClass(
            _("Failed to create physical feature class.")
        )


def get(
    db_session: Session, feature_class: str
) -> physicalfeatureclass_schema.PhysicalFeatureClass:
    try:
        physical_feature_class = (
            db_session.query(models.Physicalfeatureclas)
                .filter_by(featureClass=feature_class)
                .options(joinedload("station"))
                .first()
        )

        if not physical_feature_class:
            raise HTTPException(
                status_code=404,
                detail=_("Physical feature class does not exist.")
            )

        return physicalfeatureclass_schema.PhysicalFeatureClassWithStation \
            .from_orm(
            physical_feature_class
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingPhysicalFeatureClass(
            _("Failed to get physical feature class.")
        )


def query(
    db_session: Session,
    feature_class: str = None,
    description: str = None,
    refers_to: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[physicalfeatureclass_schema.PhysicalFeatureClass]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `physical_feature_class` row skipping
    `offset` number of rows
    """
    try:
        q = db_session.query(models.Physicalfeatureclas)

        if feature_class is not None:
            q = q.filter_by(featureClass=feature_class)

        if description is not None:
            q = q.filter(
                models.Physicalfeatureclas.description.ilike(f"%{description}%")
            )

        if refers_to is not None:
            q = q.filter_by(refers_to=refers_to)

        return (
            get_count(q),
            [
                physicalfeatureclass_schema.PhysicalFeatureClass.from_orm(s)
                for s in q.offset(offset).limit(limit).all()
            ]
        )
    except Exception as e:
        logger.exception(e)
        raise FailedGettingPhysicalFeatureClassList(
            _("Failed to get list of physical feature classes.")
        )


def update(
    db_session: Session,
    feature_class: str,
    updates: physicalfeatureclass_schema.UpdatePhysicalFeatureClass,
) -> physicalfeatureclass_schema.PhysicalFeatureClass:
    try:
        db_session.query(models.Physicalfeatureclas).filter_by(
            featureClass=feature_class
        ).update(updates.dict())
        db_session.commit()
        updated_physical_feature_class = (
            db_session.query(models.Physicalfeatureclas)
                .filter_by(featureClass=feature_class)
                .first()
        )
        return physicalfeatureclass_schema.PhysicalFeatureClass.from_orm(
            updated_physical_feature_class
        )
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingPhysicalFeatureClass(
            _("Failed to update physical feature class.")
        )


def delete(db_session: Session, feature_class: str) -> bool:
    try:
        db_session.query(models.Physicalfeatureclas).filter_by(
            featureClass=feature_class
        ).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingPhysicalFeatureClass(
            _("Failed to delete physical feature class.")
        )
