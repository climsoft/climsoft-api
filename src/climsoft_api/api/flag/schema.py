from typing import List
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr


class CreateFlag(BaseSchema):
    characterSymbol: constr(max_length=255)
    numSymbol: int
    description: constr(max_length=255)


class UpdateFlag(BaseSchema):
    numSymbol: int
    description: constr(max_length=255)


class Flag(CreateFlag):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True


class FlagResponse(Response):
    result: List[Flag]
