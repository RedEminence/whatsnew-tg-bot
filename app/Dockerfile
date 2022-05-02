FROM python:3.10
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1
WORKDIR /usr/src/app
COPY requirements.txt .

RUN apt update \
    && apt install --no-install-recommends --no-install-suggests -y python3-dev libpq-dev gcc netcat\
    && python -m pip install --upgrade pip \
    && pip3 install -r requirements.txt

COPY . .
