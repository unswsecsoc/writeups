#!/web/cs2041/bin/python3.6.3
##!/usr/bin/python3.6
import os

from wsgiref.handlers import CGIHandler

from run import app

if 'PATH_INFO' not in os.environ:
    os.environ['PATH_INFO'] = ''

CGIHandler().run(app)
