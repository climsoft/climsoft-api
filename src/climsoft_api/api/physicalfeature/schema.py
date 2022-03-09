import datetime
from typing import List

import \
    climsoft_api.api.physicalfeatureclass.schema as physicalfeatureclass_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreatePhysicalFeature(BaseSchema):
    associatedWith: constr(max_length=255) = Field(title="Associated With")
    beginDate: constr(max_length=50) = Field(title="Begin Date")
    endDate: constr(max_length=50) = Field(title="End Date")
    image: constr(max_length=255) = Field(title="Image")
    description: constr(max_length=255) = Field(title="Description")
    classifiedInto: constr(max_length=50) = Field(title="ClassifiedInto")

    class Config:
        fields = {
            "associatedWith": "associated_with",
            "beginDate": "begin_date",
            "endDate": "end_date",
            "classifiedInto": "classified_into",
        }


class UpdatePhysicalFeature(BaseSchema):
    endDate: constr(max_length=50) = Field(title="End Date")
    image: constr(max_length=255) = Field(title="Image")

    class Config:
        fields = {"endDate": "end_date"}


class PhysicalFeature(CreatePhysicalFeature):
    beginDate: datetime.datetime = Field(title="Begin Date")
    endDate: datetime.datetime = Field(title="End Date")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

        fields = {
            "associatedWith": "associated_with",
            "beginDate": "begin_date",
            "endDate": "end_date",
            "classifiedInto": "classified_into",
        }


class PhysicalFeatureWithStationAndPhysicalFeatureClass(PhysicalFeature):
    station: station_schema.Station = Field(title="Station")
    physicalfeatureclas: physicalfeatureclass_schema.PhysicalFeatureClass = Field(title="Physical Feature Class")


class PhysicalFeatureResponse(Response):
    result: List[PhysicalFeature] = Field(title="Result")


class PhysicalFeatureWithStationAndPhysicalFeatureClassResponse(Response):
    result: List[PhysicalFeatureWithStationAndPhysicalFeatureClass] = Field(title="Result")


class PhysicalFeatureQueryResponse(PhysicalFeatureResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
