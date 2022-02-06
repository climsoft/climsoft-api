FROM python:3.9.7-slim-bullseye

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
RUN apt-get install -y curl git && pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip install -r requirements.txt

COPY ./src ./
COPY ./entrypoint.sh ./entrypoint.sh
COPY ./initdb.py ./initdb.py

ENTRYPOINT [ "/bin/sh", "entrypoint.sh" ]
