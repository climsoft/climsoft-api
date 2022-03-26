import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.qcstatusdefinition import \
    schema as qcstatusdefinition_schema
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftQCStatusDefinitionService")
logging.basicConfig(level=logging.INFO)


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def create(
    db_session: Session,
    data: qcstatusdefinition_schema.CreateQCStatusDefinition
) -> qcstatusdefinition_schema.QCStatusDefinition:
    qc_status_definition = models.Qcstatusdefinition(**data.dict())
    db_session.add(qc_status_definition)
    db_session.commit()
    return qcstatusdefinition_schema.QCStatusDefinition.from_orm(
        qc_status_definition
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def get(
    db_session: Session,
    code: str
) -> qcstatusdefinition_schema.QCStatusDefinition:
    qc_status_definition = (
        db_session.query(models.Qcstatusdefinition).filter_by(
            code=code
        ).first()
    )

    if not qc_status_definition:
        raise HTTPException(
            status_code=404,
            detail=_("QC status definition does not exist.")
        )

    return qcstatusdefinition_schema.QCStatusDefinition.from_orm(
        qc_status_definition
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def query(
    db_session: Session,
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[qcstatusdefinition_schema.QCStatusDefinition]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `qc_status_definitions` row skipping
    `offset` number of rows

    """
    q = db_session.query(models.Qcstatusdefinition)

    if code is not None:
        q = q.filter_by(code=code)

    if description is not None:
        q = q.filter(
            models.Qcstatusdefinition.description.ilike(f"%{description}%")
        )

    return (
        get_count(q),
        [
            qcstatusdefinition_schema.QCStatusDefinition.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def update(
    db_session: Session,
    code: str,
    updates: qcstatusdefinition_schema.UpdateQCStatusDefinition,
) -> qcstatusdefinition_schema.QCStatusDefinition:
    db_session.query(models.Qcstatusdefinition).filter_by(code=code).update(
        updates.dict()
    )
    db_session.commit()
    updated_qc_status_definition = (
        db_session.query(models.Qcstatusdefinition).filter_by(
            code=code
        ).first()
    )
    return qcstatusdefinition_schema.QCStatusDefinition.from_orm(
        updated_qc_status_definition
    )


@backoff.on_exception(backoff.expo, sqlalchemy.exc.OperationalError)
def delete(db_session: Session, code: str) -> bool:
    db_session.query(models.Qcstatusdefinition).filter_by(
        code=code
    ).delete()
    db_session.commit()
    return True
