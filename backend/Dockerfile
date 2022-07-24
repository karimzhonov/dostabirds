FROM python:3.8

RUN apt-get update -y

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG=1

COPY . .

RUN pip install -r requirements.txt