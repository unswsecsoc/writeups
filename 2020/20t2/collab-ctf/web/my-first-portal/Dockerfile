FROM python:3.8-slim-buster

# set work directory
WORKDIR /app

# install dependencies
RUN pip install gunicorn
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt

# copy project
COPY . /app/

USER 1000:1000
EXPOSE 5000/tcp

CMD ["gunicorn", "-k", "gevent", "-w", "2", "--bind" ,"0.0.0.0:5000", "app:app"]
