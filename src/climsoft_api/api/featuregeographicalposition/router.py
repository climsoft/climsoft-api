import \
    climsoft_api.api.featuregeographicalposition.schema as featuregeographicalposition_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import featuregeographicalposition_service
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
    "/feature-geographical-positions"
)
@handle_exceptions
def get_feature_geographical_positions(
    belongs_to: str = None,
    observed_on: str = None,
    latitude: float = None,
    longitude: float = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
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
        schema=translate_schema(
            _,
            featuregeographicalposition_schema.FeatureGeographicalPositionQueryResponse.schema(),
        )
    )


@router.get(
    "/feature-geographical-positions/{belongs_to}",
)
@handle_exceptions
def get_feature_geographical_position_by_id(
    belongs_to: str,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[
            featuregeographicalposition_service.get(
                db_session=db_session, belongs_to=belongs_to
            )
        ],
        message=_("Successfully fetched feature geographical position."),
        schema=translate_schema(
            _,
            featuregeographicalposition_schema.FeatureGeographicalPositionWithSynopFeatureResponse.schema()
        )
    )


@router.post(
    "/feature-geographical-positions"
)
@handle_exceptions
def create_feature_geographical_position(
    data: featuregeographicalposition_schema.CreateFeatureGeographicalPosition,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            featuregeographicalposition_service.create(
                db_session=db_session, data=data
            )
        ],
        message=_("Successfully created feature geographical position."),
        schema=translate_schema(
            _,
            featuregeographicalposition_schema.FeatureGeographicalPositionResponse.schema(),
        )
    )


@router.put(
    "/feature-geographical-positions/{belongs_to}"
)
@handle_exceptions
def update_feature_geographical_position(
    belongs_to: str,
    data: featuregeographicalposition_schema.UpdateFeatureGeographicalPosition,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            featuregeographicalposition_service.update(
                db_session=db_session,
                belongs_to=belongs_to,
                updates=data
            )
        ],
        message=_("Successfully updated feature geographical position."),
        schema=translate_schema(
            _,
            featuregeographicalposition_schema.FeatureGeographicalPositionResponse.schema()
        )
    )


@router.delete(
    "/feature-geographical-positions/{belongs_to}"
)
@handle_exceptions
def delete_feature_geographical_position(
    belongs_to: str, db_session: Session = Depends(deps.get_session)
):
    featuregeographicalposition_service.delete(
        db_session=db_session,
        belongs_to=belongs_to
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted feature geographical position."),
        schema=translate_schema(
            _,
            featuregeographicalposition_schema.FeatureGeographicalPositionResponse.schema()
        )
    )
