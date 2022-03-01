from fastapi import APIRouter, Depends
from climsoft_api.services import obselement_service
import climsoft_api.api.obselement.schema as obselement_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get("/", response_model=obselement_schema.ObsElementQueryResponse)
def get_obselements(
    element_id: str = None,
    element_name: str = None,
    abbreviation: str = None,
    description: str = None,
    element_scale: float = None,
    upper_limit: float = None,
    lower_limit: str = None,
    units: str = None,
    element_type: str = None,
    qc_total_required: int = None,
    selected: bool = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, obselements = obselement_service.query(
            db_session=db_session,
            element_id=element_id,
            element_name=element_name,
            abbreviation=abbreviation,
            description=description,
            element_scale=element_scale,
            upper_limit=upper_limit,
            lower_limit=lower_limit,
            units=units,
            element_type=element_type,
            qc_total_required=qc_total_required,
            selected=selected,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=obselements,
            message=_("Successfully fetched obs elements.")
        )
    except obselement_service.FailedGettingObsElementList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{element_id}",
    response_model=obselement_schema.ObsElementResponse
)
def get_obs_element_by_id(
    element_id: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                obselement_service.get(
                    db_session=db_session,
                    element_id=element_id
                )
            ],
            message=_("Successfully fetched obs element."),
        )
    except obselement_service.FailedGettingObsElement as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=obselement_schema.ObsElementResponse)
def create_obs_element(
    data: obselement_schema.CreateObsElement,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[obselement_service.create(
                db_session=db_session,
                data=data
            )],
            message=_("Successfully created obs element."),
        )
    except obselement_service.FailedCreatingObsElement as e:
        return get_error_response(message=str(e))


@router.put(
    "/{element_id}",
    response_model=obselement_schema.ObsElementResponse
)
def update_obs_element(
    element_id: str,
    data: obselement_schema.UpdateObsElement,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                obselement_service.update(
                    db_session=db_session,
                    element_id=element_id,
                    updates=data
                )
            ],
            message=_("Successfully updated obs element."),
        )
    except obselement_service.FailedUpdatingObsElement as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{element_id}",
    response_model=obselement_schema.ObsElementResponse
)
def delete_obs_element(
    element_id: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        obselement_service.delete(
            db_session=db_session,
            element_id=element_id
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted obs element.")
        )
    except obselement_service.FailedDeletingObsElement as e:
        return get_error_response(message=str(e))
