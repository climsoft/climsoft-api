import logging

import climsoft_api.api.physicalfeature.schema as physicalfeature_schema
from climsoft_api.api import deps
from climsoft_api.services import physicalfeature_service
from climsoft_api.utils.exception import handle_exceptions
from climsoft_api.utils.response import get_success_response, \
    get_success_response_for_query
from climsoft_api.utils.response import translate_schema
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get(
    "/physical-features"
)
@handle_exceptions
def get_physical_feature(
    associated_with: str = None,
    begin_date: str = None,
    end_date: str = None,
    image: str = None,
    description: str = None,
    classified_into: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, physical_feature = physicalfeature_service.query(
        db_session=db_session,
        associated_with=associated_with,
        begin_date=begin_date,
        end_date=end_date,
        image=image,
        description=description,
        classified_into=classified_into,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=physical_feature,
        message=_("Successfully fetched physical feature."),
        schema=translate_schema(
            _,
            physicalfeature_schema.PhysicalFeatureQueryResponse.schema()
        )
    )


@router.get(
    "/physical-features/{associated_with}/{begin_date}/{classified_into}"
)
@handle_exceptions
def get_physical_feature_by_id(
    associated_with: str,
    begin_date: str,
    classified_into: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            physicalfeature_service.get(
                db_session=db_session,
                associated_with=associated_with,
                begin_date=begin_date,
                classified_into=classified_into,
            )
        ],
        message=_("Successfully fetched physical feature."),
        schema=translate_schema(
            _,
            physicalfeature_schema.PhysicalFeatureWithStationAndPhysicalFeatureClassResponse.schema()
        )
    )


@router.post("/physical-features")
@handle_exceptions
def create_physical_feature(
    data: physicalfeature_schema.CreatePhysicalFeature,
    db_session: Session = Depends(deps.get_session)
):
    return get_success_response(
        result=[physicalfeature_service.create(
            db_session=db_session,
            data=data
        )],
        message=_("Successfully created physical feature."),
        schema=translate_schema(
            _,
            physicalfeature_schema.PhysicalFeatureResponse.schema()
        )
    )


@router.put(
    "/physical-features/{associated_with}/{begin_date}/{classified_into}"
)
@handle_exceptions
def update_physical_feature(
    associated_with: str,
    begin_date: str,
    classified_into: str,
    data: physicalfeature_schema.UpdatePhysicalFeature,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            physicalfeature_service.update(
                db_session=db_session,
                associated_with=associated_with,
                begin_date=begin_date,
                classified_into=classified_into,
                updates=data,
            )
        ],
        message=_("Successfully updated physical feature."),
        schema=translate_schema(
            _,
            physicalfeature_schema.PhysicalFeatureResponse.schema()
        )
    )


@router.delete(
    "/physical-features/{associated_with}/{begin_date}/{classified_into}"
)
@handle_exceptions
def delete_physical_feature(
    associated_with: str,
    begin_date: str,
    classified_into: str,
    db_session: Session = Depends(deps.get_session),
):
    physicalfeature_service.delete(
        db_session=db_session,
        associated_with=associated_with,
        begin_date=begin_date,
        classified_into=classified_into,
    )
    return get_success_response(
        result=[],
        message=_("Successfully deleted physical feature."),
        schema=translate_schema(
            _,
            physicalfeature_schema.PhysicalFeatureResponse.schema()
        )
    )
