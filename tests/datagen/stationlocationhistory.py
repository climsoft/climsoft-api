import uuid
import random
import datetime
from faker import Faker
from climsoft_api.api.stationlocationhistory import (
    schema as stationlocationhistory_schema,
)


fake = Faker()


def get_valid_station_location_history_input(station_id: str):
    return stationlocationhistory_schema.StationLocationHistory(
        belongsTo=station_id,
        stationType=uuid.uuid4().hex,
        latitude=fake.latitude(),
        longitude=fake.longitude(),
        geoLocationMethod=uuid.uuid4().hex,
        geoLocationAccuracy=random.random(),
        openingDatetime=str(datetime.datetime.utcnow()),
        closingDatetime=str(datetime.datetime.utcnow()),
        elevation=random.randint(10, 80),
        authority=uuid.uuid4().hex,
        adminRegion=uuid.uuid4().hex,
        drainageBasin=uuid.uuid4().hex,
    )
