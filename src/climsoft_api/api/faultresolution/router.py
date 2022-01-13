from fastapi import APIRouter, Depends
from climsoft_api.services import faultresolution_service
import climsoft_api.api.faultresolution.schema as faultresolution_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps


router = APIRouter()


@router.get("/", response_model=faultresolution_schema.FaultResolutionResponse)
def get_instrument_inspection(
    resolved_datetime: str = None,
    associated_with: str = None,
    resolved_by: str = None,
    remarks: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        instrument_inspection = faultresolution_service.query(
            db_session=db_session,
            resolved_datetime=resolved_datetime,
            associated_with=associated_with,
            resolved_by=resolved_by,
            remarks=remarks,
            limit=limit,
            offset=offset,
        )

        return get_success_response(
            result=instrument_inspection,
            message="Successfully fetched instrument_inspection.",
        )
    except faultresolution_service.FailedGettingFaultResolutionList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{resolved_datetime}/{associated_with}",
    response_model=faultresolution_schema.FaultResolutionWithInstrumentFaultReportResponse,
)
def get_instrument_inspection_by_id(
    resolved_datetime: str,
    associated_with: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                faultresolution_service.get(
                    db_session=db_session,
                    resolved_datetime=resolved_datetime,
                    associated_with=associated_with,
                )
            ],
            message="Successfully fetched instrument_inspection.",
        )
    except faultresolution_service.FailedGettingFaultResolution as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=faultresolution_schema.FaultResolutionResponse)
def create_instrument_inspection(
    data: faultresolution_schema.CreateFaultResolution,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[faultresolution_service.create(db_session=db_session, data=data)],
            message="Successfully created instrument_inspection.",
        )
    except faultresolution_service.FailedCreatingFaultResolution as e:
        return get_error_response(message=str(e))


@router.put(
    "/{resolved_datetime}/{associated_with}",
    response_model=faultresolution_schema.FaultResolutionResponse,
)
def update_instrument_inspection(
    resolved_datetime: str,
    associated_with: str,
    data: faultresolution_schema.UpdateFaultResolution,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                faultresolution_service.update(
                    db_session=db_session,
                    resolved_datetime=resolved_datetime,
                    associated_with=associated_with,
                    updates=data,
                )
            ],
            message="Successfully updated instrument_inspection.",
        )
    except faultresolution_service.FailedUpdatingFaultResolution as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{resolved_datetime}/{associated_with}",
    response_model=faultresolution_schema.FaultResolutionResponse,
)
def delete_instrument_inspection(
    resolved_datetime: str,
    associated_with: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        faultresolution_service.delete(
            db_session=db_session,
            resolved_datetime=resolved_datetime,
            associated_with=associated_with,
        )
        return get_success_response(
            result=[], message="Successfully deleted instrument_inspection."
        )
    except faultresolution_service.FailedDeletingFaultResolution as e:
        return get_error_response(message=str(e))
