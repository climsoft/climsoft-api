import uuid
import random
from faker import Faker
from climsoft_api.api.form_monthly import schema as form_monthly_schema


fake = Faker()


def get_valid_form_monthly_input():
    return form_monthly_schema.CreateFormMonthly(
        stationId=uuid.uuid4().hex,
        elementId=random.randint(10, 1000),
        yyyy=random.randint(1900, 2022),
        mm_01=uuid.uuid4().hex,
        mm_04=uuid.uuid4().hex,
        flag01=random.choice(['a', 'b', 'c', 'd', 'e']),
        period01=uuid.uuid4().hex
    )
