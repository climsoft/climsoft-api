from typing import List

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
from climsoft_api.api.form_daily2.router import router as form_daily2_router
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
from fastapi import APIRouter
from pydantic import BaseModel


class ClimsoftAPIRouter(BaseModel):
    router: APIRouter
    prefix: str
    tags: List[str]

    class Config:
        arbitrary_types_allowed = True


api_routers: List[ClimsoftAPIRouter] = [
    ClimsoftAPIRouter(
        router=climsoft_stat_router,
        prefix="/v1",
        tags=["Table Stats"]
    ),
    ClimsoftAPIRouter(
        router=file_upload_router,
        prefix="/v1",
        tags=["File Upload"]
    ),
    ClimsoftAPIRouter(router=s3_files_router, prefix="/v1", tags=["S3 Files"]),
    ClimsoftAPIRouter(
        router=climsoft_user_router,
        prefix="/v1",
        tags=["Climsoft Users"]
    ),
    ClimsoftAPIRouter(
        router=acquisition_type_router,
        prefix="/v1",
        tags=["Acquisition Type"],
    ),
    ClimsoftAPIRouter(
        router=data_form_router, prefix="/v1",tags=["Data Forms"]),
    ClimsoftAPIRouter(
        router=faultresolution_router,
        prefix="/v1",
        tags=["Fault Resolutions"],
    ),
    ClimsoftAPIRouter(
        router=featuregeographicalposition_router,
        prefix="/v1",
        tags=["Feature Geographical Positions"],
    ),
    ClimsoftAPIRouter(router=flag_router, prefix="/v1", tags=["Flags"]),
    ClimsoftAPIRouter(
        router=instrument_router, prefix="/v1", tags=["Instruments"]
    ),
    ClimsoftAPIRouter(
        router=instrumentfaultreport_router,
        prefix="/v1",
        tags=["Instrument Fault Reports"],
    ),
    ClimsoftAPIRouter(
        router=instrumentinspection_router,
        prefix="/v1",
        tags=["Instruments Inspections"],
    ),
    ClimsoftAPIRouter(
        router=obselement_router, prefix="/v1", tags=["Obselements"]
    ),
    ClimsoftAPIRouter(
        router=observationfinal_router,
        prefix="/v1",
        tags=["Observation Finals"],
    ),
    ClimsoftAPIRouter(
        router=observationinitial_router,
        prefix="/v1",
        tags=["Observation Initials"],
    ),
    ClimsoftAPIRouter(
        router=obsscheduleclass_router,
        prefix="/v1",
        tags=["Obs Schedule Class"],
    ),
    ClimsoftAPIRouter(
        router=paperarchive_router,
        prefix="/v1",
        tags=["Paper Archives"]
    ),
    ClimsoftAPIRouter(
        router=paperarchivedefinition_router,
        prefix="/v1",
        tags=["Paper Archive Definitions"],
    ),
    ClimsoftAPIRouter(
        router=physicalfeature_router,
        prefix="/v1",
        tags=["Physical Features"],
    ),
    ClimsoftAPIRouter(
        router=physicalfeatureclass_router,
        prefix="/v1",
        tags=["Physical Feature Class"],
    ),
    ClimsoftAPIRouter(
        router=qcstatusdefinition_router,
        prefix="/v1",
        tags=["QC Status Definitions"],
    ),
    ClimsoftAPIRouter(
        router=qctype_router, prefix="/v1", tags=["QC Types"]
    ),
    ClimsoftAPIRouter(
        router=regkey_router, prefix="/v1", tags=["Reg Keys"]
    ),
    ClimsoftAPIRouter(
        router=station_router, prefix="/v1", tags=["Stations"]
    ),
    ClimsoftAPIRouter(
        router=stationelement_router,
        prefix="/v1",
        tags=["Station Elements"]
    ),
    ClimsoftAPIRouter(
        router=stationlocationhistory_router,
        prefix="/v1",
        tags=["Station Location Histories"],
    ),
    ClimsoftAPIRouter(
        router=stationqualifier_router,
        prefix="/v1",
        tags=["Station Qualifiers"],
    ),
    ClimsoftAPIRouter(
        router=synopfeature_router,
        prefix="/v1",
        tags=["Synop Features"]
    ),
    ClimsoftAPIRouter(
        router=form_daily2_router,
        prefix="/v1",
        tags=["Form Daily 2"]
    ),

]
