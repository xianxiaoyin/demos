# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2020-12-22 22:32:00
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models  import Devices
from django.db.models import Q

# 展示所有的设备信息
def devices(request):
    devices = Devices.objects.all()
    return render(request, "index.html", {"devices": devices})

#  更新设别信息
def deviceEdit(request):
    pass

# 查看设备详情
def deviceResults(request, id):
    print(id)
    device = Devices.objects.get(id=id)
    return render(request, "detail.html", {"device": device})

# 搜索页面
def deviceFilter(request):
    filterdata = request.GET.get("filterdata")
    devices = Devices.objects.filter(Q(sn=filterdata)|Q(bcode=filterdata)|Q(gategory=filterdata) )
    return render(request, "index.html", {"devices": devices})
