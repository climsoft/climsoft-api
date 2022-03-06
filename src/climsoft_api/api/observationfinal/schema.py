import datetime
from typing import List, Optional

import climsoft_api.api.obselement.schema as obselement_schema
import climsoft_api.api.station.schema as station_schema
from climsoft_api.api.schema import Response, BaseSchema
from pydantic import constr, StrictStr, Field


class CreateObservationFinal(BaseSchema):
    recordedFrom: constr(max_length=255) = Field(title=_("Recorded From"))
    describedBy: int = Field(title=_("Described By"))
    obsDatetime: StrictStr = Field(title=_("Obs Datetime"))
    qcStatus: int = Field(title=_("QC Status"))
    acquisitionType: int = Field(title=_("Acquisition Type"))
    obsLevel: constr(max_length=255) = Field(title=_("Obs Level"))
    obsValue: constr(max_length=255) = Field(title=_("ObsValue"))
    flag: constr(max_length=255) = Field(title=_("Flag"))
    period: Optional[int] = Field(title=_("Period"))
    qcTypeLog: Optional[str] = Field(title=_("QC Type Log"))
    dataForm: Optional[constr(max_length=255)] = Field(title=_("Data Form"))
    capturedBy: Optional[constr(max_length=255)] = Field(title=_("Captured By"))
    mark: Optional[bool] = Field(title=_("Mark"))
    temperatureUnits: Optional[constr(max_length=255)] = Field(title=_("Temperature Units"))
    precipitationUnits: Optional[constr(max_length=255)] = Field(title=_("Precipitation Units"))
    cloudHeightUnits: Optional[constr(max_length=255)] = Field(title=_("Cloud Height Units"))
    visUnits: Optional[constr(max_length=255)] = Field(title=_("Vis Units"))
    dataSourceTimeZone: int = Field(title=_("Data Source Timezone"))

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
    qcStatus: int = Field(title=_("QC Status"))
    acquisitionType: int = Field(title=_("Acquisition Type"))
    obsLevel: constr(max_length=255) = Field(title=_("Obs Level"))
    obsValue: constr(max_length=255) = Field(title=_("Obs Value"))
    flag: constr(max_length=255) = Field(title=_("Flag"))
    period: Optional[int] = Field(title=_("Period"))
    qcTypeLog: Optional[str] = Field(title=_("QC Type Log"))
    dataForm: Optional[constr(max_length=255)] = Field(title=_("Data Form"))
    capturedBy: Optional[constr(max_length=255)] = Field(title=_("Captured By"))
    mark: Optional[bool] = Field(title=_("Mark"))
    temperatureUnits: Optional[constr(max_length=255)] = Field(title=_("Temperature Units"))
    precipitationUnits: Optional[constr(max_length=255)] = Field(title=_("Precipitation Units"))
    cloudHeightUnits: Optional[constr(max_length=255)] = Field(title=_("Cloud Height Units"))
    visUnits: Optional[constr(max_length=255)] = Field(title=_("Vis Units"))
    dataSourceTimeZone: int = Field(title=_("Data Source Timezone"))

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
    obsDatetime: datetime.datetime = Field(title=_("Obs Datetime"))

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
    result: List[ObservationFinal] = Field(title=_("Result"))


class ObservationFinalWithChildren(ObservationFinal):
    obselement: obselement_schema.ObsElement = Field(title=_("Obs Element"))
    station: station_schema.Station = Field(title=_("Station"))

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ObservationFinalWithChildrenResponse(Response):
    result: List[ObservationFinalWithChildren] = Field(title=_("Result"))


class ObservationFinalInputGen(CreateObservationFinal):
    pass


class ObservationFinalQueryResponse(ObservationFinalResponse):
    limit: int = Field(title=_("Limit"))
    page: int = Field(title=_("Page"))
    pages: int = Field(title=_("Pages"))
