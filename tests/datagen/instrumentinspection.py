import uuid
import datetime
from faker import Faker
from climsoft_api.api.instrumentinspection import schema as instrumentinspection_schema


fake = Faker()


def get_valid_instrument_inspection_input(station_id: str, instrument_id: str):
    return instrumentinspection_schema.CreateInstrumentInspection(
        performedOn=instrument_id,
        inspectionDatetime=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S%f"),
        performedBy=uuid.uuid4().hex,
        status=uuid.uuid4().hex,
        remarks=fake.sentence(),
        performedAt=station_id,
    )
