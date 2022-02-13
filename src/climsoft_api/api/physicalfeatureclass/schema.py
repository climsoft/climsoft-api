from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response
import climsoft_api.api.station.schema as station_schema


class CreatePhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255)
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        fields = {"featureClass": "feature_class", "refersTo": "refers_to"}


class UpdatePhysicalFeatureClass(BaseSchema):
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"refersTo": "refers_to"}


class PhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255)
    description: constr(max_length=255)
    refersTo: constr(max_length=255)

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"featureClass": "feature_class", "refersTo": "refers_to"}


class PhysicalFeatureClassWithStation(PhysicalFeatureClass):
    station: station_schema.Station


class PhysicalFeatureClassResponse(Response):
    result: List[PhysicalFeatureClass]


class PhysicalFeatureClassWithStationResponse(Response):
    result: List[PhysicalFeatureClassWithStation]


class PhysicalFeatureClassQueryResponse(PhysicalFeatureClassResponse):
    limit: int
    page: int
    pages: int

