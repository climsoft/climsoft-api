from typing import Optional, List

from climsoft_api.api.station.schema import Station
from climsoft_api.api.stationelement.schema import StationElement
from pydantic import BaseModel, Field


class StationWithElements(Station):
    elements: Optional[List[StationElement]] = Field(title=_("Elements"))


class StationWithElementsResponse(BaseModel):
    message: str = Field(title=_("Message"))
    result: StationWithElements = Field(title=_("Result"))
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
