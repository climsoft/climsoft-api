import logging
from fastapi.security.oauth2 import OAuth2PasswordBearer
from climsoft_api.db import SessionLocal
from fastapi.exceptions import HTTPException
from fastapi import Request
from fastapi.security.utils import get_authorization_scheme_param
from jose.exceptions import JWTError
from starlette.types import Scope, Receive, Send, ASGIApp
from jose import jwt
from climsoft_api.config import settings
from climsoft_api.middlewares import rbac_config
from climsoft_api.api.schema import CurrentUser
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def get_climsoft_role_for_username(username: str):
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


def has_required_climsoft_role(username, required_role):
    return get_climsoft_role_for_username(username) in required_role


def extract_resource_from_path(string, sep, start, end):
    string = string.split(sep)
    return sep.join(string[start:end])


class ClimsoftRBACMiddleware():
    def __init__(self, app: ASGIApp):
        self.app = app

    def authenticate_request(self, request: Request):
        user = None
        authorization_header = request.headers.get("authorization")
        if authorization_header is None:
            raise HTTPException(401, "Unauthorized request")
        scheme, token = get_authorization_scheme_param(authorization_header)
        if scheme.lower() != "bearer":
            raise HTTPException(401, "Invalid authorization header scheme")
        try:
            claims = jwt.decode(token, settings.SURFACE_SECRET_KEY)
        except JWTError:
            raise HTTPException(401, "Unauthorized request")
        username = claims["sub"]
        if claims.get("deployment_key"):
            user = CurrentUser(username=username)
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

        if (not required_role) or has_required_climsoft_role(user.username, required_role):
            await self.app(scope, receive, send)
        else:
            raise HTTPException(status_code=403)


def get_authorized_climsoft_user(
    request: Request, token: str = Depends(oauth2_scheme)
):
    user = None
    try:
        claims = jwt.decode(token, settings.SURFACE_SECRET_KEY)
    except JWTError:
        raise HTTPException(401, "Unauthorized request")

    username = claims["sub"]

    if claims.get("deployment_key"):
        user = CurrentUser(username=username)

    if user is None:
        raise HTTPException(401, "Unauthorized request")

    resource_url = extract_resource_from_path(request.url.path, "/", 3, 4)
    required_role = rbac_config.required_role_lookup.get(resource_url, {}).get(
        request.method.lower()
    )

    if required_role and not has_required_climsoft_role(user.username, required_role):
        raise HTTPException(status_code=403)

    return user
