#!/bin/sh
/usr/local/bin/gunicorn config.wsgi -b 0.0.0.0:$PORT -w 3 --chdir=/app
