from typing import List

import climsoft_api.api.synopfeature.schema as synopfeature_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field


class CreateFeatureGeographicalPosition(BaseSchema):
    belongsTo: constr(max_length=255) = Field(title=_("Belongs To"))
    observedOn: constr(max_length=50) = Field(title=_("Observed On"))
    latitude: float = Field(title=_("Latitude"))
    longitude: float = Field(title=_("Longitude"))

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "observedOn": "observed_on"
        }


class UpdateFeatureGeographicalPosition(BaseSchema):
    observedOn: constr(max_length=50) = Field(title=_("Observed On"))
    latitude: float = Field(title=_("Latitude"))
    longitude: float = Field(title=_("Longitude"))

    class Config:
        fields = {
            "observedOn": "observed_on"
        }


class FeatureGeographicalPosition(CreateFeatureGeographicalPosition):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "belongsTo": "belongs_to",
            "observedOn": "observed_on"
        }


class FeatureGeographicalPositionWithSynopFeature(FeatureGeographicalPosition):
    synopfeature: synopfeature_schema.SynopFeature = Field(title=_("Synop Feature"))


class FeatureGeographicalPositionResponse(Response):
    result: List[FeatureGeographicalPosition] = Field(title=_("Result"))


class FeatureGeographicalPositionWithSynopFeatureResponse(Response):
    result: List[FeatureGeographicalPositionWithSynopFeature] = Field(title=_("Result"))


class FeatureGeographicalPositionQueryResponse(
    FeatureGeographicalPositionResponse
):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Limit"))
    pages: int = Field(title=_("Limit"))
