import datetime
from typing import List, Optional
from pydantic import constr, StrictStr
from climsoft_api.api.schema import Response, BaseSchema
import climsoft_api.api.station.schema as station_schema
import climsoft_api.api.obselement.schema as obselement_schema


class CreateObservationFinal(BaseSchema):
    recordedFrom: constr(max_length=255)
    describedBy: int
    obsDatetime: StrictStr
    qcStatus: int
    acquisitionType: int
    obsLevel: constr(max_length=255)
    obsValue: constr(max_length=255)
    flag: constr(max_length=255)
    period: Optional[int]
    qcTypeLog: Optional[str]
    dataForm: Optional[constr(max_length=255)]
    capturedBy: Optional[constr(max_length=255)]
    mark: Optional[bool]
    temperatureUnits: Optional[constr(max_length=255)]
    precipitationUnits: Optional[constr(max_length=255)]
    cloudHeightUnits: Optional[constr(max_length=255)]
    visUnits: Optional[constr(max_length=255)]
    dataSourceTimeZone: int

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
    qcStatus: int
    acquisitionType: int
    obsLevel: constr(max_length=255)
    obsValue: constr(max_length=255)
    flag: constr(max_length=255)
    period: Optional[int]
    qcTypeLog: Optional[str]
    dataForm: Optional[constr(max_length=255)]
    capturedBy: Optional[constr(max_length=255)]
    mark: Optional[bool]
    temperatureUnits: Optional[constr(max_length=255)]
    precipitationUnits: Optional[constr(max_length=255)]
    cloudHeightUnits: Optional[constr(max_length=255)]
    visUnits: Optional[constr(max_length=255)]
    dataSourceTimeZone: int

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
    obsDatetime: datetime.datetime

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
    result: List[ObservationFinal]


class ObservationFinalWithChildren(ObservationFinal):
    obselement: obselement_schema.ObsElement
    station: station_schema.Station

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class ObservationFinalWithChildrenResponse(Response):
    result: List[ObservationFinalWithChildren]


class ObservationFinalInputGen(CreateObservationFinal):
    pass
