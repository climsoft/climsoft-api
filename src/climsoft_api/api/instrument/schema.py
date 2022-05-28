from typing import List, Optional

import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, Field

field_names = {
    "instrumentName": "instrument_name",
    "instrumentId": "instrument_id",
    "serialNumber": "serial_number",
    "instrumentUncertainty": "instrument_uncertainty",
    "installationDatetime": "installation_datetime",
    "deinstallationDatetime": "uninstallation_datetime",
    "instrumentPicture": "instrument_picture",
    "installedAt": "installed_at",
}


class CreateInstrument(BaseSchema):
    instrumentName: constr(max_length=255) = Field(title="Instrument Name")
    instrumentId: constr(max_length=255) = Field(title="Instrument ID")
    serialNumber: constr(max_length=255) = Field(title="Serial Number")
    abbreviation: constr(max_length=255) = Field(title="Abbreviation")
    model: constr(max_length=255) = Field(title="Model")
    manufacturer: constr(max_length=255) = Field(title="Manufacturer")
    instrumentUncertainty: float = Field(title="Instrument Uncertainty")
    installationDatetime: constr(max_length=50) = Field(title="Installation Datetime")
    deinstallationDatetime: Optional[constr(max_length=50)] = Field(title="Uninstallation Datetime")
    height: constr(max_length=255) = Field(title="Height")
    instrumentPicture: Optional[constr(max_length=255)] = Field(title="Instrument Picture")
    installedAt: constr(max_length=255) = Field(title="Installed At")

    class Config:
        fields = field_names


class UpdateInstrument(BaseSchema):
    instrumentName: constr(max_length=255) = Field(title="Instrument Name")
    serialNumber: constr(max_length=255) = Field(title="Serial Number")
    abbreviation: constr(max_length=255) = Field(title="Abbreviation")
    model: constr(max_length=255) = Field(title="Model")
    manufacturer: constr(max_length=255) = Field(title="Manufacturer")
    instrumentUncertainty: float = Field(title="Instrument Uncertainty")
    installationDatetime: constr(max_length=50) = Field(title="Installation Datetime")
    deinstallationDatetime: Optional[constr(max_length=50)] = Field(title="Uninstallation Datetime")
    height: constr(max_length=255) = Field(title="Height")
    instrumentPicture: Optional[constr(max_length=255)] = Field(title="Instrument Picture")
    installedAt: constr(max_length=255) = Field(title="Installed At")

    class Config:
        fields = field_names


class Instrument(CreateInstrument):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = field_names


class InstrumentResponse(Response):
    result: List[Instrument] = Field(title="Result")


class InstrumentWithStation(Instrument):
    station: station_schema.Station = Field(title="Instrument Name")


class InstrumentWithStationResponse(Response):
    result: List[InstrumentWithStation] = Field(title="Result")


class InstrumentQueryResponse(InstrumentResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
