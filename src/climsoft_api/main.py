import logging
from pathlib import Path
from climsoft_api.db import SessionLocal
from fastapi import Response, Request
from climsoft_api.api.acquisition_type.router import \
    router as acquisition_type_router
from climsoft_api.api.climsoftuser.router import router as climsoft_user_router
from climsoft_api.api.data_form.router import router as data_form_router
from climsoft_api.api.faultresolution.router import \
    router as faultresolution_router
from climsoft_api.api.featuregeographicalposition.router import (
    router as featuregeographicalposition_router,
)
from climsoft_api.api.flag.router import router as flag_router
from climsoft_api.api.instrument.router import router as instrument_router
from climsoft_api.api.instrumentfaultreport.router import (
    router as instrumentfaultreport_router,
)
from climsoft_api.api.instrumentinspection.router import (
    router as instrumentinspection_router,
)
from climsoft_api.api.obselement.router import router as obselement_router
from climsoft_api.api.observationfinal.router import \
    router as observationfinal_router
from climsoft_api.api.observationinitial.router import (
    router as observationinitial_router,
)
from climsoft_api.api.obsscheduleclass.router import \
    router as obsscheduleclass_router
from climsoft_api.api.paperarchive.router import router as paperarchive_router
from climsoft_api.api.paperarchivedefinition.router import (
    router as paperarchivedefinition_router,
)
from climsoft_api.api.physicalfeature.router import \
    router as physicalfeature_router
from climsoft_api.api.physicalfeatureclass.router import (
    router as physicalfeatureclass_router,
)
from climsoft_api.api.qcstatusdefinition.router import (
    router as qcstatusdefinition_router,
)
from climsoft_api.api.qctype.router import router as qctype_router
from climsoft_api.api.regkey.router import router as regkey_router
from climsoft_api.api.s3_files.router import router as s3_files_router
from climsoft_api.api.station.router import router as station_router
from climsoft_api.api.stationelement.router import \
    router as stationelement_router
from climsoft_api.api.stationlocationhistory.router import (
    router as stationlocationhistory_router,
)
from climsoft_api.api.stationqualifier.router import \
    router as stationqualifier_router
from climsoft_api.api.statistics.router import router as climsoft_stat_router
from climsoft_api.api.synopfeature.router import router as synopfeature_router
from climsoft_api.api.upload.router import router as file_upload_router
from climsoft_api.api.form_daily2.router import router as form_daily2_router
from climsoft_api.api.form_agro1.router import router as form_agro1_router
from climsoft_api.api.form_hourly.router import router as form_hourly_router
from climsoft_api.api.form_hourly_time_selection.router import router as form_hourly_time_selection_router

from climsoft_api.config import settings
from climsoft_api.middlewares.localization import LocalizationMiddleware
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from starlette.middleware.base import BaseHTTPMiddleware


# load controllers


def get_app():
    app = FastAPI(docs_url="/")
    app.add_middleware(BaseHTTPMiddleware, dispatch=LocalizationMiddleware())
    app.include_router(climsoft_stat_router, prefix="/v1", tags=["Table Stats"])
    app.include_router(file_upload_router, prefix="/v1",
                       tags=["File Upload"])
    app.include_router(s3_files_router, prefix="/v1", tags=["S3 Files"])
    app.include_router(climsoft_user_router, prefix="/v1",
                       tags=["Climsoft Users"])
    app.include_router(
        acquisition_type_router,
        prefix="/v1",
        tags=["Acquisition Type"],
    )
    app.include_router(data_form_router, prefix="/v1",
                       tags=["Data Forms"])
    app.include_router(
        faultresolution_router,
        prefix="/v1",
        tags=["Fault Resolutions"],
    )
    app.include_router(
        featuregeographicalposition_router,
        prefix="/v1",
        tags=["Feature Geographical Positions"],
    )
    app.include_router(flag_router, prefix="/v1", tags=["Flags"])
    app.include_router(
        instrument_router, prefix="/v1", tags=["Instruments"]
    )
    app.include_router(
        instrumentfaultreport_router,
        prefix="/v1",
        tags=["Instrument Fault Reports"],
    )
    app.include_router(
        instrumentinspection_router,
        prefix="/v1",
        tags=["Instruments Inspections"],
    )
    app.include_router(
        obselement_router, prefix="/v1", tags=["Obselements"]
    )
    app.include_router(
        observationfinal_router,
        prefix="/v1",
        tags=["Observation Finals"],
    )
    app.include_router(
        observationinitial_router,
        prefix="/v1",
        tags=["Observation Initials"],
    )
    app.include_router(
        obsscheduleclass_router,
        prefix="/v1",
        tags=["Obs Schedule Class"],
    )
    app.include_router(
        paperarchive_router,
        prefix="/v1",
        tags=["Paper Archives"]
    )
    app.include_router(
        paperarchivedefinition_router,
        prefix="/v1",
        tags=["Paper Archive Definitions"],
    )
    app.include_router(
        physicalfeature_router,
        prefix="/v1",
        tags=["Physical Features"],
    )
    app.include_router(
        physicalfeatureclass_router,
        prefix="/v1",
        tags=["Physical Feature Class"],
    )
    app.include_router(
        qcstatusdefinition_router,
        prefix="/v1",
        tags=["QC Status Definitions"],
    )
    app.include_router(qctype_router, prefix="/v1", tags=["QC Types"])
    app.include_router(regkey_router, prefix="/v1", tags=["Reg Keys"])
    app.include_router(station_router, prefix="/v1", tags=["Stations"])
    app.include_router(
        stationelement_router,
        prefix="/v1",
        tags=["Station Elements"]
    )
    app.include_router(
        stationlocationhistory_router,
        prefix="/v1",
        tags=["Station Location Histories"],
    )
    app.include_router(
        stationqualifier_router,
        prefix="/v1",
        tags=["Station Qualifiers"],
    )
    app.include_router(
        synopfeature_router,
        prefix="/v1",
        tags=["Synop Features"]
    )

    app.include_router(
        form_agro1_router,
        prefix="/v1",
        tags=["Form Agro1 2"]
    )

    app.include_router(
        form_daily2_router,
        prefix="/v1",
        tags=["Form Daily 2"]
    )

    app.include_router(
        form_hourly_router,
        prefix="/v1",
        tags=["Form Hourly"]
    )

    app.include_router(
        form_hourly_time_selection_router,
        prefix="/v1",
        tags=["Form Hourly Time Selection"]
    )
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


app = get_app()
