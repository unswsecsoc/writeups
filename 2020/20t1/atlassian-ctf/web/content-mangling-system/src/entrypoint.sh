#!/bin/sh
gunicorn -t 10 --graceful-timeout 10 -k gevent -b 0.0.0.0:8000 server:app
