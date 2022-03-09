import datetime
from typing import List

import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateInstrumentFaultReport(BaseSchema):
    refersTo: constr(max_length=255) = Field(title="Refers To")
    reportId: int = Field(title="Report ID")
    reportDatetime: constr(max_length=50) = Field(title="Report Datetime")
    faultDescription: constr(max_length=255) = Field(title="Fault Description")
    reportedBy: constr(max_length=255) = Field(title="Reported By")
    receivedDatetime: constr(max_length=50) = Field(title="Received Datetime")
    receivedBy: constr(max_length=255) = Field(title="Received By")
    reportedFrom: constr(max_length=255) = Field(title="Reported From")

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
    refersTo: constr(max_length=255) = Field(title="Refers To")
    reportDatetime: constr(max_length=50) = Field(title="Report Datetime")
    faultDescription: constr(max_length=255) = Field(title="Fault Description")
    reportedBy: constr(max_length=255) = Field(title="Reported By")
    receivedDatetime: constr(max_length=50) = Field(title="Received Datetime")
    receivedBy: constr(max_length=255) = Field(title="Received By")
    reportedFrom: constr(max_length=255) = Field(title="Reported From")

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
    reportDatetime: datetime.datetime = Field(title="Report Datetime")
    receivedDatetime: datetime.datetime = Field(title="Received Datetime")

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
    station: station_schema.Station = Field(title="Station")
    instrument: instrument_schema.Instrument = Field(title="Instrument")


class InstrumentFaultReportResponse(Response):
    result: List[InstrumentFaultReport] = Field(title="Result")


class InstrumentFaultReportWithStationAndInstrumentResponse(Response):
    result: List[InstrumentFaultReportWithStationAndInstrument] = Field(title="Result")


class InstrumentFaultReportQueryResponse(InstrumentFaultReportResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
