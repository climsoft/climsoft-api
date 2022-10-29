import logging
from pathlib import Path
from fastapi import Response, Request
from climsoft_api.config import settings
from climsoft_api.middlewares.localization import LocalizationMiddleware
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from climsoft_api.api import api_routers
from climsoft_api.middlewares.auth import get_authorized_user
from sqlalchemy.orm import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models
from climsoft_api.utils.deployment import load_deployment_configs
from climsoft_api.db import get_session_local
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware import Middleware
from climsoft_api.api.auth import router as auth_router
from climsoft_api.api.config import router as config_router
# load controllers

deployment_configs = load_deployment_configs()


def get_app(config=None):
    app = FastAPI(docs_url="/")
    app.add_middleware(BaseHTTPMiddleware, dispatch=LocalizationMiddleware())
    if settings.MOUNT_STATIC:
        try:
            Path(settings.UPLOAD_DIR).mkdir(parents=True, exist_ok=True)
            app.mount(
                settings.UPLOAD_DIR,
                StaticFiles(directory=settings.UPLOAD_DIR),
                name="uploads"
            )
        except PermissionError as e:
            logging.getLogger(__file__).error(e)

    @app.middleware("http")
    async def db_session_middleware(request: Request, call_next):
        try:
            request.state.get_session = get_session_local(config)
            request.state.settings_override = deployment_configs.get(config)
            response = await call_next(request)
        except Exception as exc:
            logging.exception(exc)
            return Response("Internal server error", status_code=500)
        return response

    return app


def get_app_with_routers():
    app = FastAPI(
        middleware=[
            Middleware(
                CORSMiddleware,
                allow_origins=["*"],
                allow_credentials=True,
                allow_methods=["*"],
                allow_headers=["*"],
            )
        ]
    )
    app.include_router(auth_router.router)
    app.include_router(config_router.router)

    if deployment_configs:
        for key, config in deployment_configs.items():
            dependencies = [Depends(get_authorized_user)]
            climsoft_app = get_app(key)

            for r in api_routers:
                climsoft_app.include_router(
                    **r.dict(), dependencies=dependencies
                )

            app.mount(f"/{key}/climsoft", climsoft_app)
    else:
        climsoft_app = get_app()
        if settings.AUTH_ENABLED:
            dependencies = [Depends(get_authorized_user)]
        else:
            dependencies = []
        for r in api_routers:
            climsoft_app.include_router(
                **r.dict(), dependencies=dependencies
            )

        app.mount("/climsoft", climsoft_app)

    return app


app = get_app_with_routers()


def create_default_clim_user_roles(session: Session):
    clim_mysql_default_user_role = session.query(
        climsoft_models.ClimsoftUser
    ).filter_by(
        userName=settings.MYSQL_DEFAULT_USER
    ).one_or_none()

    if clim_mysql_default_user_role is None:
        clim_mysql_default_user_role = climsoft_models.ClimsoftUser(
            userName=settings.MYSQL_DEFAULT_USER,
            userRole="ClimsoftAdmin"
        )
        session.add(clim_mysql_default_user_role)
        session.commit()


@app.on_event("startup")
def create_default_user():
    if deployment_configs:
        for dk in deployment_configs:
            session = get_session_local(dk)()
            try:
                create_default_clim_user_roles(session)
            except Exception as e:
                session.rollback()
                logging.getLogger("ClimsoftLogger").exception(e)
            finally:
                session.close()
    else:
        session = get_session_local()()
        try:
            create_default_clim_user_roles(session)
        except Exception as e:
            session.rollback()
            logging.getLogger("ClimsoftLogger").exception(e)
        finally:
            session.close()
