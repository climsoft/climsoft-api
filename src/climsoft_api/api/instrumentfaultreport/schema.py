import datetime
from typing import List

import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateInstrumentFaultReport(BaseSchema):
    refersTo: constr(max_length=255) = Field(title=_("Refers To"))
    reportId: int = Field(title=_("Report ID"))
    reportDatetime: constr(max_length=50) = Field(title=_("Report Datetime"))
    faultDescription: constr(max_length=255) = Field(title=_("Fault Description"))
    reportedBy: constr(max_length=255) = Field(title=_("Reported By"))
    receivedDatetime: constr(max_length=50) = Field(title=_("Received Datetime"))
    receivedBy: constr(max_length=255) = Field(title=_("Received By"))
    reportedFrom: constr(max_length=255) = Field(title=_("Reported From"))

    class Config:
        fields = {
            "refersTo": "refers_to",
            "reportId": "report_id",
            "reportDatetime": "report_datetime",
            "faultDescription": "fault_description",
            "reportedBy": "reported_by",
            "receivedDatetime": "received_datetime",
            "receivedBy": "received_by",
            "reportedFrom": "reported_from"
        }


class UpdateInstrumentFaultReport(BaseSchema):
    refersTo: constr(max_length=255) = Field(title=_("Refers To"))
    reportDatetime: constr(max_length=50) = Field(title=_("Report Datetime"))
    faultDescription: constr(max_length=255) = Field(title=_("Fault Description"))
    reportedBy: constr(max_length=255) = Field(title=_("Reported By"))
    receivedDatetime: constr(max_length=50) = Field(title=_("Received Datetime"))
    receivedBy: constr(max_length=255) = Field(title=_("Received By"))
    reportedFrom: constr(max_length=255) = Field(title=_("Reported From"))

    class Config:
        fields = {
            "refersTo": "refers_to",
            "reportId": "report_id",
            "reportDatetime": "report_datetime",
            "faultDescription": "fault_description",
            "reportedBy": "reported_by",
            "receivedDatetime": "received_datetime",
            "receivedBy": "received_by",
            "reportedFrom": "reported_from"
        }


class InstrumentFaultReport(CreateInstrumentFaultReport):
    reportDatetime: datetime.datetime = Field(title=_("Report Datetime"))
    receivedDatetime: datetime.datetime = Field(title=_("Received Datetime"))

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "refersTo": "refers_to",
            "reportId": "report_id",
            "reportDatetime": "report_datetime",
            "faultDescription": "fault_description",
            "reportedBy": "reported_by",
            "receivedDatetime": "received_datetime",
            "receivedBy": "received_by",
            "reportedFrom": "reported_from"
        }


class InstrumentFaultReportWithStationAndInstrument(InstrumentFaultReport):
    station: station_schema.Station = Field(title=_("Station"))
    instrument: instrument_schema.Instrument = Field(title=_("Instrument"))


class InstrumentFaultReportResponse(Response):
    result: List[InstrumentFaultReport] = Field(title=_("Result"))


class InstrumentFaultReportWithStationAndInstrumentResponse(Response):
    result: List[InstrumentFaultReportWithStationAndInstrument] = Field(title=_("Result"))


class InstrumentFaultReportQueryResponse(InstrumentFaultReportResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
