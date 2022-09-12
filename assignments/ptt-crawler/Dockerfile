FROM python:3.10-slim

WORKDIR /app

COPY ./Pipfile* ./

RUN pip install pipenv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
    pipenv install --deploy --system && \
    apt-get remove -y gcc python3-dev libssl-dev && \
    apt-get autoremove -y && \
    pip uninstall pipenv -y

COPY ./scrapy.cfg ./
COPY ./scraptt ./scraptt