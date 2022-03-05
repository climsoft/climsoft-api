import climsoft_api.api.qcstatusdefinition.schema as qcstatusdefinition_schema
from climsoft_api.api import deps
from climsoft_api.services import qcstatusdefinition_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.get(
    "/",
    response_model=qcstatusdefinition_schema.QCStatusDefinitionQueryResponse,
)
def get_qc_status_definitions(
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, qc_status_definitions = qcstatusdefinition_service.query(
            db_session=db_session,
            code=code,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=qc_status_definitions,
            message=_("Successfully fetched qc_status_definitions."),
        )
    except qcstatusdefinition_service.FailedGettingQCStatusDefinitionList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{code}",
    response_model=qcstatusdefinition_schema.QCStatusDefinitionResponse,
)
def get_qc_status_definition_by_id(
    code: str, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[qcstatusdefinition_service.get(db_session=db_session,
                                                   code=code)],
            message=_("Successfully fetched qc status definition."),
        )
    except qcstatusdefinition_service.FailedGettingQCStatusDefinition as e:
        return get_error_response(message=str(e))


@router.post(
    "/",
    response_model=qcstatusdefinition_schema.QCStatusDefinitionResponse,
)
def create_qc_status_definition(
    data: qcstatusdefinition_schema.CreateQCStatusDefinition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                qcstatusdefinition_service.create(db_session=db_session,
                                                  data=data)
            ],
            message=_("Successfully created qc status definition."),
        )
    except qcstatusdefinition_service.FailedCreatingQCStatusDefinition as e:
        return get_error_response(message=str(e))


@router.put(
    "/{code}",
    response_model=qcstatusdefinition_schema.QCStatusDefinitionResponse,
)
def update_qc_status_definition(
    code: str,
    data: qcstatusdefinition_schema.UpdateQCStatusDefinition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                qcstatusdefinition_service.update(
                    db_session=db_session, code=code, updates=data
                )
            ],
            message=_("Successfully updated qc status definition."),
        )
    except qcstatusdefinition_service.FailedUpdatingQCStatusDefinition as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{code}",
    response_model=qcstatusdefinition_schema.QCStatusDefinitionResponse,
)
def delete_qc_status_definition(
    code: str, db_session: Session = Depends(deps.get_session)
):
    try:
        qcstatusdefinition_service.delete(db_session=db_session, code=code)
        return get_success_response(
            result=[], message=_("Successfully deleted qc status definition.")
        )
    except qcstatusdefinition_service.FailedDeletingQCStatusDefinition as e:
        return get_error_response(message=str(e))
