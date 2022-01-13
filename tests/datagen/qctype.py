import random
from faker import Faker
from climsoft_api.api.qctype import schema as qctype_schema


fake = Faker()


def get_valid_qc_type_input():
    return qctype_schema.QCType(
        code=random.randint(1000000, 10000000), description=" ".join(fake.sentences())
    )
