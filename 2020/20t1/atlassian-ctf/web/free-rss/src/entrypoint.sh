#!/bin/bash

set -e 

cd /app

gunicorn -b '0.0.0.0:8000' 'file_server:app' &
gunicorn -b '0.0.0.0:8001' -k gevent 'rss:app'
