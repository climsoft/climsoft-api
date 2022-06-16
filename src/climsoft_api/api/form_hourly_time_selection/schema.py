from pydantic import BaseModel, constr, Field
from typing import Optional, List
from climsoft_api.api.schema import Response


class CreateFormHourlyTimeSelection(BaseModel):
    hh: int
    hh_selection: int


class UpdateFormHourlyTimeSelection(BaseModel):
    hh_selection: int


class FormHourlyTimeSelection(CreateFormHourlyTimeSelection):
    class Config:
        orm_mode = True


class FormHourlyTimeSelectionResponse(Response):
    result: List[FormHourlyTimeSelection] = Field(title="Result")


class FormHourlyTimeSelectionQueryResponse(FormHourlyTimeSelectionResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
