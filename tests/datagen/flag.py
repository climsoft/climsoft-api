import uuid
import random
from faker import Faker
from climsoft_api.api.flag import schema as flag_schema


fake = Faker()


def get_valid_flag_input():
    return flag_schema.Flag(
        characterSymbol=uuid.uuid4().hex,
        numSymbol=random.randint(1000000, 10000000),
        description=" ".join(fake.sentences()),
    )
