from typing import List

import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreatePhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255) = Field(title="Feature Class")
    description: constr(max_length=255) = Field(title="Description")
    refersTo: constr(max_length=255) = Field(title="Refers To")

    class Config:
        fields = {"featureClass": "feature_class", "refersTo": "refers_to"}


class UpdatePhysicalFeatureClass(BaseSchema):
    description: constr(max_length=255) = Field(title="Description")
    refersTo: constr(max_length=255) = Field(title="Refers To")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"refersTo": "refers_to"}


class PhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255) = Field(title="Feature Class")
    description: constr(max_length=255) = Field(title="Description")
    refersTo: constr(max_length=255) = Field(title="Refers To")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"featureClass": "feature_class", "refersTo": "refers_to"}


class PhysicalFeatureClassWithStation(PhysicalFeatureClass):
    station: station_schema.Station = Field(title="Station")


class PhysicalFeatureClassResponse(Response):
    result: List[PhysicalFeatureClass] = Field(title="Result")


class PhysicalFeatureClassWithStationResponse(Response):
    result: List[PhysicalFeatureClassWithStation] = Field(title="Result")


class PhysicalFeatureClassQueryResponse(PhysicalFeatureClassResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
