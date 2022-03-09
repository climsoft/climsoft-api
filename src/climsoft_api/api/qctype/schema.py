from typing import List

from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateQCType(BaseSchema):
    code: int = Field(title="Code")
    description: constr(max_length=255) = Field(title="Description")


class UpdateQCType(BaseSchema):
    description: constr(max_length=255) = Field(title="Description")


class QCType(CreateQCType):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class QCTypeResponse(Response):
    result: List[QCType] = Field(title="Result")


class QCTypeQueryResponse(QCTypeResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
