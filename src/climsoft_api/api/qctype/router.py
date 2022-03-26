import climsoft_api.api.qctype.schema as qctype_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import qctype_service
from climsoft_api.utils.response import get_success_response, \
    get_error_response, get_success_response_for_query
from fastapi import APIRouter, Depends
from sqlalchemy.orm.session import Session
from climsoft_api.utils.response import translate_schema
import logging

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


@router.get("/")
def get_qc_types(
    code: str = None,
    description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, qc_types = qctype_service.query(
            db_session=db_session,
            code=code,
            description=description,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=qc_types,
            message=_("Successfully fetched qc types."),
            schema=translate_schema(
                _,
                qctype_schema.QCTypeQueryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.get("/{code}")
def get_qc_type_by_id(
    code: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[qctype_service.get(db_session=db_session, code=code)],
            message=_("Successfully fetched qc type."),
            schema=translate_schema(
                _,
                qctype_schema.QCTypeResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.post("/")
def create_qc_type(
    data: qctype_schema.CreateQCType,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[qctype_service.create(db_session=db_session, data=data)],
            message=_("Successfully created qc type."),
            schema=translate_schema(
                _,
                qctype_schema.QCTypeResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.put("/{code}")
def update_qc_type(
    code: str,
    data: qctype_schema.UpdateQCType,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                qctype_service.update(
                    db_session=db_session,
                    code=code,
                    updates=data
                )
            ],
            message=_("Successfully updated qc type."),
            schema=translate_schema(
                _,
                qctype_schema.QCTypeResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.delete("/{code}", response_model=qctype_schema.QCTypeResponse)
def delete_qc_type(code: str, db_session: Session = Depends(deps.get_session)):
    try:
        qctype_service.delete(db_session=db_session, code=code)
        return get_success_response(
            result=[],
            message=_("Successfully deleted qc type."),
            schema=translate_schema(
                _,
                qctype_schema.QCTypeResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )
