import \
    climsoft_api.api.paperarchivedefinition.schema as paperarchivedefinition_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import paperarchivedefinition_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging


router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get(
    "/",
)
def get_paper_archive_definitions(
    form_id: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, paper_archive_definitions = paperarchivedefinition_service.query(
            db_session=db_session,
            form_id=form_id,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=paper_archive_definitions,
            message=_("Successfully fetched paper archive definitions."),
            schema=translate_schema(
                _,
                paperarchivedefinition_schema.PaperArchiveDefinitionQueryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.get(
    "/{form_id}",
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
            message=_("Successfully fetched paper archive definition."),
            schema=translate_schema(
                _,
                paperarchivedefinition_schema.PaperArchiveDefinitionResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.post(
    "/",
)
def create_paper_archive_definition(
    data: paperarchivedefinition_schema.CreatePaperArchiveDefinition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                paperarchivedefinition_service.create(
                    db_session=db_session,
                    data=data
                )
            ],
            message=_("Successfully created paper archive definition."),
            schema=translate_schema(
                _,
                paperarchivedefinition_schema.PaperArchiveDefinitionResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.put(
    "/{form_id}"
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
            message=_("Successfully updated paper archive definition."),
            schema=translate_schema(
                _,
                paperarchivedefinition_schema.PaperArchiveDefinitionResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.delete(
    "/{form_id}"
)
def delete_paper_archive_definition(
    form_id: str, db_session: Session = Depends(deps.get_session)
):
    try:
        paperarchivedefinition_service.delete(db_session=db_session,
                                              form_id=form_id)
        return get_success_response(
            result=[],
            message=_("Successfully deleted paper archive definition."),
            schema=translate_schema(
                _,
                paperarchivedefinition_schema.PaperArchiveDefinitionResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )
