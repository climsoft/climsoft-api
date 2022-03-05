from typing import List

from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateFlag(BaseSchema):
    characterSymbol: constr(max_length=255)
    numSymbol: int
    description: constr(max_length=255)

    class Config:
        fields = {
            "characterSymbol": "character_symbol",
            "numSymbol": "num_symbol"
        }


class UpdateFlag(BaseSchema):
    numSymbol: int
    description: constr(max_length=255)

    class Config:
        fields = {
            "numSymbol": "num_symbol"
        }


class Flag(CreateFlag):
    class Config:
        allow_population_by_field_name = True
        orm_mode = True
        fields = {
            "characterSymbol": "character_symbol",
            "numSymbol": "num_symbol"
        }


class FlagResponse(Response):
    result: List[Flag] = Field(title=_("Result"))


class FlagQueryResponse(FlagResponse):
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
