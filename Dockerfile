FROM python:alpine

ARG run_env=only_run
ENV env $run_env

WORKDIR ./usr/PulseWave

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .
