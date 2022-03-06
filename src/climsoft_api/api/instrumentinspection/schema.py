import datetime
from typing import List

import climsoft_api.api.instrument.schema as instrument_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateInstrumentInspection(BaseSchema):
    performedOn: constr(max_length=255) = Field(title=_("Performed On"))
    inspectionDatetime: constr(max_length=50) = Field(title=_("Performed On"))
    performedBy: constr(max_length=255) = Field(title=_("Performed On"))
    status: constr(max_length=255) = Field(title=_("Status"))
    remarks: constr(max_length=255) = Field(title=_("Remarks"))
    performedAt: constr(max_length=50) = Field(title=_("Performed At"))

    class Config:
        fields = {
            "performedOn": "performed_on",
            "inspectionDatetime": "inspection_datetime",
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class UpdateInstrumentInspection(BaseSchema):
    performedBy: constr(max_length=255) = Field(title=_("Performed By"))
    status: constr(max_length=255) = Field(title=_("Status"))
    remarks: constr(max_length=255) = Field(title=_("Remarks"))
    performedAt: constr(max_length=50) = Field(title=_("Performed At"))

    class Config:
        fields = {
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class InstrumentInspection(CreateInstrumentInspection):
    performedAt = datetime.datetime = Field(title=_("Performed On"))

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
    station: station_schema.Station = Field(title=_("Station"))
    instrument: instrument_schema.Instrument = Field(title=_("Instrument"))


class InstrumentInspectionResponse(Response):
    result: List[InstrumentInspection] = Field(title=_("Result"))


class InstrumentInspectionWithStationAndInstrumentResponse(Response):
    result: List[InstrumentInspectionWithStationAndInstrument] = Field(title=_("Result"))


class InstrumentInspectionQueryResponse(InstrumentInspectionResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
