import logging
from typing import List, Tuple
import backoff
from climsoft_api.api.featuregeographicalposition import (
    schema as featuregeographicalposition_schema,
)
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftFeatureGeographicalPositionService")
logging.basicConfig(level=logging.INFO)


class FailedCreatingFeatureGeographicalPosition(Exception):
    pass


class FailedGettingFeatureGeographicalPosition(Exception):
    pass


class FailedGettingFeatureGeographicalPositionList(Exception):
    pass


class FailedUpdatingFeatureGeographicalPosition(Exception):
    pass


class FailedDeletingFeatureGeographicalPosition(Exception):
    pass


class FeatureGeographicalPositionDoesNotExist(Exception):
    pass


def create(
    db_session: Session,
    data: featuregeographicalposition_schema.CreateFeatureGeographicalPosition,
) -> featuregeographicalposition_schema.FeatureGeographicalPosition:
    try:
        feature_geographical_position = models.Featuregeographicalposition(
            **data.dict()
        )
        db_session.add(feature_geographical_position)
        db_session.commit()
        return featuregeographicalposition_schema.FeatureGeographicalPosition \
            .from_orm(
            feature_geographical_position
        )
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingFeatureGeographicalPosition(
            _("Failed to create feature geographical position.")
        )


def get(
    db_session: Session, belongs_to: str
) -> featuregeographicalposition_schema.FeatureGeographicalPosition:
    try:
        feature_geographical_position = (
            db_session.query(models.Featuregeographicalposition)
                .filter_by(belongsTo=belongs_to)
                .options(joinedload("synopfeature"))
                .first()
        )

        if not feature_geographical_position:
            raise HTTPException(
                status_code=404,
                detail="Feature geographical position does not exist."
            )

        return featuregeographicalposition_schema \
            .FeatureGeographicalPositionWithSynopFeature.from_orm(
            feature_geographical_position
        )
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingFeatureGeographicalPosition(
            _("Failed to get feature geographical position.")
        )


def query(
    db_session: Session,
    belongs_to: str = None,
    observed_on: str = None,
    latitude: str = None,
    longitude: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[
    int,
    List[featuregeographicalposition_schema.FeatureGeographicalPosition]
]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `feature_geographical_position` row skipping
    `offset` number of rows
    """
    try:
        q = db_session.query(models.Featuregeographicalposition)

        if belongs_to is not None:
            q = q.filter_by(belongsTo=belongs_to)

        if observed_on is not None:
            q = q.filter_by(observedOn=observed_on)

        if latitude is not None:
            q = q.filter_by(latitude=latitude)

        if longitude is not None:
            q = q.filter_by(longitude=longitude)

        return (
            get_count(q),
            [
                featuregeographicalposition_schema.FeatureGeographicalPosition
                    .from_orm(s)
                for s in q.offset(offset).limit(limit).all()
            ]
        )
    except Exception as e:
        logger.exception(e)
        raise FailedGettingFeatureGeographicalPositionList(
            _("Failed to get list of feature geographical positions.")
        )


def update(
    db_session: Session,
    belongs_to: str,
    updates: featuregeographicalposition_schema
        .UpdateFeatureGeographicalPosition,
) -> featuregeographicalposition_schema.FeatureGeographicalPosition:
    try:
        db_session.query(models.Featuregeographicalposition).filter_by(
            belongsTo=belongs_to
        ).update(updates.dict())
        db_session.commit()
        updated_feature_geographical_position = (
            db_session.query(models.Featuregeographicalposition)
                .filter_by(belongsTo=belongs_to)
                .first()
        )
        return featuregeographicalposition_schema.FeatureGeographicalPosition \
            .from_orm(
            updated_feature_geographical_position
        )
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingFeatureGeographicalPosition(
            _("Failed to update feature geographical position.")
        )


def delete(db_session: Session, belongs_to: str) -> bool:
    try:
        db_session.query(models.Featuregeographicalposition).filter_by(
            belongsTo=belongs_to
        ).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingFeatureGeographicalPosition(
            _("Failed to delete feature geographical position.")
        )
