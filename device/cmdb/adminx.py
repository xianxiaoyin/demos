# encoding: utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-28 10:26:30
LastEditTime: 2020-12-28 14:39:07
'''

from django.contrib.auth.models import User, Group, Permission
from xadmin.adminx import Log
from reversion.models import Revision


import xadmin
from .models import Devices




class DevicesAdmin(object):
    # 显示的字段
    list_display = ("sn", "bcode", "category" ,"status", "update_at")
    # 搜索条件
    search_fields = ("sn", "bcode", "category" ,"status", "update_at")
    # 每页显示10条
    list_per_page = 10
     
    list_filter = ("sn", "bcode", "category" ,"status", "update_at")
    model_icon = ""





# 注册Devices表
xadmin.site.unregister(User)
xadmin.site.unregister(Group)
xadmin.site.unregister(Permission)
xadmin.site.unregister(Log)
# xadmin.site.unregister(Revision)
xadmin.site.register(Devices, DevicesAdmin)