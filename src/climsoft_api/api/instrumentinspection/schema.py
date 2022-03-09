import datetime
from typing import List

import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateInstrumentInspection(BaseSchema):
    performedOn: constr(max_length=255) = Field(title="Performed On")
    inspectionDatetime: constr(max_length=50) = Field(title="Performed On")
    performedBy: constr(max_length=255) = Field(title="Performed On")
    status: constr(max_length=255) = Field(title="Status")
    remarks: constr(max_length=255) = Field(title="Remarks")
    performedAt: constr(max_length=50) = Field(title="Performed At")

    class Config:
        fields = {
            "performedOn": "performed_on",
            "inspectionDatetime": "inspection_datetime",
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class UpdateInstrumentInspection(BaseSchema):
    performedBy: constr(max_length=255) = Field(title="Performed By")
    status: constr(max_length=255) = Field(title="Status")
    remarks: constr(max_length=255) = Field(title="Remarks")
    performedAt: constr(max_length=50) = Field(title="Performed At")

    class Config:
        fields = {
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class InstrumentInspection(CreateInstrumentInspection):
    performedAt: datetime.datetime = Field(title="Performed On")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "performedOn": "performed_on",
            "inspectionDatetime": "inspection_datetime",
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class InstrumentInspectionWithStationAndInstrument(InstrumentInspection):
    station: station_schema.Station = Field(title="Station")
    instrument: instrument_schema.Instrument = Field(title="Instrument")


class InstrumentInspectionResponse(Response):
    result: List[InstrumentInspection] = Field(title="Result")


class InstrumentInspectionWithStationAndInstrumentResponse(Response):
    result: List[InstrumentInspectionWithStationAndInstrument] = Field(title="Result")


class InstrumentInspectionQueryResponse(InstrumentInspectionResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
