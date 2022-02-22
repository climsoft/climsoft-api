from fastapi import APIRouter, Depends
from climsoft_api.services import featuregeographicalposition_service
import climsoft_api.api.featuregeographicalposition.schema as featuregeographicalposition_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps
from gettext import gettext as _


router = APIRouter()


@router.get(
    "/",
    response_model=featuregeographicalposition_schema.FeatureGeographicalPositionQueryResponse,
)
def get_feature_geographical_positions(
    belongs_to: str = None,
    observed_on: str = None,
    latitude: float = None,
    longitude: float = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, feature_geographical_positions = featuregeographicalposition_service.query(
            db_session=db_session,
            belongs_to=belongs_to,
            observed_on=observed_on,
            latitude=latitude,
            longitude=longitude,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=feature_geographical_positions,
            message=_("Successfully fetched feature geographical positions."),
        )
    except featuregeographicalposition_service\
            .FailedGettingFeatureGeographicalPositionList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{belongs_to}",
    response_model=featuregeographicalposition_schema.FeatureGeographicalPositionWithSynopFeatureResponse,
)
def get_feature_geographical_position_by_id(
    belongs_to: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                featuregeographicalposition_service.get(
                    db_session=db_session, belongs_to=belongs_to
                )
            ],
            message=_("Successfully fetched feature geographical position."),
        )
    except featuregeographicalposition_service.FailedGettingFeatureGeographicalPosition as e:
        return get_error_response(message=str(e))


@router.post(
    "/",
    response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse,
)
def create_feature_geographical_position(
    data: featuregeographicalposition_schema.CreateFeatureGeographicalPosition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                featuregeographicalposition_service.create(
                    db_session=db_session, data=data
                )
            ],
            message=_("Successfully created feature geographical position."),
        )
    except featuregeographicalposition_service.FailedCreatingFeatureGeographicalPosition as e:
        return get_error_response(message=str(e))


@router.put(
    "/{belongs_to}",
    response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse,
)
def update_feature_geographical_position(
    belongs_to: str,
    data: featuregeographicalposition_schema.UpdateFeatureGeographicalPosition,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                featuregeographicalposition_service.update(
                    db_session=db_session,
                    belongs_to=belongs_to,
                    updates=data
                )
            ],
            message=_("Successfully updated feature geographical position."),
        )
    except featuregeographicalposition_service.FailedUpdatingFeatureGeographicalPosition as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{belongs_to}",
    response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse,
)
def delete_feature_geographical_position(
    belongs_to: str, db_session: Session = Depends(deps.get_session)
):
    try:
        featuregeographicalposition_service.delete(
            db_session=db_session,
            belongs_to=belongs_to
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted feature geographical position.")
        )
    except featuregeographicalposition_service.FailedDeletingFeatureGeographicalPosition as e:
        return get_error_response(message=str(e))
