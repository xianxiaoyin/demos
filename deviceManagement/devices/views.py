# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2020-12-19 18:42:34
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models  import Devices

# 展示所有的设备信息
def devices(request):
    devices = Devices.objects.all()
    return render(request, "index.html", {"devices": devices})

#  更新设别信息
def deviceEdit(request):
    pass

# 查看设备详情
def deviceResults(request, sn):
    pass
