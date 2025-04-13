FROM python:3.12.10-slim-bookworm AS python-build

WORKDIR /app

COPY ./requirements.txt ./

RUN apt-get update && \
  apt-get install -y \
  gcc \
  default-libmysqlclient-dev \
  pkg-config \
  curl && \
  pip install --no-cache-dir -r requirements.txt && \
  apt-get remove -y \
  gcc \
  pkg-config && \
  rm -rf /var/lib/apt/lists/*

COPY . .

EXPOSE 8000