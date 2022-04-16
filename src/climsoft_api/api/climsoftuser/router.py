import climsoft_api.api.climsoftuser.schema as climsoft_user_schema
import fastapi
from climsoft_api.api import deps
from climsoft_api.services import climsoftuser_service
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
    "/climsoft-users"
)
@handle_exceptions
def get_climsoft_users(
    username: str = None,
    role: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    total, climsoft_users = climsoftuser_service.query(
        db_session=db_session,
        username=username,
        role=role,
        limit=limit,
        offset=offset,
    )

    return get_success_response_for_query(
        limit=limit,
        total=total,
        offset=offset,
        result=climsoft_users,
        message=_("Successfully fetched climsoft users."),
        schema=translate_schema(
            _,
            climsoft_user_schema.ClimsoftUserQueryResponse.schema()
        )
    )


@router.get("/climsoft-users/{username}")
@handle_exceptions
def get_climsoft_user_by_username(
    username: str,
    db_session: Session = Depends(deps.get_session)
):

    return get_success_response(
        result=[climsoftuser_service.get(
            db_session=db_session,
            username=username
        )],
        message=_("Successfully fetched climsoft user."),
        schema=translate_schema(
            _,
            climsoft_user_schema.ClimsoftUserResponse.schema()
        )
    )


@router.post("/climsoft-users")
@handle_exceptions
def create_climsoft_user(
    data: climsoft_user_schema.CreateClimsoftUser,
    db_session: Session = Depends(deps.get_session),
):

    return get_success_response(
        result=[climsoftuser_service.create(
            db_session=db_session,
            data=data
        )],
        message=_("Successfully created climsoft user."),
        schema=translate_schema(
            _,
            climsoft_user_schema.ClimsoftUserResponse.schema()
        )
    )


@router.put(
    "/climsoft-users/{username}/update-role/{role}"
)
@handle_exceptions
def update_climsoft_user(
    username: str,
    role: str,
    db_session: Session = Depends(deps.get_session),
):
    return get_success_response(
        result=[
            climsoftuser_service.update(
                db_session=db_session, username=username, role=role
            )
        ],
        message=_("Successfully updated climsoft user."),
        schema=translate_schema(
            _,
            climsoft_user_schema.ClimsoftUserResponse.schema()
        )
    )


@router.delete(
    "/climsoft-users/{username}"
)
@handle_exceptions
def delete_climsoft_user(
    username: str,
    db_session: Session = Depends(deps.get_session)
):
    climsoftuser_service.delete(db_session=db_session, username=username)
    return get_success_response(
        result=[],
        message=_("Successfully deleted climsoft user."),
        schema=translate_schema(
            _,
            climsoft_user_schema.ClimsoftUserResponse.schema()
        )
    )
