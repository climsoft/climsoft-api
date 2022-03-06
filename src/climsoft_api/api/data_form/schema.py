from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateDataForm(BaseSchema):
    form_name: constr(max_length=250) = Field(title=_("Form Name"))
    order_num: int = Field(title=_("Order Number"))
    table_name: constr(max_length=255) = Field(title=_("Table Name"))
    description: str = Field(title=_("Description"))
    selected: bool = Field(title=_("Selected"))
    val_start_position: int = Field(title=_("Start Position"))
    val_end_position: int = Field(title=_("End Position"))
    elem_code_location: constr(max_length=255) = Field(title=_("Location Code of Element"))
    sequencer: constr(max_length=50) = Field(title=_("Sequencer"))
    entry_mode: bool = Field(title=_("Entry Mode"))


class UpdateDataForm(BaseSchema):
    order_num: int = Field(title=_("Order Number"))
    table_name: constr(max_length=255) = Field(title=_("Table Name"))
    description: str = Field(title=_("Description"))
    selected: bool = Field(title=_("Selected"))
    val_start_position: int = Field(title=_("Start Position"))
    val_end_position: int = Field(title=_("End Position"))
    elem_code_location: constr(max_length=255) = Field(title=_("Location Code of Element"))
    sequencer: constr(max_length=50) = Field(title=_("Sequencer"))
    entry_mode: bool = Field(title=_("Entry Mode"))


class DataForm(CreateDataForm):
    class Config:
        orm_mode = True


class DataFormResponse(Response):
    result: List[DataForm] = Field(title=_("Result"))


class DataFormQueryResponse(DataFormResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
