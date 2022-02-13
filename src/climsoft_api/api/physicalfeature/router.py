from fastapi import APIRouter, Depends
from climsoft_api.services import physicalfeature_service
import climsoft_api.api.physicalfeature.schema as physicalfeature_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps

router = APIRouter()


@router.get("/", response_model=physicalfeature_schema.PhysicalFeatureQueryResponse)
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
    try:
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
            result=physical_feature, message="Successfully fetched physical_feature."
        )
    except physicalfeature_service.FailedGettingPhysicalFeatureList as e:
        return get_error_response(message=str(e))


@router.get(
    "/{associated_with}/{begin_date}/{classified_into}/{description}",
    response_model=physicalfeature_schema.PhysicalFeatureWithStationAndPhysicalFeatureClassResponse,
)
def get_physical_feature_by_id(
    associated_with: str,
    begin_date: str,
    classified_into: str,
    description: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                physicalfeature_service.get(
                    db_session=db_session,
                    associated_with=associated_with,
                    begin_date=begin_date,
                    classified_into=classified_into,
                    description=description,
                )
            ],
            message="Successfully fetched physical_feature.",
        )
    except physicalfeature_service.FailedGettingPhysicalFeature as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=physicalfeature_schema.PhysicalFeatureResponse)
def create_physical_feature(
    data: physicalfeature_schema.CreatePhysicalFeature,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[physicalfeature_service.create(db_session=db_session, data=data)],
            message="Successfully created physical_feature.",
        )
    except physicalfeature_service.FailedCreatingPhysicalFeature as e:
        return get_error_response(message=str(e))


@router.put(
    "/{associated_with}/{begin_date}/{classified_into}/{description}",
    response_model=physicalfeature_schema.PhysicalFeatureResponse,
)
def update_physical_feature(
    associated_with: str,
    begin_date: str,
    classified_into: str,
    description: str,
    data: physicalfeature_schema.UpdatePhysicalFeature,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                physicalfeature_service.update(
                    db_session=db_session,
                    associated_with=associated_with,
                    begin_date=begin_date,
                    classified_into=classified_into,
                    description=description,
                    updates=data,
                )
            ],
            message="Successfully updated physical_feature.",
        )
    except physicalfeature_service.FailedUpdatingPhysicalFeature as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{associated_with}/{begin_date}/{classified_into}/{description}",
    response_model=physicalfeature_schema.PhysicalFeatureResponse,
)
def delete_physical_feature(
    associated_with: str,
    begin_date: str,
    classified_into: str,
    description: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        physicalfeature_service.delete(
            db_session=db_session,
            associated_with=associated_with,
            begin_date=begin_date,
            classified_into=classified_into,
            description=description,
        )
        return get_success_response(
            result=[], message="Successfully deleted physical_feature."
        )
    except physicalfeature_service.FailedDeletingPhysicalFeature as e:
        return get_error_response(message=str(e))
