from typing import List

from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateQCStatusDefinition(BaseSchema):
    code: int = Field(title="Code")
    description: constr(max_length=255) = Field(title="Description")


class UpdateQCStatusDefinition(BaseSchema):
    description: constr(max_length=255) = Field(title="Description")


class QCStatusDefinition(CreateQCStatusDefinition):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class QCStatusDefinitionResponse(Response):
    result: List[QCStatusDefinition] = Field(title="Result")


class QCStatusDefinitionQueryResponse(QCStatusDefinitionResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
