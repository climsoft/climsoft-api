import gettext
import os.path
from climsoft_api.api.stationelement.schema import StationElementWithStation
from climsoft_api.utils.response import translate_schema


ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)


LOCALE_DIR = os.path.join(
    ROOT_DIR,
    "src/climsoft_api/locale"
)


def test_should_translate_schema_successfully():
    language = gettext.translation(
        domain="climsoft_messages",
        localedir=LOCALE_DIR,
        languages=["fr"],
    )

    language.install()

    translated_schema = translate_schema(
        language.gettext,
        StationElementWithStation.schema()
    )

    assert translated_schema[
               "definitions"
           ][
               "Station"
           ][
               "properties"
           ][
               "station_name"
           ][
               "title"
           ] == "Nom de la station"

