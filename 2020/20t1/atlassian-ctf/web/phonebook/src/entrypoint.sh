#!/bin/sh

gunicorn -b 0.0.0.0:8000 app:app --daemon
python admin.py
