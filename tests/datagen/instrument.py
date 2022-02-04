import uuid
import random
import datetime
from faker import Faker
from climsoft_api.api.instrument import schema as instrument_schema


fake = Faker()


def get_valid_instrument_input(station_id: str):
    return instrument_schema.CreateInstrument(
        instrumentId=uuid.uuid4().hex,
        instrumentName=uuid.uuid4().hex,
        abbreviation=uuid.uuid4().hex,
        serialNumber=uuid.uuid4().hex,
        model=uuid.uuid4().hex,
        manufacturer=uuid.uuid4().hex,
        instrumentUncertainty=random.random(),
        installationDatetime=datetime.datetime.utcnow().isoformat(),
        deinstallationDatetime=(
            datetime.datetime.utcnow() + datetime.timedelta(days=1234)
        ).isoformat(),
        height=uuid.uuid4().hex,
        installedAt=station_id,
        instrumentPicture=uuid.uuid4().hex,
    )
