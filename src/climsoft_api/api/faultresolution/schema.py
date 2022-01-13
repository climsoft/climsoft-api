import datetime

from pydantic import constr
from climsoft_api.api.schema import Response, BaseSchema
from typing import List
import climsoft_api.api.instrumentfaultreport.schema as instrumentfaultreport_schema


class CreateFaultResolution(BaseSchema):
    resolvedDatetime: constr(max_length=50)
    associatedWith: constr(max_length=255)
    resolvedBy: constr(max_length=255)
    remarks: constr(max_length=255)


class UpdateFaultResolution(BaseSchema):
    resolvedBy: constr(max_length=255)
    remarks: constr(max_length=255)


class FaultResolution(CreateFaultResolution):
    resolvedDatetime = datetime.datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class FaultResolutionWithInstrumentFaultReport(FaultResolution):
    instrumentfaultreport: instrumentfaultreport_schema.InstrumentFaultReport


class FaultResolutionResponse(Response):
    result: List[FaultResolution]


class FaultResolutionWithInstrumentFaultReportResponse(Response):
    result: List[FaultResolutionWithInstrumentFaultReport]
