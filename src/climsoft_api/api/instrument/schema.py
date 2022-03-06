from typing import List

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
    instrumentName: constr(max_length=255) = Field(title=_("Instrument Name"))
    instrumentId: constr(max_length=255) = Field(title=_("Instrument ID"))
    serialNumber: constr(max_length=255) = Field(title=_("Serial Number"))
    abbreviation: constr(max_length=255) = Field(title=_("Abbreviation"))
    model: constr(max_length=255) = Field(title=_("Model"))
    manufacturer: constr(max_length=255) = Field(title=_("Manufacturer"))
    instrumentUncertainty: float = Field(title=_("Instrument Uncertainty"))
    installationDatetime: constr(max_length=50) = Field(title=_("Installation Datetime"))
    deinstallationDatetime: constr(max_length=50) = Field(title=_("Uninstallation Datetime"))
    height: constr(max_length=255) = Field(title=_("Height"))
    instrumentPicture: constr(max_length=255) = Field(title=_("Instrument Picture"))
    installedAt: constr(max_length=255) = Field(title=_("Installed At"))

    class Config:
        fields = field_names


class UpdateInstrument(BaseSchema):
    instrumentName: constr(max_length=255) = Field(title=_("Instrument Name"))
    serialNumber: constr(max_length=255) = Field(title=_("Serial Number"))
    abbreviation: constr(max_length=255) = Field(title=_("Abbreviation"))
    model: constr(max_length=255) = Field(title=_("Model"))
    manufacturer: constr(max_length=255) = Field(title=_("Manufacturer"))
    instrumentUncertainty: float = Field(title=_("Instrument Uncertainty"))
    installationDatetime: constr(max_length=50) = Field(title=_("Installation Datetime"))
    deinstallationDatetime: constr(max_length=50) = Field(title=_("Uninstallation Datetime"))
    height: constr(max_length=255) = Field(title=_("Height"))
    instrumentPicture: constr(max_length=255) = Field(title=_("Instrument Picture"))
    installedAt: constr(max_length=255) = Field(title=_("Installed At"))

    class Config:
        fields = field_names


class Instrument(CreateInstrument):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = field_names


class InstrumentResponse(Response):
    result: List[Instrument] = Field(title=_("Result"))


class InstrumentWithStation(Instrument):
    station: station_schema.Station = Field(title=_("Instrument Name"))


class InstrumentWithStationResponse(Response):
    result: List[InstrumentWithStation] = Field(title=_("Result"))


class InstrumentQueryResponse(InstrumentResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
