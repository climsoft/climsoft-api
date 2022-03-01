from fastapi import APIRouter, Depends
from climsoft_api.services import climsoftuser_service
import climsoft_api.api.climsoftuser.schema as climsoft_user_schema
from climsoft_api.utils.response import get_success_response, get_error_response, get_success_response_for_query
from sqlalchemy.orm.session import Session
from climsoft_api.api import deps


router = APIRouter()


@router.get(
    "/",
    response_model=climsoft_user_schema.ClimsoftUserQueryResponse
)
def get_climsoft_users(
    username: str = None,
    role: str = None,
    limit: int = 25,
    offset: int = 0,
    db_session: Session = Depends(deps.get_session),
):
    try:
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
            message=_("Successfully fetched climsoft users.")
        )
    except climsoftuser_service.FailedGettingClimsoftUserList as e:
        return get_error_response(message=str(e))


@router.get("/{username}", response_model=climsoft_user_schema.ClimsoftUserResponse)
def get_climsoft_user_by_username(
    username: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        return get_success_response(
            result=[climsoftuser_service.get(
                db_session=db_session,
                username=username
            )],
            message=_("Successfully fetched climsoft user."),
        )
    except climsoftuser_service.FailedGettingClimsoftUser as e:
        return get_error_response(message=str(e))


@router.post("/", response_model=climsoft_user_schema.ClimsoftUserResponse)
def create_climsoft_user(
    data: climsoft_user_schema.CreateClimsoftUser,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[climsoftuser_service.create(
                db_session=db_session,
                data=data
            )],
            message=_("Successfully created climsoft user."),
        )
    except climsoftuser_service.FailedCreatingClimsoftUser as e:
        return get_error_response(message=str(e))


@router.put(
    "/{username}/update-role/{role}",
    response_model=climsoft_user_schema.ClimsoftUserResponse
)
def update_climsoft_user(
    username: str,
    role: str,
    db_session: Session = Depends(deps.get_session),
):
    try:
        return get_success_response(
            result=[
                climsoftuser_service.update(
                    db_session=db_session, username=username, role=role
                )
            ],
            message=_("Successfully updated climsoft user."),
        )
    except climsoftuser_service.FailedUpdatingClimsoftUser as e:
        return get_error_response(message=str(e))


@router.delete(
    "/{username}",
    response_model=climsoft_user_schema.ClimsoftUserResponse
)
def delete_climsoft_user(
    username: str,
    db_session: Session = Depends(deps.get_session)
):
    try:
        climsoftuser_service.delete(db_session=db_session, username=username)
        return get_success_response(
            result=[],
            message=_("Successfully deleted climsoft user.")
        )
    except climsoftuser_service.FailedDeletingClimsoftUser as e:
        return get_error_response(message=str(e))
