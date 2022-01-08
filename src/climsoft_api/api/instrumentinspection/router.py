from fastapi import APIRouter, Depends
from climsoft_api.services import instrumentinspection_service
import climsoft_api.api.instrumentinspection.schema as instrumentinspection_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get(
    "/",
    response_model=instrumentinspection_schema.InstrumentInspectionResponse,
)
def get_instrument_inspection(
    performed_on: str = None,
    inspection_datetime: str = None,
    performed_by: str = None,
    status: str = None,
    remarks: str = None,
    performed_at: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        instrument_inspection = instrumentinspection_service.query(
            db_session=db_session,
            performed_on=performed_on,
            inspection_datetime=inspection_datetime,
            performed_by=performed_by,
            status=status,
            remarks=remarks,
            performed_at=performed_at,
            limit=limit,
            offset=offset,
        )

        return get_success_response(
            result=instrument_inspection,
            message="Successfully fetched instrument_inspection.",
        )
    except instrumentinspection_service.FailedGettingInstrumentInspectionList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{performed_on}/{inspection_datetime}",
    response_model=instrumentinspection_schema.InstrumentInspectionWithStationAndInstrumentResponse,
)
def get_instrument_inspection_by_id(
    performed_on: str,
    inspection_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                instrumentinspection_service.get(
                    db_session=db_session,
                    performed_on=performed_on,
                    inspection_datetime=inspection_datetime,
                )
            ],
            message="Successfully fetched instrument_inspection.",
        )
    except instrumentinspection_service.FailedGettingInstrumentInspection as e:
        return get_error_response(message=str(e))


@router.post(
    "/",
    response_model=instrumentinspection_schema.InstrumentInspectionResponse,
)
def create_instrument_inspection(
    data: instrumentinspection_schema.CreateInstrumentInspection,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                instrumentinspection_service.create(db_session=db_session, data=data)
            ],
            message="Successfully created instrument_inspection.",
        )
    except instrumentinspection_service.FailedCreatingInstrumentInspection as e:
        return get_error_response(message=str(e))


@router.put(
    "/{performed_on}/{inspection_datetime}",
    response_model=instrumentinspection_schema.InstrumentInspectionResponse,
)
def update_instrument_inspection(
    performed_on: str,
    inspection_datetime: str,
    data: instrumentinspection_schema.UpdateInstrumentInspection,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                instrumentinspection_service.update(
                    db_session=db_session,
                    performed_on=performed_on,
                    inspection_datetime=inspection_datetime,
                    updates=data,
                )
            ],
            message="Successfully updated instrument_inspection.",
        )
    except instrumentinspection_service.FailedUpdatingInstrumentInspection as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{performed_on}/{inspection_datetime}",
    response_model=instrumentinspection_schema.InstrumentInspectionResponse,
)
def delete_instrument_inspection(
    performed_on: str,
    inspection_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        instrumentinspection_service.delete(
            db_session=db_session,
            performed_on=performed_on,
            inspection_datetime=inspection_datetime,
        )
        return get_success_response(
            result=[], message="Successfully deleted instrument_inspection."
        )
    except instrumentinspection_service.FailedDeletingInstrumentInspection as e:
        return get_error_response(message=str(e))
