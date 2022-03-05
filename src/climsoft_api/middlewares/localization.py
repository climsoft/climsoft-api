import gettext
import os

from fastapi import Request

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


class LocalizationMiddleware:
    def __init__(
        self,
        domain: str = "climsoft_messages",
        translation_dir: str = os.path.join(
            BASE_DIR, "locale"
        ),
    ):
        self.translation_dir = translation_dir
        self.domain = domain

    async def __call__(self, request: Request, call_next):
        language_code = request.headers.get('accept-language')

        if language_code is None:
            language_code = request.query_params.get("lang")

        if type(language_code) is not str:
            response = await call_next(request)
            return response

        language_code: str = language_code.split(',')[0]

        if language_code.startswith("fr"):
            language_code = "fr"

        if language_code.startswith("en"):
            language_code = "en"

        language = gettext.translation(
            domain=self.domain,
            localedir=self.translation_dir,
            languages=[language_code],
        )

        language.install()

        request.state.gettext = language.gettext

        response = await call_next(request)
        return response
