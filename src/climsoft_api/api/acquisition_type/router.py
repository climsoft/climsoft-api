from climsoft_api.services import acquisitiontype_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.api.acquisition_type import schema as acquisitiontype_schema
from climsoft_api.api.deps import get_session
from climsoft_api.utils.response import translate_schema

router = APIRouter()


@router.get(
    "/",
)
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
            message=_("Successfully fetched acquisition types."),
            schema=translate_schema(
                _,
                acquisitiontype_schema.AcquisitionTypeQueryResponse.schema()
            )
        )
    except acquisitiontype_service.FailedGettingAcquisitionTypeList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{code}"
)
def get_acquisition_type_by_id(
    code: str,
    db_session: Session = Depends(get_session)
):
    try:
        return get_success_response(
            result=[acquisitiontype_service.get(
                db_session=db_session,
                code=code
            )],
            message=_("Successfully fetched acquisition type."),
            schema=translate_schema(
                _,
                acquisitiontype_schema.AcquisitionTypeResponse.schema()
            )
        )
    except acquisitiontype_service.FailedGettingAcquisitionType as e:
        return get_error_response(message=str(e))


@router.post(
    "/"
)
def create_acquisition_type(
    data: acquisitiontype_schema.CreateAcquisitionType,
    db_session: Session = Depends(get_session),
):
    try:
        return get_success_response(
            result=[acquisitiontype_service.create(
                db_session=db_session,
                data=data
            )],
            message=_("Successfully created acquisition type."),
            schema=translate_schema(
                _,
                acquisitiontype_schema.AcquisitionTypeResponse.schema()
            )
        )
    except acquisitiontype_service.FailedCreatingAcquisitionType as e:
        return get_error_response(message=str(e))


@router.put(
    "/{code}"
)
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
            message=_("Successfully updated acquisition type."),
            schema=translate_schema(
                _,
                acquisitiontype_schema.AcquisitionTypeResponse.schema()
            )
        )
    except acquisitiontype_service.FailedUpdatingAcquisitionType as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{code}"
)
def delete_acquisition_type(
    code: str,
    db_session: Session = Depends(get_session)
):
    try:
        acquisitiontype_service.delete(db_session=db_session, code=code)
        return get_success_response(
            result=[],
            message=_("Successfully deleted acquisition type."),
            schema=translate_schema(
                _,
                acquisitiontype_schema.AcquisitionTypeResponse.schema()
            )
        )
    except acquisitiontype_service.FailedDeletingAcquisitionType as e:
        return get_error_response(message=str(e))
