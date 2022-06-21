import uuid
import random
from faker import Faker
from climsoft_api.api.form_synoptic_2_ra1 import schema as form_synoptic_2_ra1_schema


fake = Faker()


def get_valid_form_synoptic_2_ra1_input():
    return form_synoptic_2_ra1_schema.CreateFormSynoptic2Ra1(
        stationId=uuid.uuid4().hex[:10],
        yyyy=random.randint(1900, 2022),
        mm=random.randint(1, 12),
        dd=random.randint(0, 30),
        hh=random.randint(0, 23),
        Val_Elem002=uuid.uuid4().hex[:6],
        Flag002=random.choice(['a', 'b', 'c', 'd', 'e']),
    )
