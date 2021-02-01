'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 测试环境配置
Date: 2021-01-19 09:43:22
LastEditTime: 2021-02-01 13:34:58
'''
# coding: utf-8
from .base import *
DEBUG = True
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
