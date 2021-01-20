'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2021-01-19 09:43:22
LastEditTime: 2021-01-20 11:22:19
'''
# coding: utf-8

from .base import *
DEBUG = True
# DEBUG = False
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
