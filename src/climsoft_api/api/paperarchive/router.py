import climsoft_api.api.paperarchive.schema as paperarchive_schema
from climsoft_api.api import deps
from climsoft_api.services import paperarchive_service
from climsoft_api.utils.response import get_success_response, \
    get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging
from climsoft_api.utils.exception import handle_exceptions


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get("/paper-archives")
@handle_exceptions
def get_paper_archives(
    belongs_to: str = None,
    form_datetime: str = None,
    image: str = None,
    classified_into: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, paper_archives = paperarchive_service.query(
        db_session=db_session,
        belongs_to=belongs_to,
        form_datetime=form_datetime,
        image=image,
        classified_into=classified_into,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=paper_archives,
        message=_("Successfully fetched paper archives."),
        schema=translate_schema(
            _,
            paperarchive_schema.PaperArchiveQueryResponse.schema()
        )
    )


@router.get(
    "/paper-archives/{belongs_to}/{form_datetime}/{classified_into}"
)
@handle_exceptions
def get_paper_archive_by_id(
    belongs_to: str,
    form_datetime: str,
    classified_into: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            paperarchive_service.get(
                db_session=db_session,
                belongs_to=belongs_to,
                form_datetime=form_datetime,
                classified_into=classified_into,
            )
        ],
        message=_("Successfully fetched paper archive."),
        schema=translate_schema(
            _,
            paperarchive_schema.PaperArchiveWithStationAndPaperArchiveDefinitionResponse.schema()
        )
    )


@router.post("/paper-archives")
@handle_exceptions
def create_paper_archive(
    data: paperarchive_schema.CreatePaperArchive,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            paperarchive_service.create(db_session=db_session, data=data)],
        message=_("Successfully created paper archive."),
        schema=translate_schema(
            _,
            paperarchive_schema.PaperArchiveResponse.schema()
        )
    )


@router.put(
    "/paper-archives/{belongs_to}/{form_datetime}/{classified_into}"
)
@handle_exceptions
def update_paper_archive(
    belongs_to: str,
    form_datetime: str,
    classified_into: str,
    data: paperarchive_schema.UpdatePaperArchive,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            paperarchive_service.update(
                db_session=db_session,
                belongs_to=belongs_to,
                form_datetime=form_datetime,
                classified_into=classified_into,
                data=data,
            )
        ],
        message=_("Successfully updated paper archive."),
        schema=translate_schema(
            _,
            paperarchive_schema.PaperArchiveResponse.schema()
        )
    )


@router.delete(
    "/paper-archives/{belongs_to}/{form_datetime}/{classified_into}"
)
@handle_exceptions
def delete_paper_archive(
    belongs_to: str,
    form_datetime: str,
    classified_into: str,
    db_session: Session = Depends(deps.get_session),
):
    paperarchive_service.delete(
        db_session=db_session,
        belongs_to=belongs_to,
        form_datetime=form_datetime,
        classified_into=classified_into,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted paper archive."),
        schema=translate_schema(
            _,
            paperarchive_schema.PaperArchiveResponse.schema()
        )
    )
