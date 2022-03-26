import climsoft_api.api.regkey.schema as regkey_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import regkey_service
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
def get_reg_keys(
    key_name: str = None,
    key_value: str = None,
    key_description: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
        total, reg_keys = regkey_service.query(
            db_session=db_session,
            key_name=key_name,
            key_value=key_value,
            key_description=key_description,
            limit=limit,
            offset=offset,
        )

        return get_success_response_for_query(
            limit=limit,
            total=total,
            offset=offset,
            result=reg_keys,
            message=_("Successfully fetched reg keys."),
            schema=translate_schema(
                _,
                regkey_schema.RegKeyQueryResponse.schema()
            )
        )
    except fastapi.HTTPException:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=str(e)
        )


@router.get("/{key_name}")
def get_reg_key_by_id(
    key_name: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[
                regkey_service.get(
                    db_session=db_session,
                    key_name=key_name
                )
            ],
            message=_("Successfully fetched reg key."),
            schema=translate_schema(
                _,
                regkey_schema.RegKeyResponse.schema()
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
def create_reg_key(
    data: regkey_schema.CreateRegKey,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[regkey_service.create(db_session=db_session, data=data)],
            message=_("Successfully created reg key."),
            schema=translate_schema(
                _,
                regkey_schema.RegKeyResponse.schema()
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


@router.put("/{key_name}")
def update_reg_key(
    key_name: str,
    data: regkey_schema.UpdateRegKey,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                regkey_service.update(
                    db_session=db_session, key_name=key_name, updates=data
                )
            ],
            message=_("Successfully updated reg key."),
            schema=translate_schema(
                _,
                regkey_schema.RegKeyResponse.schema()
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


@router.delete("/{key_name}")
def delete_reg_key(
    key_name: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        regkey_service.delete(db_session=db_session, key_name=key_name)
        return get_success_response(
            result=[],
            message=_("Successfully deleted reg key."),
            schema=translate_schema(
                _,
                regkey_schema.RegKeyResponse.schema()
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
