FROM python:3-alpine3.12
LABEL maintainer="whitespots.io"
RUN adduser -D -u 1001 whitespots whitespots

ARG serpstack_token=""

RUN set -xe \
    && apk add --no-cache git jq curl \
    && rm -rf /var/cache/apk/*

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

USER whitespots
ENTRYPOINT []
