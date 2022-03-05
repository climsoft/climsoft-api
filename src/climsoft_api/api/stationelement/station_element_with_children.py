from typing import List

from climsoft_api.api.schema import Response
from pydantic import Field
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
    result: List[StationElementWithObsElement] = Field(title=_("Result"))
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
