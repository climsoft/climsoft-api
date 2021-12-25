from pydantic import constr
from typing import List
from climsoft_api.api.schema import Response, BaseSchema


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
    result: List[SynopFeature]
