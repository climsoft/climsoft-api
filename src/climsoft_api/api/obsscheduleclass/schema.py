from typing import List
from pydantic import constr
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema

field_names = {"refersTo": "refers_to"}


class CreateObsScheduleClass(BaseSchema):
    scheduleClass: constr(max_length=255)
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        fields = {**field_names, "scheduleClass": "schedule_class"}


class UpdateObsScheduleClass(BaseSchema):
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        fields = field_names


class ObsScheduleClass(CreateObsScheduleClass):
    class Config:
        fields = {**field_names, "scheduleClass": "schedule_class"}
        orm_mode = True
        allow_population_by_field_name = True


class ObsScheduleClassResponse(Response):
    result: List[ObsScheduleClass]


class ObsScheduleClassWithStation(ObsScheduleClass):
    station: station_schema.Station


class ObsScheduleClassWithStationResponse(Response):
    result: List[ObsScheduleClassWithStation]
