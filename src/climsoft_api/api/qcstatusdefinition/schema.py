from typing import List

from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateQCStatusDefinition(BaseSchema):
    code: int
    description: constr(max_length=255)


class UpdateQCStatusDefinition(BaseSchema):
    description: constr(max_length=255)


class QCStatusDefinition(CreateQCStatusDefinition):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class QCStatusDefinitionResponse(Response):
    result: List[QCStatusDefinition] = Field(title=_("Result"))


class QCStatusDefinitionQueryResponse(QCStatusDefinitionResponse):
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
