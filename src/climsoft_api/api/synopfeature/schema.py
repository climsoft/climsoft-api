from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateSynopFeature(BaseSchema):
    abbreviation: str = Field(title="Abbreviation")
    description: constr(max_length=255) = Field(title="Description")


class UpdateSynopFeature(BaseSchema):
    description: constr(max_length=255) = Field(title="Description")


class SynopFeature(CreateSynopFeature):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class SynopFeatureResponse(Response):
    result: List[SynopFeature] = Field(title="Result")


class SynopFeatureQueryResponse(SynopFeatureResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
