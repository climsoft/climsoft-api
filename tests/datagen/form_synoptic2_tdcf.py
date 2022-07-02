import uuid
import random
from faker import Faker
from climsoft_api.api.form_synoptic2_tdcf import schema as form_synoptic2_tdcf_schema


fake = Faker()


def get_valid_form_synoptic2_tdcf_input():
    return form_synoptic2_tdcf_schema.CreateFormSynoptic2Tdcf(
        stationId=uuid.uuid4().hex[:10],
        yyyy=random.randint(1900, 2022),
        mm=random.randint(1, 12),
        dd=random.randint(0, 30),
        hh=random.randint(0, 23),
        _106=uuid.uuid4().hex[:6],
        flag01=random.choice(['a', 'b', 'c', 'd', 'e'])
    )
