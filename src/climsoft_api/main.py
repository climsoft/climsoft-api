import logging
from pathlib import Path
from climsoft_api.db import SessionLocal
from fastapi import Response, Request
from climsoft_api.config import settings
from climsoft_api.middlewares.localization import LocalizationMiddleware
from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from climsoft_api.api import api_routers
from climsoft_api.middlewares.auth import get_authorized_climsoft_user
from sqlalchemy.orm import Session
from opencdms.models.climsoft import v4_1_1_core as climsoft_models

# load controllers


def get_app():
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
            request.state.get_session = SessionLocal
            response = await call_next(request)
        except Exception as exc:
            logging.exception(exc)
            return Response("Internal server error", status_code=500)
        return response

    return app


def get_app_with_routers():
    app = get_app()
    for router in api_routers:
        app.include_router(**router.dict(), dependencies=[Depends(get_authorized_climsoft_user)])

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
    session: Session = SessionLocal()
    try:
        create_default_clim_user_roles(session)
    except Exception as e:
        session.rollback()
        logging.getLogger("OpenCDMSLogger").exception(e)
    finally:
        session.close()
    return app
