from fastapi import APIRouter, Depends
from climsoft_api.services import featuregeographicalposition_service
import climsoft_api.api.featuregeographicalposition.schema as featuregeographicalposition_schema
from climsoft_api.utils.response import get_success_response, get_error_response
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps


router = APIRouter()



@router.get("/feature-geographical-positions", response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse)
def get_feature_geographical_positions(
        belongs_to: str = None,
        observed_on: str = None,
        latitude: float = None,
        longitude: float = None,
        limit: int = 25,
        offset: int = 0,
        db_session: Session = Depends(deps.get_session)
):
    try:
        feature_geographical_positions = featuregeographicalposition_service.query(
            db_session=db_session,
            belongs_to=belongs_to,
            observed_on=observed_on,
            latitude=latitude,
            longitude=longitude,
            limit=limit,
            offset=offset
        )

        return get_success_response(result=feature_geographical_positions, message="Successfully fetched feature_geographical_positions.")
    except featuregeographicalposition_service.FailedGettingFeatureGeographicalPositionList as e:
        return get_error_response(message=str(e))


@router.get("/feature-geographical-positions/{belongs_to}", response_model=featuregeographicalposition_schema.FeatureGeographicalPositionWithSynopFeatureResponse)
def get_feature_geographical_position_by_id(belongs_to: str, db_session: Session = Depends(deps.get_session)):
    try:
        return get_success_response(
            result=[featuregeographicalposition_service.get(db_session=db_session, belongs_to=belongs_to)],
            message="Successfully fetched feature_geographical_position."
        )
    except featuregeographicalposition_service.FailedGettingFeatureGeographicalPosition as e:
        return get_error_response(
            message=str(e)
        )


@router.post("/feature-geographical-positions", response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse)
def create_feature_geographical_position(data: featuregeographicalposition_schema.CreateFeatureGeographicalPosition, db_session: Session = Depends(deps.get_session)):
    try:
        return get_success_response(
            result=[featuregeographicalposition_service.create(db_session=db_session, data=data)],
            message="Successfully created feature_geographical_position."
        )
    except featuregeographicalposition_service.FailedCreatingFeatureGeographicalPosition as e:
        return get_error_response(
            message=str(e)
        )


@router.put("/feature-geographical-positions/{belongs_to}", response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse)
def update_feature_geographical_position(belongs_to: str, data: featuregeographicalposition_schema.UpdateFeatureGeographicalPosition, db_session: Session = Depends(deps.get_session)):
    try:
        return get_success_response(
            result=[featuregeographicalposition_service.update(db_session=db_session, belongs_to=belongs_to, updates=data)],
            message="Successfully updated feature_geographical_position."
        )
    except featuregeographicalposition_service.FailedUpdatingFeatureGeographicalPosition as e:
        return get_error_response(
            message=str(e)
        )


@router.delete("/feature-geographical-positions/{belongs_to}", response_model=featuregeographicalposition_schema.FeatureGeographicalPositionResponse)
def delete_feature_geographical_position(belongs_to: str, db_session: Session = Depends(deps.get_session)):
    try:
        featuregeographicalposition_service.delete(db_session=db_session, belongs_to=belongs_to)
        return get_success_response(
            result=[],
            message="Successfully deleted feature_geographical_position."
        )
    except featuregeographicalposition_service.FailedDeletingFeatureGeographicalPosition as e:
        return get_error_response(
            message=str(e)
        )
