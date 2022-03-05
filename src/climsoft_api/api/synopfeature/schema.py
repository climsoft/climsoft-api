from typing import List

from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr


class CreateSynopFeature(BaseSchema):
    abbreviation: str
    description: constr(max_length=255)


class UpdateSynopFeature(BaseSchema):
    description: constr(max_length=255)


class SynopFeature(CreateSynopFeature):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class SynopFeatureResponse(Response):
    result: List[SynopFeature] = Field(title=_("Result"))


class SynopFeatureQueryResponse(SynopFeatureResponse):
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
