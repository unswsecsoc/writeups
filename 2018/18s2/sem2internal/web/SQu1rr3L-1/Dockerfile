FROM ubuntu:bionic

RUN (export DEBIAN_FRONTEND=noninteractive; apt-get update -y && apt-get install -y \
    apt-utils \
    python3 \
    python3-pip \
    wget \
    vim \
    less \
    locales)
RUN locale-gen en_AU.UTF-8

RUN (export DEBIAN_FRONTEND=noninteractive; apt-get update -y && apt-get install -y \
    python3-flask \
    python3-setproctitle \
    gunicorn3)

COPY app.py /app/
COPY static/* /app/static/
COPY templates/* /app/templates/
COPY secrets/auth secrets/flag /app/secrets/

ENV LANG en_AU.UTF-8
ENV LC_ALL en_AU.UTF-8

WORKDIR /app/

CMD gunicorn3 --bind='[::]:80' --access-logfile='-' app:app

EXPOSE 80
