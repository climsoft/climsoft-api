import uuid
import datetime
from faker import Faker
from climsoft_api.api.paperarchive import schema as paperarchive_schema


fake = Faker()


def get_valid_paper_archive_input(station_id: str, paper_archive_definition_id: str):
    return paperarchive_schema.CreatePaperArchive(
        **dict(
            belongs_to=station_id,
            form_datetime=datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            image=uuid.uuid4().hex,
            classified_into=paper_archive_definition_id,
        )
    )
