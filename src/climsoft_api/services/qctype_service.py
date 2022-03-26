import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.qctype import schema as qctype_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftQCTypeService")
logging.basicConfig(level=logging.INFO)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session, data: qctype_schema.CreateQCType
) -> qctype_schema.QCType:
    qc_type = models.Qctype(**data.dict())
    db_session.add(qc_type)
    db_session.commit()
    return qctype_schema.QCType.from_orm(qc_type)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(db_session: Session, code: str) -> qctype_schema.QCType:
    qc_type = db_session.query(models.Qctype).filter_by(code=code).first()

    if not qc_type:
        raise HTTPException(
            status_code=404,
            detail=_("QC type does not exist.")
        )

    return qctype_schema.QCType.from_orm(qc_type)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[qctype_schema.QCType]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `qc_types` row skipping
    `offset` number of rows

    """
    q = db_session.query(models.Qctype)

    if code is not None:
        q = q.filter_by(code=code)

    if description is not None:
        q = q.filter(models.Qctype.description.ilike(f"%{description}%"))

    return (
        get_count(q),
        [
            qctype_schema.QCType.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session, code: str, updates: qctype_schema.UpdateQCType
) -> qctype_schema.QCType:
    db_session.query(models.Qctype).filter_by(code=code).update(
        updates.dict())
    db_session.commit()
    updated_qc_type = db_session.query(models.Qctype).filter_by(
        code=code).first()
    return qctype_schema.QCType.from_orm(updated_qc_type)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, code: str) -> bool:
    db_session.query(models.Qctype).filter_by(code=code).delete()
    db_session.commit()
    return True
