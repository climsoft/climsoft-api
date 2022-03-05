from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr


class CreateDataForm(BaseSchema):
    form_name: constr(max_length=250)
    order_num: int
    table_name: constr(max_length=255)
    description: str
    selected: bool
    val_start_position: int
    val_end_position: int
    elem_code_location: constr(max_length=255)
    sequencer: constr(max_length=50)
    entry_mode: bool


class UpdateDataForm(BaseSchema):
    order_num: int
    table_name: constr(max_length=255)
    description: str
    selected: bool
    val_start_position: int
    val_end_position: int
    elem_code_location: constr(max_length=255)
    sequencer: constr(max_length=50)
    entry_mode: bool


class DataForm(CreateDataForm):
    class Config:
        orm_mode = True


class DataFormResponse(Response):
    result: List[DataForm]


class DataFormQueryResponse(DataFormResponse):
    limit: int
    page: int
    pages: int
