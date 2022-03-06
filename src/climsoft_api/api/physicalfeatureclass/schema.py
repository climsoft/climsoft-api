from typing import List

import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreatePhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255) = Field(title=_("Feature Class"))
    description: constr(max_length=255) = Field(title=_("Description"))
    refersTo: constr(max_length=255) = Field(title=_("Refers To"))

    class Config:
        fields = {"featureClass": "feature_class", "refersTo": "refers_to"}


class UpdatePhysicalFeatureClass(BaseSchema):
    description: constr(max_length=255) = Field(title=_("Description"))
    refersTo: constr(max_length=255) = Field(title=_("Refers To"))

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"refersTo": "refers_to"}


class PhysicalFeatureClass(BaseSchema):
    featureClass: constr(max_length=255) = Field(title=_("Feature Class"))
    description: constr(max_length=255) = Field(title=_("Description"))
    refersTo: constr(max_length=255) = Field(title=_("Refers To"))

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {"featureClass": "feature_class", "refersTo": "refers_to"}


class PhysicalFeatureClassWithStation(PhysicalFeatureClass):
    station: station_schema.Station = Field(title=_("Station"))


class PhysicalFeatureClassResponse(Response):
    result: List[PhysicalFeatureClass] = Field(title=_("Result"))


class PhysicalFeatureClassWithStationResponse(Response):
    result: List[PhysicalFeatureClassWithStation] = Field(title=_("Result"))


class PhysicalFeatureClassQueryResponse(PhysicalFeatureClassResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
