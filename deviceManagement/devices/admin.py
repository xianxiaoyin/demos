'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion:
Date: 2020-12-19 12:30:13
LastEditTime: 2021-02-01 13:43:56
'''
from django.contrib import admin
from .models import Devices

@admin.register(Devices)
class DevicesAdmin(admin.ModelAdmin):
    """  后台显示的字段，后台可编辑字段"""
    list_display = ["sn", "bcode", "category", "status", "project", "location",
                    "actual_user", "borrow_wwid", "po_requestor", "comments", "update_at"]

    list_editable = ["bcode", "category", "status", "project", "location",
                    "actual_user", "borrow_wwid", "po_requestor", "comments"]
                    