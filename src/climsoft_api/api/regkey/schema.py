from pydantic import constr
from typing import List
from climsoft_api.api.schema import BaseSchema, Response


class CreateRegKey(BaseSchema):
    keyName: constr(max_length=255)
    keyValue: constr(max_length=255)
    keyDescription: constr(max_length=255)

    class Config:
        fields = {
            "keyName": "key_name",
            "keyValue": "key_value",
            "keyDescription": "key_description",
        }


class UpdateRegKey(BaseSchema):
    keyValue: constr(max_length=255)
    keyDescription: constr(max_length=255)

    class Config:
        fields = {
            "keyValue": "key_value",
            "keyDescription": "key_description",
        }


class RegKey(CreateRegKey):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "keyName": "key_name",
            "keyValue": "key_value",
            "keyDescription": "key_description",
        }


class RegKeyResponse(Response):
    result: List[RegKey]


class RegKeyQueryResponse(RegKeyResponse):
    limit: int
    page: int
    pages: int



