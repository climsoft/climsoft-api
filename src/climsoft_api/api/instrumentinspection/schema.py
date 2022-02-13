import datetime

from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema
import climsoft_api.api.instrument.schema as instrument_schema


class CreateInstrumentInspection(BaseSchema):
    performedOn: constr(max_length=255)
    inspectionDatetime: constr(max_length=50)
    performedBy: constr(max_length=255)
    status: constr(max_length=255)
    remarks: constr(max_length=255)
    performedAt: constr(max_length=50)

    class Config:
        fields = {
            "performedOn": "performed_on",
            "inspectionDatetime": "inspection_datetime",
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class UpdateInstrumentInspection(BaseSchema):
    performedBy: constr(max_length=255)
    status: constr(max_length=255)
    remarks: constr(max_length=255)
    performedAt: constr(max_length=50)

    class Config:
        fields = {
            "performedBy": "performed_by",
            "performedAt": "performed_at"
        }


class InstrumentInspection(CreateInstrumentInspection):
    performedAt = datetime.datetime

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
    station: station_schema.Station
    instrument: instrument_schema.Instrument


class InstrumentInspectionResponse(Response):
    result: List[InstrumentInspection]


class InstrumentInspectionWithStationAndInstrumentResponse(Response):
    result: List[InstrumentInspectionWithStationAndInstrument]


class InstrumentInspectionQueryResponse(InstrumentInspectionResponse):
    limit: int
    page: int
    pages: int
