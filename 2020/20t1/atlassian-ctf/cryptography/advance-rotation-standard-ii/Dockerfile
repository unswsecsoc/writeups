FROM python:3.8-alpine

RUN apk update && apk add --no-cache ucspi-tcp

WORKDIR /srv/
COPY ./src/*.py /srv/

EXPOSE 8000
ENTRYPOINT ["tcpserver", "-R", "-H", "-l", "0", "0.0.0.0", "8000", "python", "app.py"]
