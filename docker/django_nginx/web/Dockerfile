# base image
FROM python:3.12.5-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt requirements.txt

# Upgrading pip version
RUN pip install --upgrade pip

# Installing dependencies
RUN pip install gunicorn

# install dependencies
RUN pip install -r requirements.txt

# copy whole project to your docker home directory.
COPY . .
