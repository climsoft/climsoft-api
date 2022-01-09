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


class ObsElement(CreateObsElement):
    class Config:
        orm_mode = True

        allow_population_by_field_name = True


class ObsElementResponse(BaseSchema):
    message: str
    status: str
    result: List[ObsElement]
