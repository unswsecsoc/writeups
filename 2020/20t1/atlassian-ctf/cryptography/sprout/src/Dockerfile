FROM python:3.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && rm -r /tmp/requirements.txt

WORKDIR /app
COPY ./src/ /app/

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]
