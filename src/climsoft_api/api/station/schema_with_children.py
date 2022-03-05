from typing import Optional, List

from climsoft_api.api.station.schema import Station
from climsoft_api.api.stationelement.schema import StationElement
from pydantic import BaseModel, Field


class StationWithElements(Station):
    elements: Optional[List[StationElement]]


class StationWithElementsResponse(BaseModel):
    message: str
    result: StationWithElements = Field(title=_("Result"))
    limit: int = Field(title=_("Limit"))
    page: int
    pages: int
