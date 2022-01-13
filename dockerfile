FROM python:3.9.7-slim-bullseye

# https://docs.python.org/3/using/cmdline.html#envvar
# https://pip.pypa.io/en/stable/user_guide/#environment-variables
# https://python-poetry.org/docs/configuration/
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.11 \
    POETRY_VIRTUALENVS_CREATE=0

RUN apt-get update --fix-missing
RUN apt-get install -y g++ libgdal-dev libpq-dev libgeos-dev libproj-dev openjdk-17-jre vim wait-for-it
RUN apt-get install -y curl git && pip install --upgrade pip "poetry==${POETRY_VERSION}"

WORKDIR /code


# Install Python dependencies.
COPY pyproject.toml poetry.lock ./


RUN poetry install -v


COPY . .


RUN poetry install

RUN useradd -m climsoft_api_user && chown -R climsoft_api_user /code


USER climsoft_api_user

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
