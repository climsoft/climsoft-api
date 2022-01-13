from fastapi import APIRouter, Depends
from climsoft_api.services import observationfinal_service
import climsoft_api.api.observationfinal.schema as observationfinal_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get(
    "/",
    response_model=observationfinal_schema.ObservationFinalResponse,
)
def get_observation_finals(
    recorded_from: str = None,
    described_by: int = None,
    obs_datetime: str = None,
    qc_status: int = None,
    acquisition_type: int = None,
    obs_level: int = None,
    obs_value: float = None,
    flag: str = None,
    period: int = None,
    qc_type_log: str = None,
    data_form: str = None,
    captured_by: str = None,
    mark: bool = None,
    temperature_units: str = None,
    precipitation_units: str = None,
    cloud_height_units: str = None,
    vis_units: str = None,
    data_source_timezone: int = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        observation_finals = observationfinal_service.query(
            db_session=db_session,
            recorded_from=recorded_from,
            obs_datetime=obs_datetime,
            qc_status=qc_status,
            described_by=described_by,
            acquisition_type=acquisition_type,
            obs_value=obs_value,
            obs_level=obs_level,
            flag=flag,
            period=period,
            qc_type_log=qc_type_log,
            data_form=data_form,
            captured_by=captured_by,
            mark=mark,
            temperature_units=temperature_units,
            precipitation_units=precipitation_units,
            cloud_height_units=cloud_height_units,
            vis_units=vis_units,
            data_source_timezone=data_source_timezone,
            limit=limit,
            offset=offset,
        )

        return get_success_response(
            result=observation_finals,
            message="Successfully fetched observation_finals.",
        )
    except observationfinal_service.FailedGettingObservationFinalList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{recorded_from}/{described_by}/{obs_datetime}",
    response_model=observationfinal_schema.ObservationFinalWithChildrenResponse,
)
def get_observation_final_by_id(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                observationfinal_service.get(
                    db_session=db_session,
                    recorded_from=recorded_from,
                    described_by=described_by,
                    obs_datetime=obs_datetime,
                )
            ],
            message="Successfully fetched observation_final.",
        )
    except observationfinal_service.FailedGettingObservationFinal as e:
        return get_error_response(message=str(e))


@router.post(
    "/",
    response_model=observationfinal_schema.ObservationFinalResponse,
)
def create_observation_final(
    data: observationfinal_schema.CreateObservationFinal,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[observationfinal_service.create(db_session=db_session, data=data)],
            message="Successfully created observation_final.",
        )
    except observationfinal_service.FailedCreatingObservationFinal as e:
        return get_error_response(message=str(e))


@router.put(
    "/{recorded_from}/{described_by}/{obs_datetime}",
    response_model=observationfinal_schema.ObservationFinalResponse,
)
def update_observation_final(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    data: observationfinal_schema.UpdateObservationFinal,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                observationfinal_service.update(
                    db_session=db_session,
                    recorded_from=recorded_from,
                    described_by=described_by,
                    obs_datetime=obs_datetime,
                    updates=data,
                )
            ],
            message="Successfully updated observation_final.",
        )
    except observationfinal_service.FailedUpdatingObservationFinal as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{recorded_from}/{described_by}/{obs_datetime}",
    response_model=observationfinal_schema.ObservationFinalResponse,
)
def delete_observation_final(
    recorded_from: str,
    described_by: int,
    obs_datetime: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        observationfinal_service.delete(
            db_session=db_session,
            recorded_from=recorded_from,
            described_by=described_by,
            obs_datetime=obs_datetime,
        )
        return get_success_response(
            result=[], message="Successfully deleted observation_final."
        )
    except observationfinal_service.FailedDeletingObservationFinal as e:
        return get_error_response(message=str(e))
