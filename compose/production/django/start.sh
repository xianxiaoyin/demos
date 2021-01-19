#!/usr/bin/env bash

python manage.py migrate --settings=deviceManagement.settings.prc
python manage.py collectstatic --noinput  --settings=deviceManagement.settings.prc
gunicorn --env DJANGO_SETTINGS_MODULE=deviceManagement.settings.prc  deviceManagement.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/root/devices/deviceManagement 
