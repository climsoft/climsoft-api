import random
from faker import Faker
from climsoft_api.api.acquisition_type import schema as acquisitiontype_schema

fake = Faker()


def get_valid_acquisition_type_input():
    return acquisitiontype_schema.CreateAcquisitionType(
        code=random.randint(10000000, 99999999), description=fake.sentence()
    )
