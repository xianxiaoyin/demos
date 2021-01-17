#!/usr/bin/env bash
python manage.py migrate
python  manage.py   runserver 0:8080 --settings=deviceManagement.settings.dev
