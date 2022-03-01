import logging
from fastapi import APIRouter
from climsoft_api.utils.response import get_error_response
from opencdms.models.climsoft.v4_1_1_core import TARGET_TABLES
from climsoft_api.db import engine
from sqlalchemy import text
import enum

router = APIRouter()

logger = logging.getLogger(__file__)
logging.basicConfig(level=logging.INFO)


class ClimsoftTables(str, enum.Enum):
    acquisitiontype = 'acquisitiontype'
    data_forms = 'data_forms'
    flags = 'flags'
    obselement = 'obselement'
    paperarchivedefinition = 'paperarchivedefinition'
    qcstatusdefinition = 'qcstatusdefinition'
    qctype = 'qctype'
    regkeys = 'regkeys'
    station = 'station'
    synopfeature = 'synopfeature'
    featuregeographicalposition = 'featuregeographicalposition'
    instrument = 'instrument'
    observationfinal = 'observationfinal'
    observationinitial = 'observationinitial'
    obsscheduleclass = 'obsscheduleclass'
    paperarchive = 'paperarchive'
    physicalfeatureclass = 'physicalfeatureclass'
    stationlocationhistory = 'stationlocationhistory'
    stationqualifier = 'stationqualifier'
    instrumentfaultreport = 'instrumentfaultreport'
    instrumentinspection = 'instrumentinspection'
    observationschedule = 'observationschedule'
    physicalfeature = 'physicalfeature'
    stationelement = 'stationelement'
    faultresolution = 'faultresolution'
    climsoftusers = 'climsoftusers'


@router.get(
    "/statistics",
)
# async def get_statistics_for_all_climsoft_tables(table: ClimsoftTables):
async def get_statistics_for_all_climsoft_tables():
    try:
        stats = {}
        for _table in TARGET_TABLES:
            with engine.connect() as connection:
                result = connection.execute(
                    text(f"SELECT COUNT(*) as count FROM {_table};")
                )
                count = [row['count'] for row in result][0]
            stats[_table] = count
        return stats
    except TypeError:
        raise
    except Exception as e:
        logger.exception(e)
        return get_error_response(
            message=_("Failed getting statistics for climsoft tables.")
        )

