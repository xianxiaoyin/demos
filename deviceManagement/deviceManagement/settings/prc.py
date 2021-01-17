# coding: utf-8

from .base import *
DEBUG = False
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'devices',
        'USER': 'admin',
        'PASSWORD': '123456',
        'HOST': 'db',
        'PORT': '3306',
    }
}
