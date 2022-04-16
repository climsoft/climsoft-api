import climsoft_api.api.obsscheduleclass.schema as obsscheduleclass_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import obsscheduleclass_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging
from climsoft_api.utils.exception import handle_exceptions

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get(
    "/obs-schedule-class"
)
@handle_exceptions
def get_obs_schedule_class(
    schedule_class: str = None,
    description: str = None,
    refers_to: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, obs_schedule_class = obsscheduleclass_service.query(
        db_session=db_session,
        schedule_class=schedule_class,
        description=description,
        refers_to=refers_to,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=obs_schedule_class,
        message=_("Successfully fetched obs schedule class."),
        schema=translate_schema(
            _,
            obsscheduleclass_schema.ObsScheduleClassQueryResponse.schema()
        )
    )


@router.get(
    "/obs-schedule-class/{schedule_class}"
)
@handle_exceptions
def get_instrument_by_id(
    schedule_class: str,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            obsscheduleclass_service.get(
                db_session=db_session, schedule_class=schedule_class
            )
        ],
        message=_("Successfully fetched instrument."),
        schema=translate_schema(
            _,
            obsscheduleclass_schema.ObsScheduleClassWithStationResponse.schema()
        )
    )


@router.post(
    "/obs-schedule-class",
)
@handle_exceptions
def create_instrument(
    data: obsscheduleclass_schema.CreateObsScheduleClass,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[obsscheduleclass_service.create(
            db_session=db_session,
            data=data
        )],
        message=_("Successfully created instrument."),
        schema=translate_schema(
            _,
            obsscheduleclass_schema.ObsScheduleClassResponse.schema()
        )
    )


@router.put(
    "/obs-schedule-class/{schedule_class}",
    response_model=obsscheduleclass_schema.ObsScheduleClassResponse,
)
@handle_exceptions
def update_instrument(
    schedule_class: str,
    data: obsscheduleclass_schema.UpdateObsScheduleClass,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            obsscheduleclass_service.update(
                db_session=db_session, schedule_class=schedule_class,
                updates=data
            )
        ],
        message=_("Successfully updated instrument."),
        schema=translate_schema(
            _,
            obsscheduleclass_schema.ObsScheduleClassResponse.schema()
        )
    )


@router.delete(
    "/obs-schedule-class/{schedule_class}",
    response_model=obsscheduleclass_schema.ObsScheduleClassResponse,
)
@handle_exceptions
def delete_instrument(
    schedule_class: str, db_session: Session = Depends(deps.get_session)
):
    obsscheduleclass_service.delete(
        db_session=db_session, schedule_class=schedule_class
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted instrument."),
        schema=translate_schema(
            _,
            obsscheduleclass_schema.ObsScheduleClassResponse.schema()
        )
    )
