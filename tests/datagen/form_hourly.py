import uuid
import random
from faker import Faker
from climsoft_api.api.form_hourly import schema as form_hourly_schema


fake = Faker()


def get_valid_form_hourly_input():
    return form_hourly_schema.CreateFormHourly(
        stationId=uuid.uuid4().hex,
        elementId=random.randint(10, 1000),
        yyyy=random.randint(1900, 2022),
        mm=random.randint(1, 12),
        dd=random.randint(0, 30),
        hh_00=uuid.uuid4().hex,
        flag00=random.choice(['a', 'b', 'c', 'd', 'e'])
    )
