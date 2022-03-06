from typing import List

from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateRegKey(BaseSchema):
    keyName: constr(max_length=255) = Field(title=_("Key Name"))
    keyValue: constr(max_length=255) = Field(title=_("Key Value"))
    keyDescription: constr(max_length=255) = Field(title=_("Key Description"))

    class Config:
        fields = {
            "keyName": "key_name",
            "keyValue": "key_value",
            "keyDescription": "key_description",
        }


class UpdateRegKey(BaseSchema):
    keyValue: constr(max_length=255) = Field(title=_("Key Value"))
    keyDescription: constr(max_length=255) = Field(title=_("Key Description"))

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
    result: List[RegKey] = Field(title=_("Result"))


class RegKeyQueryResponse(RegKeyResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
