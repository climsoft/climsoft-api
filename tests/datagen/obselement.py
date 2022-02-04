import uuid
import random
from faker import Faker
from climsoft_api.api.obselement import schema as obselement_schema


fake = Faker()


def get_valid_obselement_input():
    return obselement_schema.CreateObsElement(
        elementId=random.randint(10000000, 10000000000),
        elementName=uuid.uuid4().hex,
        abbreviation=uuid.uuid4().hex,
        description=uuid.uuid4().hex,
        elementScale=random.random() * 100000,
        upperLimit=uuid.uuid4().hex,
        lowerLimit=uuid.uuid4().hex,
        units=uuid.uuid4().hex,
        elementtype=uuid.uuid4().hex,
        qcTotalRequired=random.randint(10000, 100000),
        selected=True,
    )
