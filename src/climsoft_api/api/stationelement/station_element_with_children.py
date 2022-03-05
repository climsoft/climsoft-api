from typing import List

from climsoft_api.api.schema import Response

from .schema import StationElement
from ..obselement.schema import ObsElement, field_mapping


class StationElementWithObsElement(StationElement):
    obselement: ObsElement

    class Config:
        orm_mode = True
        fields = {**field_mapping, "obselement": "obs_element"}
        allow_population_by_field_name = True


class StationElementWithObsElementQueryResponse(Response):
    status: str = "success"
    result: List[StationElementWithObsElement]
    limit: int
    page: int
    pages: int
