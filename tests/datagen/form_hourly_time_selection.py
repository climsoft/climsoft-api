import uuid
import random
from faker import Faker
from climsoft_api.api.form_hourly_time_selection import schema as form_hourly_time_selection_schema


fake = Faker()


def get_valid_form_hourly_time_selection_input():
    choices = [
        form_hourly_time_selection_schema.CreateFormHourlyTimeSelection(
            hh=i,
            hh_selection=i%5
        ) for i in range(1, 100000)]

    return random.choice(choices)

