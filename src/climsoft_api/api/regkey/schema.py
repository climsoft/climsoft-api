from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response


class CreateRegKey(BaseSchema):
    keyName: constr(max_length=255)
    keyValue: constr(max_length=255)
    keyDescription: constr(max_length=255)


class UpdateRegKey(BaseSchema):
    keyValue: constr(max_length=255)
    keyDescription: constr(max_length=255)


class RegKey(CreateRegKey):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RegKeyResponse(Response):
    result: List[RegKey]
