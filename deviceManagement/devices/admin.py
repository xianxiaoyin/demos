'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2020-12-19 15:36:12
'''
from django.contrib import admin

from django.contrib import admin
from .models import Devices

@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ["sn", "bcode", "gategory", "status", "project", "functeam", "location", "rowner", "wwid", "comments", "update_at"]
