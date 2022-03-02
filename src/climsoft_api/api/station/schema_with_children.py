from pydantic import BaseModel
from typing import Optional, List
from climsoft_api.api.station.schema import Station
from climsoft_api.api.stationelement.schema import StationElement


class StationWithElements(Station):
    elements: Optional[List[StationElement]]


class StationWithElementsResponse(BaseModel):
    message: str
    result: StationWithElements
    limit: int
    page: int
    pages: int
