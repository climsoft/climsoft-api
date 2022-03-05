import climsoft_api.api.synopfeature.schema as synopfeature_schema
from climsoft_api.api import deps
from climsoft_api.services import synopfeature_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session

router = APIRouter()


@router.get("/", response_model=synopfeature_schema.SynopFeatureQueryResponse)
def get_qc_types(
    abbreviation: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, qc_types = synopfeature_service.query(
            db_session=db_session,
            abbreviation=abbreviation,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=qc_types, message=_("Successfully fetched synop features.")
        )
    except synopfeature_service.FailedGettingSynopFeatureList as e:
        return get_error_response(message=str(e))


@router.get("/{abbreviation}",
            response_model=synopfeature_schema.SynopFeatureResponse)
def get_qc_type_by_id(
    abbreviation: str, db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                synopfeature_service.get(
                    db_session=db_session, abbreviation=abbreviation
                )
            ],
            message=_("Successfully fetched synop feature."),
        )
    except synopfeature_service.FailedGettingSynopFeature as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=synopfeature_schema.SynopFeatureResponse)
def create_qc_type(
    data: synopfeature_schema.CreateSynopFeature,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                synopfeature_service.create(db_session=db_session, data=data)],
            message=_("Successfully created synop feature."),
        )
    except synopfeature_service.FailedCreatingSynopFeature as e:
        return get_error_response(message=str(e))


@router.put("/{abbreviation}",
            response_model=synopfeature_schema.SynopFeatureResponse)
def update_qc_type(
    abbreviation: str,
    data: synopfeature_schema.UpdateSynopFeature,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                synopfeature_service.update(
                    db_session=db_session,
                    abbreviation=abbreviation,
                    updates=data
                )
            ],
            message=_("Successfully updated synop feature."),
        )
    except synopfeature_service.FailedUpdatingSynopFeature as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{abbreviation}", response_model=synopfeature_schema.SynopFeatureResponse
)
def delete_qc_type(abbreviation: str,
                   db_session: Session = Depends(deps.get_session)):
    try:
        synopfeature_service.delete(
            db_session=db_session,
            abbreviation=abbreviation
        )
        return get_success_response(
            result=[],
            message=_("Successfully deleted synop feature.")
        )
    except synopfeature_service.FailedDeletingSynopFeature as e:
        return get_error_response(message=str(e))
