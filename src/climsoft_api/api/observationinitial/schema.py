import datetime
from typing import List
from pydantic import constr
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema
import climsoft_api.api.obselement.schema as obselement_schema


class CreateObservationInitial(BaseSchema):
    recordedFrom: constr(max_length=255)
    describedBy: int
    obsDatetime: str
    qcStatus: int
    acquisitionType: int
    obsLevel: constr(max_length=255)
    obsValue: constr(max_length=255)
    flag: constr(max_length=255)
    period: int
    qcTypeLog: str
    dataForm: constr(max_length=255)
    capturedBy: constr(max_length=255)
    mark: bool
    temperatureUnits: constr(max_length=255)
    precipitationUnits: constr(max_length=255)
    cloudHeightUnits: constr(max_length=255)
    visUnits: constr(max_length=255)
    dataSourceTimeZone: int


class UpdateObservationInitial(BaseSchema):
    obsLevel: constr(max_length=255)
    obsValue: constr(max_length=255)
    flag: constr(max_length=255)
    period: int
    qcTypeLog: str
    dataForm: constr(max_length=255)
    capturedBy: constr(max_length=255)
    mark: bool
    temperatureUnits: constr(max_length=255)
    precipitationUnits: constr(max_length=255)
    cloudHeightUnits: constr(max_length=255)
    visUnits: constr(max_length=255)
    dataSourceTimeZone: int


class ObservationInitial(CreateObservationInitial):
    obsDatetime: datetime.datetime

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ObservationInitialResponse(Response):
    result: List[ObservationInitial]


class ObservationInitialWithChildren(ObservationInitial):
    obselement: obselement_schema.ObsElement
    station: station_schema.Station

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ObservationInitialWithChildrenResponse(Response):
    result: List[ObservationInitialWithChildren]


class ObservationInitialInputGen(CreateObservationInitial):
    class Config:
        allow_population_by_field_name = True
