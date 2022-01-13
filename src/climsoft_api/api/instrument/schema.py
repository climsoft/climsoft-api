from typing import List
from pydantic import constr
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema


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
    instrumentName: constr(max_length=255)
    instrumentId: constr(max_length=255)
    serialNumber: constr(max_length=255)
    abbreviation: constr(max_length=255)
    model: constr(max_length=255)
    manufacturer: constr(max_length=255)
    instrumentUncertainty: float
    installationDatetime: constr(max_length=50)
    deinstallationDatetime: constr(max_length=50)
    height: constr(max_length=255)
    instrumentPicture: constr(max_length=255)
    installedAt: constr(max_length=255)


class UpdateInstrument(BaseSchema):
    instrumentName: constr(max_length=255)
    serialNumber: constr(max_length=255)
    abbreviation: constr(max_length=255)
    model: constr(max_length=255)
    manufacturer: constr(max_length=255)
    instrumentUncertainty: float
    installationDatetime: constr(max_length=50)
    deinstallationDatetime: constr(max_length=50)
    height: constr(max_length=255)
    instrumentPicture: constr(max_length=255)
    installedAt: constr(max_length=255)


class Instrument(CreateInstrument):
    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class InstrumentResponse(Response):
    result: List[Instrument]


class InstrumentWithStation(Instrument):
    station: station_schema.Station


class InstrumentWithStationResponse(Response):
    result: List[InstrumentWithStation]
