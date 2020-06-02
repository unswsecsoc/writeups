FROM python:3.7-slim-buster

RUN apt-get update && apt-get install -y sqlite firefox-esr

COPY app_requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY ./src/ /app/
COPY ./entrypoint.sh /

COPY db/schema.sql /tmp
RUN rm /app/phonenumbers.db && sqlite3 /app/phonenumbers.db < /tmp/schema.sql && rm /tmp/schema.sql

EXPOSE 8000
ENTRYPOINT ["/entrypoint.sh"]

