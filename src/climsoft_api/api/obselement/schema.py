from typing import List
from pydantic import constr
from climsoft_api.api.schema import BaseSchema


class CreateObsElement(BaseSchema):
    elementId: int
    abbreviation: constr(max_length=255)
    elementName: constr(max_length=255)
    description: constr(max_length=255)
    elementScale: float
    upperLimit: constr(max_length=255)
    lowerLimit: constr(max_length=255)
    units: constr(max_length=255)
    elementtype: constr(max_length=50)
    qcTotalRequired: int
    selected: bool

    class Config:
        fields = {
            "elementId": "element_id",
            "elementName": "element_name",
            "elementScale": "element_scale",
            "upperLimit": "upper_limit",
            "lowerLimit": "lower_limit",
            "elementtype": "element_type",
            "qcTotalRequired": "qc_total_required"
        }


class UpdateObsElement(BaseSchema):
    abbreviation: constr(max_length=255)
    elementName: constr(max_length=255)
    description: constr(max_length=255)
    elementScale: float
    upperLimit: constr(max_length=255)
    lowerLimit: constr(max_length=255)
    units: constr(max_length=255)
    elementtype: constr(max_length=50)
    qcTotalRequired: int
    selected: bool

    class Config:
        fields = {
            "elementId": "element_id",
            "elementName": "element_name",
            "elementScale": "element_scale",
            "upperLimit": "upper_limit",
            "lowerLimit": "lower_limit",
            "elementtype": "element_type",
            "qcTotalRequired": "qc_total_required"
        }


class ObsElement(CreateObsElement):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "elementId": "element_id",
            "elementName": "element_name",
            "elementScale": "element_scale",
            "upperLimit": "upper_limit",
            "lowerLimit": "lower_limit",
            "elementtype": "element_type",
            "qcTotalRequired": "qc_total_required"
        }


class ObsElementResponse(BaseSchema):
    message: str
    status: str
    result: List[ObsElement]


class ObsElementQueryResponse(ObsElementResponse):
    limit: int
    page: int
    pages: int

