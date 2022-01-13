import uuid
import random
import datetime
from faker import Faker
from climsoft_api.api.stationqualifier import schema as stationqualifier_schema


fake = Faker()


def get_valid_station_qualifier_input(station_id: str):
    return stationqualifier_schema.StationQualifier(
        qualifier=uuid.uuid4().hex,
        qualifierBeginDate=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ"),
        qualifierEndDate=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ"),
        belongsTo=station_id,
        stationTimeZone=random.randint(10, 90),
        stationNetworkType=uuid.uuid4().hex,
    )
