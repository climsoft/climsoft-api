import logging
import backoff
from climsoft_api.api.paperarchive import schema as paperarchive_schema
from climsoft_api.utils.query import get_count
from fastapi import HTTPException
from opencdms.models.climsoft import v4_1_1_core as models
from sqlalchemy.orm import joinedload
from sqlalchemy.orm.session import Session

logger = logging.getLogger("ClimsoftPaperArchiveService")
logging.basicConfig(level=logging.INFO)


def query(
    db_session: Session,
    belongs_to: str = None,
    form_datetime: str = None,
    image: str = None,
    classified_into: str = None,
    offset: int = 0,
    limit: int = 25,
):
    q = db_session.query(models.Paperarchive)

    if belongs_to is not None:
        q = q.filter_by(belongsTo=belongs_to)

    if form_datetime is not None:
        q = q.filter_by(formDatetime=form_datetime)

    if image is not None:
        q = q.filter_by(image=image)

    if classified_into is not None:
        q = q.filter_by(classifiedInto=classified_into)

    return (
        get_count(q),
        [
            paperarchive_schema.PaperArchive.from_orm(paper_archive)
            for paper_archive in q.offset(offset).limit(limit).all()
        ]
    )


def get(
    db_session: Session,
    belongs_to: str,
    form_datetime: str,
    classified_into: str
):
    response = (
        db_session.query(models.Paperarchive)
        .filter_by(
            belongsTo=belongs_to,
            formDatetime=form_datetime,
            classifiedInto=classified_into,
        )
        .options(
            joinedload("station"),
            joinedload("paperarchivedefinition")
        )
        .first()
    )
    if not response:
        raise HTTPException(
            status_code=404,
            detail=_("Paper archive not found.")
        )

    return paperarchive_schema \
        .PaperArchiveWithStationAndPaperArchiveDefinition.from_orm(
            response
        )


def create(db_session: Session, data: paperarchive_schema.CreatePaperArchive):
    paper_archive = models.Paperarchive(**data.dict())
    db_session.add(paper_archive)
    db_session.commit()
    return paperarchive_schema.PaperArchive.from_orm(paper_archive)


def update(
    db_session: Session,
    belongs_to: str,
    form_datetime: str,
    classified_into: str,
    data: paperarchive_schema.UpdatePaperArchive,
):
    db_session.query(models.Paperarchive).filter_by(
        belongsTo=belongs_to,
        formDatetime=form_datetime,
        classifiedInto=classified_into,
    ).update(data.dict())
    db_session.commit()
    updated_paper_archive = (
        db_session.query(models.Paperarchive)
        .filter_by(
            belongsTo=belongs_to,
            formDatetime=form_datetime,
            classifiedInto=classified_into,
        )
        .first()
    )
    return paperarchive_schema.PaperArchive.from_orm(updated_paper_archive)


def delete(
    db_session: Session, belongs_to: str, form_datetime: str,
    classified_into: str
):
    db_session.query(models.Paperarchive).filter_by(
        belongsTo=belongs_to,
        formDatetime=form_datetime,
        classifiedInto=classified_into,
    ).delete()
    db_session.commit()
    return True
