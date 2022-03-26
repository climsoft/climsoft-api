import logging
from typing import List, Tuple
import backoff
from climsoft_api.api.synopfeature import schema as synopfeature_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftSynopFeatureService")
logging.basicConfig(level=logging.INFO)


def create(
    db_session: Session, data: synopfeature_schema.CreateSynopFeature
) -> synopfeature_schema.SynopFeature:

    synop_feature = models.Synopfeature(**data.dict())
    db_session.add(synop_feature)
    db_session.commit()
    return synopfeature_schema.SynopFeature.from_orm(synop_feature)


def get(db_session: Session,
    abbreviation: str) -> synopfeature_schema.SynopFeature:
    synop_feature = (
        db_session.query(models.Synopfeature)
            .filter_by(abbreviation=abbreviation)
            .first()
    )

    if not synop_feature:
        raise HTTPException(
            status_code=404,
            detail=_("Synop feature does not exist.")
        )

    return synopfeature_schema.SynopFeature.from_orm(synop_feature)


def query(
    db_session: Session,
    abbreviation: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[synopfeature_schema.SynopFeature]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `synop_features` row skipping
    `offset` number of rows

    """
    q = db_session.query(models.Synopfeature)

    if abbreviation is not None:
        q = q.filter_by(abbreviation=abbreviation)

    if description is not None:
        q = q.filter(
            models.Synopfeature.description.ilike(f"%{description}%")
        )

    return (
        get_count(q),
        [
            synopfeature_schema.SynopFeature.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    abbreviation: str,
    updates: synopfeature_schema.UpdateSynopFeature,
) -> synopfeature_schema.SynopFeature:
    db_session.query(models.Synopfeature).filter_by(
        abbreviation=abbreviation
    ).update(updates.dict())
    db_session.commit()
    updated_synop_feature = (
        db_session.query(models.Synopfeature)
            .filter_by(abbreviation=abbreviation)
            .first()
    )
    return synopfeature_schema.SynopFeature.from_orm(updated_synop_feature)


def delete(db_session: Session, abbreviation: str) -> bool:
    db_session.query(models.Synopfeature).filter_by(
        abbreviation=abbreviation
    ).delete()
    db_session.commit()
    return True
