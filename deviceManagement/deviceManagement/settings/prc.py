# coding: utf-8

from .base import *
SECRET_KEY = '#)o+^3*jl2d#qxq21w*8zl9rba^)*ygh+=z(f89@^&+#to0)e_'
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
