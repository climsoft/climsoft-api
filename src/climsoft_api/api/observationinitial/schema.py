import datetime
from typing import List

import climsoft_api.api.obselement.schema as obselement_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import BaseSchema, Response
from pydantic import constr, Field


class CreateObservationInitial(BaseSchema):
    recordedFrom: constr(max_length=255) = Field(title=_("Recorded From"))
    describedBy: int = Field(title=_("Described By"))
    obsDatetime: str = Field(title=_("Obs Datetime"))
    qcStatus: int = Field(title=_("QC Status"))
    acquisitionType: int = Field(title=_("Acquisition Type"))
    obsLevel: constr(max_length=255) = Field(title=_("Obs Level"))
    obsValue: constr(max_length=255) = Field(title=_("Obs Value"))
    flag: constr(max_length=255) = Field(title=_("Flag"))
    period: int = Field(title=_("Period"))
    qcTypeLog: str = Field(title=_("QC Type Log"))
    dataForm: constr(max_length=255) = Field(title=_("Data Form"))
    capturedBy: constr(max_length=255) = Field(title=_("Captured By"))
    mark: bool = Field(title=_("Mark"))
    temperatureUnits: constr(max_length=255) = Field(title=_("Temperature Units"))
    precipitationUnits: constr(max_length=255) = Field(title=_("Precipitation Units"))
    cloudHeightUnits: constr(max_length=255) = Field(title=_("Cloud Height Units"))
    visUnits: constr(max_length=255) = Field(title=_("Vis Units"))
    dataSourceTimeZone: int = Field(title=_("Data Source Timezone"))

    class Config:
        fields = {
            "recordedFrom": "recorded_from",
            "describedBy": "described_by",
            "obsDatetime": "obs_datetime",
            "qcStatus": "qc_status",
            "acquisitionType": "acquisition_type",
            "obsLevel": "obs_level",
            "qcTypeLog": "qc_type_log",
            "dataForm": "data_form",
            "capturedBy": "captured_by",
            "temperatureUnits": "temperature_units",
            "precipitationUnits": "precipitation_units",
            "cloudHeightUnits": "cloud_height_units",
            "visUnits": "vis_units",
            "dataSourceTimeZone": "data_source_timezone"
        }


class UpdateObservationInitial(BaseSchema):
    obsLevel: constr(max_length=255) = Field(title=_("Obs Level"))
    obsValue: constr(max_length=255) = Field(title=_("Obs Value"))
    flag: constr(max_length=255) = Field(title=_("Flag"))
    period: int = Field(title=_("Period"))
    qcTypeLog: str = Field(title=_("QC Type Log"))
    dataForm: constr(max_length=255) = Field(title=_("Data Form"))
    capturedBy: constr(max_length=255) = Field(title=_("Captured By"))
    mark: bool = Field(title=_("Mark"))
    temperatureUnits: constr(max_length=255) = Field(title=_("Temperature Units"))
    precipitationUnits: constr(max_length=255) = Field(title=_("Precipitation Units"))
    cloudHeightUnits: constr(max_length=255) = Field(title=_("Cloud Height Units"))
    visUnits: constr(max_length=255) = Field(title=_("Vis Units"))
    dataSourceTimeZone: int = Field(title=_("Data Source Timezone"))

    class Config:
        fields = {
            "recordedFrom": "recorded_from",
            "describedBy": "described_by",
            "obsDatetime": "obs_datetime",
            "qcStatus": "qc_status",
            "acquisitionType": "acquisition_type",
            "obsLevel": "obs_level",
            "qcTypeLog": "qc_type_log",
            "dataForm": "data_form",
            "capturedBy": "captured_by",
            "temperatureUnits": "temperature_units",
            "precipitationUnits": "precipitation_units",
            "cloudHeightUnits": "cloud_height_units",
            "visUnits": "vis_units",
            "dataSourceTimeZone": "data_source_timezone"
        }


class ObservationInitial(CreateObservationInitial):
    obsDatetime: datetime.datetime = Field(title=_("Obs Datetime"))

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ObservationInitialResponse(Response):
    result: List[ObservationInitial] = Field(title=_("Result"))


class ObservationInitialWithChildren(ObservationInitial):
    obselement: obselement_schema.ObsElement = Field(title=_("Obs Element"))
    station: station_schema.Station = Field(title=_("Station"))

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        fields = {
            "recordedFrom": "recorded_from",
            "describedBy": "described_by",
            "obsDatetime": "obs_datetime",
            "qcStatus": "qc_status",
            "acquisitionType": "acquisition_type",
            "obsLevel": "obs_level",
            "qcTypeLog": "qc_type_log",
            "dataForm": "data_form",
            "capturedBy": "captured_by",
            "temperatureUnits": "temperature_units",
            "precipitationUnits": "precipitation_units",
            "cloudHeightUnits": "cloud_height_units",
            "visUnits": "vis_units",
            "dataSourceTimeZone": "data_source_timezone"
        }


class ObservationInitialWithChildrenResponse(Response):
    result: List[ObservationInitialWithChildren] = Field(title=_("Result"))


class ObservationInitialInputGen(CreateObservationInitial):
    class Config:
        allow_population_by_field_name = True


class ObservationInitialQueryResponse(ObservationInitialResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
