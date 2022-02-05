import datetime
from faker import Faker
from climsoft_api.api.featuregeographicalposition import (
    schema as featuregeographicalposition_schema,
)


fake = Faker()


def get_valid_feature_geographical_position_input(synop_feature_abbreviation: str):
    return featuregeographicalposition_schema.CreateFeatureGeographicalPosition(
        belongsTo=synop_feature_abbreviation,
        observedOn=datetime.datetime.utcnow().isoformat(),
        latitude=fake.latitude(),
        longitude=fake.longitude(),
    )
