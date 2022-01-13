import uuid
from faker import Faker
from climsoft_api.api.synopfeature import schema as synopfeature_schema


fake = Faker()


def get_valid_synop_feature_input():
    return synopfeature_schema.SynopFeature(
        abbreviation=uuid.uuid4().hex, description=" ".join(fake.sentences())
    )
