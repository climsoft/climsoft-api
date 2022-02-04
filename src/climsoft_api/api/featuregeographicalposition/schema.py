from pydantic import constr
from climsoft_api.api.schema import Response, BaseSchema
from typing import List
import climsoft_api.api.synopfeature.schema as synopfeature_schema


class CreateFeatureGeographicalPosition(BaseSchema):
    belongsTo: constr(max_length=255)
    observedOn: constr(max_length=50)
    latitude: float
    longitude: float

    class Config:
        fields = {
            "belongsTo": "belongs_to",
            "observedOn": "observed_on"
        }


class UpdateFeatureGeographicalPosition(BaseSchema):
    observedOn: constr(max_length=50)
    latitude: float
    longitude: float

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
    synopfeature: synopfeature_schema.SynopFeature


class FeatureGeographicalPositionResponse(Response):
    result: List[FeatureGeographicalPosition]


class FeatureGeographicalPositionWithSynopFeatureResponse(Response):
    result: List[FeatureGeographicalPositionWithSynopFeature]
