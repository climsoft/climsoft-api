import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.obselement import schema as obselement_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session
from opencdms.utils.climsoft.elements import (
    get_element_abbreviation_by_time_period
)

logger = logging.getLogger("ClimsoftObsElementService")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session,
    element_id: str
):

    obs_element = (
        db_session.query(
            models.Obselement
        ).filter_by(elementId=element_id).first()
    )

    if not obs_element:
        raise HTTPException(
            status_code=404,
            detail=_("Obs element does not exist.")
        )

    return obs_element


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: obselement_schema.CreateObsElement
) -> obselement_schema.ObsElement:
    obs_element = models.Obselement(**data.dict())
    db_session.add(obs_element)
    db_session.commit()
    return obselement_schema.ObsElement.from_orm(obs_element)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(db_session: Session, element_id: str) -> obselement_schema.ObsElement:
    obs_element = get_or_404(db_session, element_id)

    return obselement_schema.ObsElement.from_orm(obs_element)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    element_id: str = None,
    element_name: str = None,
    abbreviation: str = None,
    description: str = None,
    element_scale: float = None,
    upper_limit: float = None,
    lower_limit: str = None,
    units: str = None,
    element_type: str = None,
    qc_total_required: int = None,
    selected: bool = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[obselement_schema.ObsElement]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `obselement` row skipping
    `offset` number of rows

    :param db_session: sqlalchemy database session
    :param element_id: compares with `elementId` column for an exact match
    :param element_name: compares with `elementName` column for an exact match
    :param abbreviation: compares with `abbreviation` column for an exact match
    :param description: check if `description` column contains given value
    :param element_scale: returns items with equal or greater element scale
    :param upper_limit: returns items with lower or equal upper limit
    :param lower_limit: returns items with higher or equal lower limit
    :param units: checks if `units` column contains given value
    :param element_type: checks if `elementtype` column contains given value
    :param qc_total_required: returns items with greater or equal qcTotalRequired
    :param selected: compares with `selected` column for an exact match
    :param limit: describes page size
    :param offset: describe how many to skip
    :return: list of `obselement`
    """
    q = db_session.query(models.Obselement)

    if element_id is not None:
        q = q.filter_by(elementId=element_id)

    if element_name is not None:
        q = q.filter_by(elementName=element_name)

    if abbreviation is not None:
        q = q.filter_by(abbreviation=abbreviation)

    if description is not None:
        q = q.filter(models.Obselement.description.ilike(
            f"%{description}%")
        )

    if element_scale is not None:
        q = q.filter(models.Obselement.elementScale >= element_scale)

    if upper_limit is not None:
        q = q.filter(models.Obselement.upperLimit <= upper_limit)

    if lower_limit is not None:
        q = q.filter(models.Obselement.lowerLimit >= lower_limit)

    if units is not None:
        q = q.filter(models.Obselement.units.ilike(f"%{units}%"))

    if element_type is not None:
        q = q.filter(
            models.Obselement.elementtype.ilike(f"%{element_type}%")
        )

    if qc_total_required is not None:
        q = q.filter(models.Obselement.qcTotalRequired >= qc_total_required)

    if selected is not None:
        q = q.filter_by(selected=selected)

    return (
        get_count(q),
        [
            obselement_schema.ObsElement.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    element_id: str,
    updates: obselement_schema.UpdateObsElement
) -> obselement_schema.ObsElement:
    get_or_404(db_session, element_id)
    db_session.query(models.Obselement).filter_by(
        elementId=element_id).update(
        updates.dict()
    )
    db_session.commit()
    updated_obs_element = (
        db_session.query(models.Obselement).filter_by(
            elementId=element_id).first()
    )
    return obselement_schema.ObsElement.from_orm(updated_obs_element)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, element_id: str) -> bool:
    get_or_404(db_session, element_id)
    db_session.query(models.Obselement).filter_by(
        elementId=element_id
    ).delete()
    db_session.commit()
    return True


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def search(
    db_session: Session,
    _query: str = None,
    time_period: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[obselement_schema.ObsElement]]:

    q = db_session.query(models.Obselement)

    if _query:
        q = q.filter(
            models.Obselement.elementId.ilike(f"%{_query}%")
            | models.Obselement.elementName.ilike(f"%{_query}%")
        )
    if time_period:
        abbreviations = get_element_abbreviation_by_time_period(time_period)
        q = q.filter(models.Obselement.abbreviation.in_(
            tuple(abbreviations)
        ))

    return (
        get_count(q),
        [
            obselement_schema.ObsElement.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )
