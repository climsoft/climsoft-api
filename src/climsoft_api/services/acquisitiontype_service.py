import logging
from typing import List, Tuple
import backoff
import fastapi
import sqlalchemy.exc
from climsoft_api.api.acquisition_type import schema as acquisitiontype_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftAcquisitionTypeService")
logging.basicConfig(level=logging.INFO)


def get_or_not_found_acquisition_type(db_session: Session, code: str):
    acquisition_type = db_session.query(
        models.Acquisitiontype
    ).filter_by(code=code).first()
    if not acquisition_type:
        raise fastapi.HTTPException(
            status_code=404,
            detail=_("Acquisition type does not exist.")
        )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: acquisitiontype_schema.CreateAcquisitionType
) -> acquisitiontype_schema.AcquisitionType:
    acquisition_type = models.Acquisitiontype(**data.dict())
    db_session.add(acquisition_type)
    db_session.commit()
    return acquisitiontype_schema.AcquisitionType.from_orm(acquisition_type)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(
    db_session: Session,
    code: str
) -> acquisitiontype_schema.AcquisitionType:
    acquisition_type = (
        db_session.query(models.Acquisitiontype).filter_by(
            code=code).first()
    )

    if not acquisition_type:
        raise HTTPException(
            status_code=404,
            detail=_("Acquisition type does not exist.")
        )

    return acquisitiontype_schema.AcquisitionType.from_orm(acquisition_type)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[acquisitiontype_schema.AcquisitionType]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `obselement` row skipping
    `offset` number of rows
    :param db_session:
    :param code:
    :param description:
    :param limit:
    :param offset:
    :return:
    """

    q = db_session.query(models.Acquisitiontype)

    if code is not None:
        q = q.filter_by(code=code)

    if description is not None:
        q = q.filter(models.Acquisitiontype.description.ilike(
            f"%{description}%")
        )

    return (
        get_count(q),
        [
            acquisitiontype_schema.AcquisitionType.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    code: str,
    updates: acquisitiontype_schema.UpdateAcquisitionType,
) -> acquisitiontype_schema.AcquisitionType:
    get_or_not_found_acquisition_type(db_session, code)
    db_session.query(models.Acquisitiontype).filter_by(code=code).update(
        updates.dict()
    )
    db_session.commit()
    updated_acquisition_type = (
        db_session.query(
            models.Acquisitiontype
        ).filter_by(code=code).first()
    )
    return acquisitiontype_schema.AcquisitionType.from_orm(
        updated_acquisition_type
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, code: str) -> bool:
    get_or_not_found_acquisition_type(db_session, code)
    db_session.query(models.Acquisitiontype).filter_by(code=code).delete()
    db_session.commit()
    return True
