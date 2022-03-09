from typing import List

from climsoft_api.api.schema import BaseSchema
from pydantic import constr, Field

field_mapping = {
    "elementId": "element_id",
    "elementName": "element_name",
    "elementScale": "element_scale",
    "upperLimit": "upper_limit",
    "lowerLimit": "lower_limit",
    "elementtype": "element_type",
    "qcTotalRequired": "qc_total_required"
}


class CreateObsElement(BaseSchema):
    elementId: int = Field(title="Element ID")
    abbreviation: constr(max_length=255) = Field(title="Abbreviation")
    elementName: constr(max_length=255) = Field(title="Element Name")
    description: constr(max_length=255) = Field(title="Description")
    elementScale: float = Field(title="Element Scale")
    upperLimit: constr(max_length=255) = Field(title="Upper Limit")
    lowerLimit: constr(max_length=255) = Field(title="Lower Limit")
    units: constr(max_length=255) = Field(title="Units")
    elementtype: constr(max_length=50) = Field(title="Element Type")
    qcTotalRequired: int = Field(title="QC Total Required")
    selected: bool = Field(title="Selected")

    class Config:
        fields = field_mapping


class UpdateObsElement(BaseSchema):
    abbreviation: constr(max_length=255) = Field(title="Abbreviation")
    elementName: constr(max_length=255) = Field(title="Element Name")
    description: constr(max_length=255) = Field(title="Description")
    elementScale: float = Field(title="Element Scale")
    upperLimit: constr(max_length=255) = Field(title="Upper Limit")
    lowerLimit: constr(max_length=255) = Field(title="Lower Limit")
    units: constr(max_length=255) = Field(title="Units")
    elementtype: constr(max_length=50) = Field(title="Element Type")
    qcTotalRequired: int = Field(title="QC Total Required")
    selected: bool = Field(title="Selected")

    class Config:
        fields = field_mapping


class ObsElement(CreateObsElement):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = field_mapping


class ObsElementResponse(BaseSchema):
    message: str = Field(title="Message")
    status: str = Field(title="Status")
    result: List[ObsElement] = Field(title="Result")


class ObsElementQueryResponse(ObsElementResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
