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
    elementId: int = Field(title=_("Element ID"))
    abbreviation: constr(max_length=255) = Field(title=_("Abbreviation"))
    elementName: constr(max_length=255) = Field(title=_("Element Name"))
    description: constr(max_length=255) = Field(title=_("Description"))
    elementScale: float = Field(title=_("Element Scale"))
    upperLimit: constr(max_length=255) = Field(title=_("Upper Limit"))
    lowerLimit: constr(max_length=255) = Field(title=_("Lower Limit"))
    units: constr(max_length=255) = Field(title=_("Units"))
    elementtype: constr(max_length=50) = Field(title=_("Element Type"))
    qcTotalRequired: int = Field(title=_("QC Total Required"))
    selected: bool = Field(title=_("Selected"))

    class Config:
        fields = field_mapping


class UpdateObsElement(BaseSchema):
    abbreviation: constr(max_length=255) = Field(title=_("Abbreviation"))
    elementName: constr(max_length=255) = Field(title=_("Element Name"))
    description: constr(max_length=255) = Field(title=_("Description"))
    elementScale: float = Field(title=_("Element Scale"))
    upperLimit: constr(max_length=255) = Field(title=_("Upper Limit"))
    lowerLimit: constr(max_length=255) = Field(title=_("Lower Limit"))
    units: constr(max_length=255) = Field(title=_("Units"))
    elementtype: constr(max_length=50) = Field(title=_("Element Type"))
    qcTotalRequired: int = Field(title=_("QC Total Required"))
    selected: bool = Field(title=_("Selected"))

    class Config:
        fields = field_mapping


class ObsElement(CreateObsElement):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = field_mapping


class ObsElementResponse(BaseSchema):
    message: str = Field(title=_("Message"))
    status: str = Field(title=_("Status"))
    result: List[ObsElement] = Field(title=_("Result"))


class ObsElementQueryResponse(ObsElementResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
