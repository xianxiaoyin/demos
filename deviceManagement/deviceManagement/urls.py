'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion:
Date: 2020-12-19 12:28:05
LastEditTime: 2021-02-01 14:30:56
'''

from django.contrib import admin
from django.urls import path
from devices.views import device_edit, status, devices, index, history_user, delete

urlpatterns = [
    path('', index),
    path('status', status),
    path('devices', devices),
    path('edit', device_edit),
    path('delete', delete),
    path('history/<int:number>', history_user),
    path('admin/', admin.site.urls),
]
