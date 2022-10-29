import logging
from fastapi.exceptions import HTTPException
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from jose.exceptions import JWTError
from starlette.types import Scope, Receive, Send, ASGIApp
from jose import jwt
from climsoft_api.config import settings
from climsoft_api.db import get_session_local
from climsoft_api.middlewares import rbac_config
from climsoft_api.api.schema import CurrentUser
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from climsoft_api.utils.deployment import load_deployment_configs


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/token",
    scopes={
        f"deployment_key:{key}": f"DB access to deployment key: {key}"
        for key in load_deployment_configs()
    },
)


def get_role_for_username(username: str, deployment_key: str = None):
    SessionLocal = get_session_local(deployment_key)
    session = SessionLocal()

    role = None

    try:
        user_role = (
            session.query(climsoft_models.ClimsoftUser)
            .filter_by(userName=username)
            .one_or_none()
        )
        role = user_role.userRole
    except Exception as e:
        logging.exception(e)
        pass
    finally:
        session.close()

    return role


def has_required_climsoft_role(username, required_role, deployment_key=None):
    return get_role_for_username(username, deployment_key) in required_role


def extract_resource_from_path(string, sep, start, end):
    string = string.split(sep)
    return sep.join(string[start:end])


class ClimsoftRBACMiddleware:
    def __init__(self, app: ASGIApp):
        super().__init__(app)

    def authenticate_request(self, request: Request):
        user = None
        authorization_header = request.headers.get("authorization")
        if authorization_header is None:
            raise HTTPException(401, "Unauthorized request")
        scheme, token = get_authorization_scheme_param(authorization_header)
        if scheme.lower() != "bearer":
            raise HTTPException(401, "Invalid authorization header scheme")
        try:
            claims = jwt.decode(token, settings.SECRET_KEY)
        except JWTError:
            raise HTTPException(401, "Unauthorized request")
        username = claims["sub"]
        if claims.get("deployment_key"):
            user = CurrentUser(
                username=username, deployment_key=claims.get("deployment_key")
            )
        if user is None:
            raise HTTPException(401, "Unauthorized request")
        return user

    async def __call__(self, scope: Scope, receive: Receive, send: Send):
        request = Request(scope, receive, send)
        user = None
        if request.url.path not in {
            "/climsoft",
            "/climsoft/openapi.json",
            "/climsoft/",
        }:
            user = self.authenticate_request(request)

        resource_url = extract_resource_from_path(request.url.path, "/", 3, 4)
        required_role = rbac_config.required_role_lookup.get(
            resource_url, {}
        ).get(request.method.lower())

        if (not required_role) or has_required_climsoft_role(
            user.username, required_role, user.deployment_key
        ):
            await self.app(scope, receive, send)
        else:
            raise HTTPException(status_code=403)


def get_authorized_user(
    request: Request, token: str = Depends(oauth2_scheme)
):
    user = None
    try:
        claims = jwt.decode(token, settings.SECRET_KEY)
    except JWTError:
        raise HTTPException(401, "Unauthorized request")

    username = claims["sub"]

    user = CurrentUser(
        username=username, deployment_key=claims.get("deployment_key")
    )

    if user is None:
        raise HTTPException(401, "Unauthorized request")

    resource_url = extract_resource_from_path(request.url.path, "/", 3, 4)
    required_role = rbac_config.required_role_lookup.get(resource_url, {}).get(
        request.method.lower()
    )

    if required_role and not has_required_climsoft_role(
        user.username, required_role, user.deployment_key
    ):
        raise HTTPException(status_code=403)

    return user
