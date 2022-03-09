import datetime
from typing import List, Optional

import climsoft_api.api.obselement.schema as obselement_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, StrictStr, Field


class CreateObservationFinal(BaseSchema):
    recordedFrom: constr(max_length=255) = Field(title="Recorded From")
    describedBy: int = Field(title="Described By")
    obsDatetime: StrictStr = Field(title="Obs Datetime")
    qcStatus: int = Field(title="QC Status")
    acquisitionType: int = Field(title="Acquisition Type")
    obsLevel: constr(max_length=255) = Field(title="Obs Level")
    obsValue: constr(max_length=255) = Field(title="ObsValue")
    flag: constr(max_length=255) = Field(title="Flag")
    period: Optional[int] = Field(title="Period")
    qcTypeLog: Optional[str] = Field(title="QC Type Log")
    dataForm: Optional[constr(max_length=255)] = Field(title="Data Form")
    capturedBy: Optional[constr(max_length=255)] = Field(title="Captured By")
    mark: Optional[bool] = Field(title="Mark")
    temperatureUnits: Optional[constr(max_length=255)] = Field(title="Temperature Units")
    precipitationUnits: Optional[constr(max_length=255)] = Field(title="Precipitation Units")
    cloudHeightUnits: Optional[constr(max_length=255)] = Field(title="Cloud Height Units")
    visUnits: Optional[constr(max_length=255)] = Field(title="Vis Units")
    dataSourceTimeZone: int = Field(title="Data Source Timezone")

    class Config:
        fields = {
            "recordedFrom": "recorded_from",
            "describedBy": "described_by",
            "obsDatetime": "obs_datetime",
            "qcStatus": "qc_status",
            "acquisitionType": "acquisition_type",
            "obsLevel": "obs_level",
            "obsValue": "obs_value",
            "qcTypeLog": "qc_type_log",
            "dataForm": "data_form",
            "capturedBy": "captured_by",
            "temperatureUnits": "temperature_units",
            "precipitationUnits": "precipitation_units",
            "cloudHeightUnits": "cloud_height_units",
            "visUnits": "vis_units",
            "dataSourceTimeZone": "data_source_timezone"
        }


class UpdateObservationFinal(BaseSchema):
    qcStatus: int = Field(title="QC Status")
    acquisitionType: int = Field(title="Acquisition Type")
    obsLevel: constr(max_length=255) = Field(title="Obs Level")
    obsValue: constr(max_length=255) = Field(title="Obs Value")
    flag: constr(max_length=255) = Field(title="Flag")
    period: Optional[int] = Field(title="Period")
    qcTypeLog: Optional[str] = Field(title="QC Type Log")
    dataForm: Optional[constr(max_length=255)] = Field(title="Data Form")
    capturedBy: Optional[constr(max_length=255)] = Field(title="Captured By")
    mark: Optional[bool] = Field(title="Mark")
    temperatureUnits: Optional[constr(max_length=255)] = Field(title="Temperature Units")
    precipitationUnits: Optional[constr(max_length=255)] = Field(title="Precipitation Units")
    cloudHeightUnits: Optional[constr(max_length=255)] = Field(title="Cloud Height Units")
    visUnits: Optional[constr(max_length=255)] = Field(title="Vis Units")
    dataSourceTimeZone: int = Field(title="Data Source Timezone")

    class Config:
        fields = {
            "recordedFrom": "recorded_from",
            "describedBy": "described_by",
            "obsDatetime": "obs_datetime",
            "qcStatus": "qc_status",
            "acquisitionType": "acquisition_type",
            "obsLevel": "obs_level",
            "obsValue": "obs_value",
            "qcTypeLog": "qc_type_log",
            "dataForm": "data_form",
            "capturedBy": "captured_by",
            "temperatureUnits": "temperature_units",
            "precipitationUnits": "precipitation_units",
            "cloudHeightUnits": "cloud_height_units",
            "visUnits": "vis_units",
            "dataSourceTimeZone": "data_source_timezone"
        }


class ObservationFinal(CreateObservationFinal):
    obsDatetime: datetime.datetime = Field(title="Obs Datetime")

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
            "obsValue": "obs_value",
            "qcTypeLog": "qc_type_log",
            "dataForm": "data_form",
            "capturedBy": "captured_by",
            "temperatureUnits": "temperature_units",
            "precipitationUnits": "precipitation_units",
            "cloudHeightUnits": "cloud_height_units",
            "visUnits": "vis_units",
            "dataSourceTimeZone": "data_source_timezone"
        }


class ObservationFinalResponse(Response):
    result: List[ObservationFinal] = Field(title="Result")


class ObservationFinalWithChildren(ObservationFinal):
    obselement: obselement_schema.ObsElement = Field(title="Obs Element")
    station: station_schema.Station = Field(title="Station")

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ObservationFinalWithChildrenResponse(Response):
    result: List[ObservationFinalWithChildren] = Field(title="Result")


class ObservationFinalInputGen(CreateObservationFinal):
    pass


class ObservationFinalQueryResponse(ObservationFinalResponse):
    limit: int = Field(title="Limit")
    page: int = Field(title="Page")
    pages: int = Field(title="Pages")
