from fastapi import APIRouter, Depends
from climsoft_api.services import qctype_service
import climsoft_api.api.qctype.schema as qctype_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get("/", response_model=qctype_schema.QCTypeQueryResponse)
def get_qc_types(
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, qc_types = qctype_service.query(
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
            result=qc_types, message="Successfully fetched qc_types."
        )
    except qctype_service.FailedGettingQCTypeList as e:
        return get_error_response(message=str(e))


@router.get("/{code}", response_model=qctype_schema.QCTypeResponse)
def get_qc_type_by_id(code: str, db_session: Session = Depends(deps.get_session)):
    try:
        return get_success_response(
            result=[qctype_service.get(db_session=db_session, code=code)],
            message="Successfully fetched qc_type.",
        )
    except qctype_service.FailedGettingQCType as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=qctype_schema.QCTypeResponse)
def create_qc_type(
    data: qctype_schema.CreateQCType, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[qctype_service.create(db_session=db_session, data=data)],
            message="Successfully created qc_type.",
        )
    except qctype_service.FailedCreatingQCType as e:
        return get_error_response(message=str(e))


@router.put("/{code}", response_model=qctype_schema.QCTypeResponse)
def update_qc_type(
    code: str,
    data: qctype_schema.UpdateQCType,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                qctype_service.update(db_session=db_session, code=code, updates=data)
            ],
            message="Successfully updated qc_type.",
        )
    except qctype_service.FailedUpdatingQCType as e:
        return get_error_response(message=str(e))


@router.delete("/{code}", response_model=qctype_schema.QCTypeResponse)
def delete_qc_type(code: str, db_session: Session = Depends(deps.get_session)):
    try:
        qctype_service.delete(db_session=db_session, code=code)
        return get_success_response(result=[], message="Successfully deleted qc_type.")
    except qctype_service.FailedDeletingQCType as e:
        return get_error_response(message=str(e))
