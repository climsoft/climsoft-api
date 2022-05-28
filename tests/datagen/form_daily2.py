import uuid
import random
from faker import Faker
from climsoft_api.api.form_daily2 import schema as form_daily2_schema


fake = Faker()


def get_valid_form_daily2_input():
    return form_daily2_schema.CreateFormDaily2(
        stationId=uuid.uuid4().hex,
        elementId=random.randint(10, 1000),
        yyyy=random.randint(1900, 2022),
        mm=random.randint(1, 12),
        hh=random.randint(0, 23),
        day01=uuid.uuid4().hex,
        flag01=random.choice(['a', 'b', 'c', 'd', 'e']),
        period01=uuid.uuid4().hex
    )
