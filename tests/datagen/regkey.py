import uuid
from faker import Faker
from climsoft_api.api.regkey import schema as regkey_schema


fake = Faker()


def get_valid_reg_key_input():
    return regkey_schema.RegKey(
        keyName=uuid.uuid4().hex,
        keyValue=uuid.uuid4().hex,
        keyDescription=" ".join(fake.sentences()),
    )
