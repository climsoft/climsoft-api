from fastapi import APIRouter, Depends
from climsoft_api.services import paperarchivedefinition_service
import climsoft_api.api.paperarchivedefinition.schema as paperarchivedefinition_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get(
    "/paper-archive-definitions",
    response_model=paperarchivedefinition_schema.PaperArchiveDefinitionResponse,
)
def get_paper_archive_definitions(
    form_id: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        paper_archive_definitions = paperarchivedefinition_service.query(
            db_session=db_session,
            form_id=form_id,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response(
            result=paper_archive_definitions,
            message="Successfully fetched paper_archive_definitions.",
        )
    except paperarchivedefinition_service.FailedGettingPaperArchiveDefinitionList as e:
        return get_error_response(message=str(e))


@router.get(
    "/paper-archive-definitions/{form_id}",
    response_model=paperarchivedefinition_schema.PaperArchiveDefinitionResponse,
)
def get_paper_archive_definition_by_id(
    form_id: str, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                paperarchivedefinition_service.get(
                    db_session=db_session, form_id=form_id
                )
            ],
            message="Successfully fetched paper_archive_definition.",
        )
    except paperarchivedefinition_service.FailedGettingPaperArchiveDefinition as e:
        return get_error_response(message=str(e))


@router.post(
    "/paper-archive-definitions",
    response_model=paperarchivedefinition_schema.PaperArchiveDefinitionResponse,
)
def create_paper_archive_definition(
    data: paperarchivedefinition_schema.CreatePaperArchiveDefinition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                paperarchivedefinition_service.create(db_session=db_session, data=data)
            ],
            message="Successfully created paper_archive_definition.",
        )
    except paperarchivedefinition_service.FailedCreatingPaperArchiveDefinition as e:
        return get_error_response(message=str(e))


@router.put(
    "/paper-archive-definitions/{form_id}",
    response_model=paperarchivedefinition_schema.PaperArchiveDefinitionResponse,
)
def update_paper_archive_definition(
    form_id: str,
    data: paperarchivedefinition_schema.UpdatePaperArchiveDefinition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                paperarchivedefinition_service.update(
                    db_session=db_session, form_id=form_id, updates=data
                )
            ],
            message="Successfully updated paper_archive_definition.",
        )
    except paperarchivedefinition_service.FailedUpdatingPaperArchiveDefinition as e:
        return get_error_response(message=str(e))


@router.delete(
    "/paper-archive-definitions/{form_id}",
    response_model=paperarchivedefinition_schema.PaperArchiveDefinitionResponse,
)
def delete_paper_archive_definition(
    form_id: str, db_session: Session = Depends(deps.get_session)
):
    try:
        paperarchivedefinition_service.delete(db_session=db_session, form_id=form_id)
        return get_success_response(
            result=[], message="Successfully deleted paper_archive_definition."
        )
    except paperarchivedefinition_service.FailedDeletingPaperArchiveDefinition as e:
        return get_error_response(message=str(e))
