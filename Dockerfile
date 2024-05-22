FROM python:3.9-alpine3.13
LABEL maintainer="faiznawab"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    #after requirements are installed 
    #installing client pkg for postgres to run in alpine image pkg
    apk add --update --no-cache postgresql-client && \ 
    #virtual dependency pkg : group pkgs into tmp-build-deps
    apk add --update --no-cache --virtual .tmp-build-deps \
        #build-base postgresql-dev musl-dev && \
        gcc musl-dev postgresql-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    #only install if DEV is true in docker compose #shell code
    if [ $DEV = "true" ]; then /py/bin/pip install -r /tmp/requirements.dev.txt; fi && \
    rm -rf /tmp && \
    #removes tmp-builds-deps pkg
    apk del .tmp-build-deps && \
    adduser \
        --disabled-password \
        --no-create-home  \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user