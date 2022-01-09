import datetime

from pydantic import constr
from climsoft_api.api.schema import Response, BaseSchema
from typing import List
import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.station.schema as station_schema


class CreateInstrumentFaultReport(BaseSchema):
    refersTo: constr(max_length=255)
    reportId: int
    reportDatetime: constr(max_length=50)
    faultDescription: constr(max_length=255)
    reportedBy: constr(max_length=255)
    receivedDatetime: constr(max_length=50)
    receivedBy: constr(max_length=255)
    reportedFrom: constr(max_length=255)


class UpdateInstrumentFaultReport(BaseSchema):
    refersTo: constr(max_length=255)
    reportDatetime: constr(max_length=50)
    faultDescription: constr(max_length=255)
    reportedBy: constr(max_length=255)
    receivedDatetime: constr(max_length=50)
    receivedBy: constr(max_length=255)
    reportedFrom: constr(max_length=255)


class InstrumentFaultReport(CreateInstrumentFaultReport):
    reportDatetime: datetime.datetime
    receivedDatetime: datetime.datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class InstrumentFaultReportWithStationAndInstrument(InstrumentFaultReport):
    station: station_schema.Station
    instrument: instrument_schema.Instrument


class InstrumentFaultReportResponse(Response):
    result: List[InstrumentFaultReport]


class InstrumentFaultReportWithStationAndInstrumentResponse(Response):
    result: List[InstrumentFaultReportWithStationAndInstrument]
