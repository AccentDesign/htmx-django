FROM        accent/python-uvicorn-gunicorn:3.12 as base

ARG         ENVIRONMENT=production

WORKDIR     /app

COPY        ./src/pyproject.toml ./src/poetry.lock ./

RUN         pip install poetry \
            && poetry config virtualenvs.create false \
            && poetry install $(test "$ENVIRONMENT" = production && echo "--only main") --no-interaction --no-ansi \
            && rm -rf /root/.cache/pypoetry

FROM        base as final

ENV         APP_MODULE=app.asgi:application
ENV         PYTHONUNBUFFERED=1
ENV         PYTHONDONTWRITEBYTECODE=1
ENV         DJANGO_SETTINGS_MODULE=app.settings
ENV         DJANGO_MANAGEPY_MIGRATE=on
ENV         DJANGO_MANAGEPY_COLLECTSTATIC=on
ENV         SECRET_KEY='***** change me *****'
ENV         HASHIDS_SALT='***** change me *****'
ENV         ALLOWED_HOSTS=*
ENV         CSRF_TRUSTED_ORIGINS=http://*
ENV         RDS_HOSTNAME=db
ENV         RDS_PORT=5432
ENV         RDS_DB_NAME=postgres
ENV         RDS_USERNAME=postgres
ENV         RDS_PASSWORD=password

WORKDIR     /app

COPY        ./src .