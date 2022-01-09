import random
from faker import Faker
from climsoft_api.api.qcstatusdefinition import schema as qcstatusdefinition_schema


fake = Faker()


def get_valid_qc_status_definition_input():
    return qcstatusdefinition_schema.QCStatusDefinition(
        code=random.randint(1000000, 10000000), description=" ".join(fake.sentences())
    )
