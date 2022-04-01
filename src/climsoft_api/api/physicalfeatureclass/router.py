import \
    climsoft_api.api.physicalfeatureclass.schema as physicalfeatureclass_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import physicalfeatureclass_service
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
    "/physical-feature-class"
)
def get_physical_feature_class(
    feature_class: str = None,
    description: str = None,
    refers_to: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, physical_feature_class = physicalfeatureclass_service.query(
            db_session=db_session,
            feature_class=feature_class,
            description=description,
            refers_to=refers_to,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=physical_feature_class,
            message=_("Successfully fetched physical feature class."),
            schema=translate_schema(
                _,
                physicalfeatureclass_schema.PhysicalFeatureClassQueryResponse.schema()
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
    "/physical-feature-class/{feature_class}"
)
def get_physical_feature_class_by_id(
    feature_class: str, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                physicalfeatureclass_service.get(
                    db_session=db_session, feature_class=feature_class
                )
            ],
            message=_("Successfully fetched physical feature class."),
            schema=translate_schema(
                _,
                physicalfeatureclass_schema.PhysicalFeatureClassWithStationResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.post(
    "/physical-feature-class",
)
def create_physical_feature_class(
    data: physicalfeatureclass_schema.CreatePhysicalFeatureClass,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                physicalfeatureclass_service.create(
                    db_session=db_session,
                    data=data
                )
            ],
            message=_("Successfully created physical feature class."),
            schema=translate_schema(
                _,
                physicalfeatureclass_schema.PhysicalFeatureClassResponse.schema()
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


@router.put(
    "/physical-feature-class/{feature_class}"
)
def update_physical_feature_class(
    feature_class: str,
    data: physicalfeatureclass_schema.UpdatePhysicalFeatureClass,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                physicalfeatureclass_service.update(
                    db_session=db_session,
                    feature_class=feature_class,
                    updates=data
                )
            ],
            message=_("Successfully updated physical feature class."),
            schema=translate_schema(
                _,
                physicalfeatureclass_schema.PhysicalFeatureClassResponse.schema()
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
    "/physical-feature-class/{feature_class}"
)
def delete_physical_feature_class(
    feature_class: str, db_session: Session = Depends(deps.get_session)
):
    try:
        physicalfeatureclass_service.delete(
            db_session=db_session, feature_class=feature_class
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted physical feature class."),
            schema=translate_schema(
                _,
                physicalfeatureclass_schema.PhysicalFeatureClassResponse.schema()
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
