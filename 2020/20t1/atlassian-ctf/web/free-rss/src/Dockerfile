FROM python:3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

WORKDIR /app
COPY ./src/ /app/
COPY entrypoint.sh /

COPY ./meta/flag /flag

EXPOSE 8001

ENTRYPOINT ["/entrypoint.sh"]
