FROM python:3.10.13-alpine3.18
MAINTAINER toropow@gmail.com

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt  --no-cache-dir

COPY . /app

CMD python -m pytest -vv tests/