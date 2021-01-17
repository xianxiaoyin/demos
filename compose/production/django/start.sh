#!/usr/bin/env bash

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn deviceManagement.wsgi:application -w 4 -k gthread -b 0.0.0.0:8000 --chdir=/root/devices/deviceManagement --settings=deviceManagement.settings.prc
~
