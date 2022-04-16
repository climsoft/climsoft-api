import climsoft_api.api.physicalfeature.schema as physicalfeature_schema
import fastapi
import backoff
import sqlalchemy.exc
from climsoft_api.api import deps
from climsoft_api.services import physicalfeature_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get(
    "/physical-features"
)
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
            result=physical_feature,
            message=_("Successfully fetched physical feature."),
            schema=translate_schema(
                _,
                physicalfeature_schema.PhysicalFeatureQueryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.get(
    "/physical-features/{associated_with}/{begin_date}/{classified_into}/{description}"
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
            message=_("Successfully fetched physical feature."),
            schema=translate_schema(
                _,
                physicalfeature_schema.PhysicalFeatureWithStationAndPhysicalFeatureClassResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
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
    "/physical-features/{associated_with}/{begin_date}/{classified_into}/{description}"
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
            message=_("Successfully updated physical feature."),
            schema=translate_schema(
                _,
                physicalfeature_schema.PhysicalFeatureResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.delete(
    "/physical-features/{associated_with}/{begin_date}/{classified_into}/{description}"
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
            result=[],
            message=_("Successfully deleted physical feature."),
            schema=translate_schema(
                _,
                physicalfeature_schema.PhysicalFeatureResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        db_session.rollback()
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )
