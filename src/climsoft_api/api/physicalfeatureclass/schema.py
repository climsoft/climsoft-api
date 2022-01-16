from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema


class CreatePhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255)
    description: constr(max_length=255)
    refersTo: constr(max_length=255)


class UpdatePhysicalFeatureClass(BaseSchema):
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class PhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255)
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class PhysicalFeatureClassWithStation(PhysicalFeatureClass):
    station: station_schema.Station


class PhysicalFeatureClassResponse(Response):
    result: List[PhysicalFeatureClass]


class PhysicalFeatureClassWithStationResponse(Response):
    result: List[PhysicalFeatureClassWithStation]
