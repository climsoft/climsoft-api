import enum
import logging

from climsoft_api.utils.response import get_error_response
from fastapi import APIRouter, Depends
from opencdms.models.climsoft.v4_1_1_core import TARGET_TABLES
from sqlalchemy import text
from climsoft_api.api import deps
from sqlalchemy.orm import Session

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
async def get_statistics_for_all_climsoft_tables(
    db_session: Session = Depends(deps.get_session),
):
    try:
        stats = {}
        for _table in TARGET_TABLES:
            result = db_session.execute(
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
            message=_("Failed to get statistics for climsoft tables.")
        )
