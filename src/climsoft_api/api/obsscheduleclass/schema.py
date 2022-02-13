from typing import List
from pydantic import constr
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema


class CreateObsScheduleClass(BaseSchema):
    scheduleClass: constr(max_length=255)
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        fields = {
            "scheduleClass": "schedule_class",
            "refersTo": "refers_to"
        }


class UpdateObsScheduleClass(BaseSchema):
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        fields = {
            "refersTo": "refers_to"
        }


class ObsScheduleClass(CreateObsScheduleClass):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "scheduleClass": "schedule_class",
            "refersTo": "refers_to"
        }


class ObsScheduleClassResponse(Response):
    result: List[ObsScheduleClass]


class ObsScheduleClassWithStation(ObsScheduleClass):
    station: station_schema.Station


class ObsScheduleClassWithStationResponse(Response):
    result: List[ObsScheduleClassWithStation]


class ObsScheduleClassQueryResponse(ObsScheduleClassResponse):
    limit: int
    page: int
    pages: int
