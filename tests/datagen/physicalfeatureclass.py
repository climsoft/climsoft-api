import uuid
from faker import Faker
from climsoft_api.api.physicalfeatureclass import schema as physicalfeatureclass_schema


fake = Faker()


def get_valid_physical_feature_class_input(station_id: str):
    return physicalfeatureclass_schema.PhysicalFeatureClass(
        featureClass=station_id, description=uuid.uuid4().hex, refersTo=station_id
    )
