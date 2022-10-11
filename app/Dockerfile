FROM python:alpine

WORKDIR /src/

RUN apk add --no-cache postgresql-dev

COPY requirements.dev.txt .
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    && pip install --no-cache-dir -r requirements.dev.txt \
    && apk del --no-cache .build-deps \
    && wget -qO /bin/wait-for https://raw.githubusercontent.com/eficode/wait-for/v2.1.3/wait-for && chmod +x /bin/wait-for
