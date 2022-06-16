import uuid
import random
from faker import Faker
from climsoft_api.api.form_hourlywind import schema as form_hourlywind_schema


fake = Faker()


def get_valid_form_hourlywind_input():
    return form_hourlywind_schema.CreateFormHourlyWind(
        stationId=uuid.uuid4().hex,
        yyyy=random.randint(1900, 2022),
        mm=random.randint(1, 12),
        dd=random.randint(0, 30),
        elem_111_00=uuid.uuid4().hex[:2],
        elem_112_00=uuid.uuid4().hex[:2],
        ddflag00=random.choice(['a', 'b', 'c', 'd', 'e'])
    )
