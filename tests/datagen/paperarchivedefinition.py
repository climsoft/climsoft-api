import uuid
from faker import Faker
from climsoft_api.api.paperarchivedefinition import (
    schema as paperarchivedefinition_schema,
)


fake = Faker()


def get_valid_paper_archive_definition_input():
    return paperarchivedefinition_schema.PaperArchiveDefinition(
        formId=uuid.uuid4().hex, description=" ".join(fake.sentences())
    )
