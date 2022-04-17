import logging
from typing import List, Tuple
import backoff
import sqlalchemy.exc
from climsoft_api.api.paperarchivedefinition import (
    schema as paperarchivedefinition_schema,
)
from climsoft_api.utils.query import get_count
from fastapi.exceptions import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftPaperArchiveDefinitionService")
logging.basicConfig(level=logging.INFO)


def get_or_404(
    db_session: Session, form_id: str
):
    paper_archive_definition = (
        db_session.query(models.Paperarchivedefinition)
        .filter_by(formId=form_id)
        .first()
    )

    if not paper_archive_definition:
        raise HTTPException(
            status_code=404,
            detail=_("Paper archive definition does not exist.")
        )

    return paper_archive_definition


def create(
    db_session: Session,
    data: paperarchivedefinition_schema.CreatePaperArchiveDefinition,
) -> paperarchivedefinition_schema.PaperArchiveDefinition:
    paper_archive_definition = models.Paperarchivedefinition(**data.dict())
    db_session.add(paper_archive_definition)
    db_session.commit()
    return paperarchivedefinition_schema.PaperArchiveDefinition.from_orm(
        paper_archive_definition
    )


def get(
    db_session: Session, form_id: str
) -> paperarchivedefinition_schema.PaperArchiveDefinition:
    paper_archive_definition = get_or_404(db_session, form_id)

    return paperarchivedefinition_schema.PaperArchiveDefinition.from_orm(
        paper_archive_definition
    )


def query(
    db_session: Session,
    form_id: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
) -> Tuple[int, List[paperarchivedefinition_schema.PaperArchiveDefinition]]:
    """
    This function builds a query based on the given parameter and returns
    `limit` numbers of `paper_archive_definitions` row skipping
    `offset` number of rows

    """
    q = db_session.query(models.Paperarchivedefinition)

    if form_id is not None:
        q = q.filter_by(formId=form_id)

    if description is not None:
        q = q.filter(
            models.Paperarchivedefinition.description.ilike(
                f"%{description}%"
            )
        )

    return (
        get_count(q),
        [
            paperarchivedefinition_schema.PaperArchiveDefinition.from_orm(s)
            for s in q.offset(offset).limit(limit).all()
        ]
    )


def update(
    db_session: Session,
    form_id: str,
    updates: paperarchivedefinition_schema.UpdatePaperArchiveDefinition,
) -> paperarchivedefinition_schema.PaperArchiveDefinition:
    get_or_404(db_session, form_id)
    db_session.query(models.Paperarchivedefinition).filter_by(
        formId=form_id
    ).update(updates.dict())
    db_session.commit()
    updated_paper_archive_definition = (
        db_session.query(models.Paperarchivedefinition)
        .filter_by(formId=form_id)
        .first()
    )
    return paperarchivedefinition_schema.PaperArchiveDefinition.from_orm(
        updated_paper_archive_definition
    )


def delete(db_session: Session, form_id: str) -> bool:
    get_or_404(db_session, form_id)
    db_session.query(models.Paperarchivedefinition).filter_by(
        formId=form_id
    ).delete()
    db_session.commit()
    return True
