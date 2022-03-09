from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateDataForm(BaseSchema):
    form_name: constr(max_length=250) = Field(title="Form Name")
    order_num: int = Field(title="Order Number")
    table_name: constr(max_length=255) = Field(title="Table Name")
    description: str = Field(title="Description")
    selected: bool = Field(title="Selected")
    val_start_position: int = Field(title="Start Position")
    val_end_position: int = Field(title="End Position")
    elem_code_location: constr(max_length=255) = Field(title="Location Code of Element")
    sequencer: constr(max_length=50) = Field(title="Sequencer")
    entry_mode: bool = Field(title="Entry Mode")


class UpdateDataForm(BaseSchema):
    order_num: int = Field(title="Order Number")
    table_name: constr(max_length=255) = Field(title="Table Name")
    description: str = Field(title="Description")
    selected: bool = Field(title="Selected")
    val_start_position: int = Field(title="Start Position")
    val_end_position: int = Field(title="End Position")
    elem_code_location: constr(max_length=255) = Field(title="Location Code of Element")
    sequencer: constr(max_length=50) = Field(title="Sequencer")
    entry_mode: bool = Field(title="Entry Mode")


class DataForm(CreateDataForm):
    class Config:
        orm_mode = True


class DataFormResponse(Response):
    result: List[DataForm] = Field(title="Result")


class DataFormQueryResponse(DataFormResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
