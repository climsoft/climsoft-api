import logging
from pathlib import Path
from climsoft_api.db import SessionLocal
from fastapi import Response, Request
from climsoft_api.config import settings
from climsoft_api.middlewares.localization import LocalizationMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware
from climsoft_api.api import api_routers

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
        except: # noqa
            return Response("Internal server error", status_code=500)
        return response

    return app


def get_app_with_routers():
    app = get_app()
    for router in api_routers:
        app.include_router(**router.dict())

    return app


app = get_app_with_routers()
