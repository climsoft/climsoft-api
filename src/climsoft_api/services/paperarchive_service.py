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
    try:
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
    except Exception as e:
        logger.exception(e)
        raise FailedFetchingPaperArchives(
            _("Failed fetching list of paper archives.")
        )


def get(
    db_session: Session,
    belongs_to: str,
    form_datetime: str,
    classified_into: str
):
    try:
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
    except HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        raise FailedGettingPaperArchive(
            _("Failed to get paper archive.")
        )


def create(db_session: Session, data: paperarchive_schema.CreatePaperArchive):
    try:
        paper_archive = models.Paperarchive(**data.dict())
        db_session.add(paper_archive)
        db_session.commit()
        return paperarchive_schema.PaperArchive.from_orm(paper_archive)
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedCreatingPaperArchive(
            _("Failed to create paper archive.")
        )


def update(
    db_session: Session,
    belongs_to: str,
    form_datetime: str,
    classified_into: str,
    data: paperarchive_schema.UpdatePaperArchive,
):
    try:
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
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedUpdatingPaperArchive(
            _("Failed to update paper archive.")
        )


def delete(
    db_session: Session, belongs_to: str, form_datetime: str,
    classified_into: str
):
    try:
        db_session.query(models.Paperarchive).filter_by(
            belongsTo=belongs_to,
            formDatetime=form_datetime,
            classifiedInto=classified_into,
        ).delete()
        db_session.commit()
        return True
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        raise FailedDeletingPaperArchive(
            _("Failed to delete paper archive.")
        )
