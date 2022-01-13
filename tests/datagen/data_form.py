import uuid
import random
from faker import Faker
from climsoft_api.api.data_form import schema as data_form_schema


fake = Faker()


def get_valid_data_form_input():
    return data_form_schema.DataForm(
        form_name=uuid.uuid4().hex,
        order_num=random.randint(10000, 100000),
        table_name=uuid.uuid4().hex,
        description=fake.sentence(),
        selected=True,
        val_start_position=random.randint(10000, 1000000),
        val_end_position=random.randint(10000, 1000000),
        elem_code_location=uuid.uuid4().hex,
        sequencer=uuid.uuid4().hex,
        entry_mode=True,
    )
