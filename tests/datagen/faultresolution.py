import uuid
import datetime
from faker import Faker
from climsoft_api.api.faultresolution import schema as faultresolution_schema


fake = Faker()


def get_valid_fault_resolution_input(instrument_fault_report_id: str):
    return faultresolution_schema.CreateFaultResolution(
        resolvedDatetime=datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f"),
        resolvedBy=uuid.uuid4().hex,
        associatedWith=instrument_fault_report_id,
        remarks=fake.sentence(),
    )
