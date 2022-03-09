from typing import Optional, List

from climsoft_api.api.station.schema import Station
from climsoft_api.api.stationelement.schema import StationElement
from pydantic import BaseModel, Field


class StationWithElements(Station):
    elements: Optional[List[StationElement]] = Field(title="Elements")


class StationWithElementsResponse(BaseModel):
    message: str = Field(title="Message")
    result: StationWithElements = Field(title="Result")
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
