import datetime

from pydantic import constr
from typing import List
from climsoft_api.api.schema import Response, BaseSchema
import climsoft_api.api.station.schema as station_schema
import climsoft_api.api.physicalfeatureclass.schema as physicalfeatureclass_schema


class CreatePhysicalFeature(BaseSchema):
    associatedWith: constr(max_length=255)
    beginDate: constr(max_length=50)
    endDate: constr(max_length=50)
    image: constr(max_length=255)
    description: constr(max_length=255)
    classifiedInto: constr(max_length=50)

    class Config:
        fields = {
            "associatedWith": "associated_with",
            "beginDate": "begin_date",
            "endDate": "end_date",
            "classifiedInto": "classified_into",
        }


class UpdatePhysicalFeature(BaseSchema):
    endDate: constr(max_length=50)
    image: constr(max_length=255)

    class Config:
        fields = {"endDate": "end_date"}


class PhysicalFeature(CreatePhysicalFeature):
    beginDate = datetime.datetime
    endDate = datetime.datetime

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
    station: station_schema.Station
    physicalfeatureclas: physicalfeatureclass_schema.PhysicalFeatureClass


class PhysicalFeatureResponse(Response):
    result: List[PhysicalFeature]


class PhysicalFeatureWithStationAndPhysicalFeatureClassResponse(Response):
    result: List[PhysicalFeatureWithStationAndPhysicalFeatureClass]


class PhysicalFeatureQueryResponse(PhysicalFeatureResponse):
    limit: int
    page: int
    pages: int





