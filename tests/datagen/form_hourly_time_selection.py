import uuid
import random
from faker import Faker
from climsoft_api.api.form_hourly_time_selection import schema as form_hourly_time_selection_schema


fake = Faker()


def get_valid_form_hourly_time_selection_input():
    return form_hourly_time_selection_schema.CreateFormHourlyTimeSelection(
        hh=random.randint(1, 10),
        hh_selection=random.randint(1, 4)
    )
