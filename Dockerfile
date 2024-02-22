FROM python:3.11-alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apk add --no-cache \
    zlib-dev \
    jpeg-dev \
    gcc \
    musl-dev \
    chromium \
    chromium-chromedriver

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

ENV CHROME_DRIVER_PATH /usr/bin/chromedriver

COPY . /usr/src/app

RUN chmod -R 755 /usr/src/app
