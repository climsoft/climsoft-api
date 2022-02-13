import math

from fastapi import APIRouter, Depends
from climsoft_api.services import acquisitiontype_service
import climsoft_api.api.acquisition_type.schema as acquisitiontype_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api.deps import get_session


router = APIRouter()


@router.get("/", response_model=acquisitiontype_schema.AcquisitionTypeQueryResponse)
def get_acquisition_types(
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(get_session),
):
    try:
        total, stations = acquisitiontype_service.query(
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
            result=stations,
            message="Successfully fetched stations."
        )
    except acquisitiontype_service.FailedGettingAcquisitionTypeList as e:
        return get_error_response(message=str(e))


@router.get("/{code}", response_model=acquisitiontype_schema.AcquisitionTypeResponse)
def get_acquisition_type_by_id(code: str, db_session: Session = Depends(get_session)):
    try:
        return get_success_response(
            result=[acquisitiontype_service.get(db_session=db_session, code=code)],
            message="Successfully fetched station.",
        )
    except acquisitiontype_service.FailedGettingAcquisitionType as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=acquisitiontype_schema.AcquisitionTypeResponse)
def create_acquisition_type(
    data: acquisitiontype_schema.CreateAcquisitionType,
    db_session: Session = Depends(get_session),
):
    try:
        return get_success_response(
            result=[acquisitiontype_service.create(db_session=db_session, data=data)],
            message="Successfully created station.",
        )
    except acquisitiontype_service.FailedCreatingAcquisitionType as e:
        return get_error_response(message=str(e))


@router.put("/{code}", response_model=acquisitiontype_schema.AcquisitionTypeResponse)
def update_acquisition_type(
    code: str,
    data: acquisitiontype_schema.UpdateAcquisitionType,
    db_session: Session = Depends(get_session),
):
    try:
        return get_success_response(
            result=[
                acquisitiontype_service.update(
                    db_session=db_session, code=code, updates=data
                )
            ],
            message="Successfully updated station.",
        )
    except acquisitiontype_service.FailedUpdatingAcquisitionType as e:
        return get_error_response(message=str(e))


@router.delete("/{code}", response_model=acquisitiontype_schema.AcquisitionTypeResponse)
def delete_acquisition_type(code: str, db_session: Session = Depends(get_session)):
    try:
        acquisitiontype_service.delete(db_session=db_session, code=code)
        return get_success_response(result=[], message="Successfully deleted station.")
    except acquisitiontype_service.FailedDeletingAcquisitionType as e:
        return get_error_response(message=str(e))
