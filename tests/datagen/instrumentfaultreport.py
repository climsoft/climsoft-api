import uuid
import random
import datetime
from faker import Faker
from climsoft_api.api.instrumentfaultreport import (
    schema as instrumentfaultreport_schema,
)


fake = Faker()


def get_valid_instrument_fault_report_input(station_id: str, instrument_id: str):
    return instrumentfaultreport_schema.CreateInstrumentFaultReport(
        refersTo=instrument_id,
        reportId=random.randint(10000, 1000000),
        reportDatetime=datetime.datetime.utcnow().isoformat(),
        faultDescription=" ".join(fake.sentences()),
        reportedBy=uuid.uuid4().hex,
        receivedDatetime=datetime.datetime.utcnow().isoformat(),
        receivedBy=uuid.uuid4().hex,
        reportedFrom=station_id,
    )
