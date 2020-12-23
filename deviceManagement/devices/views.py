# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2020-12-24 00:13:21
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models  import Devices
from django.db.models import Q
import numpy as np

import json

# 展示所有的设备信息
def devices(request):
    devices = Devices.objects.all()
    return render(request, "index.html", {"devices": devices})

#  更新设别信息
def deviceEdit(request):
    if request.method == 'POST':
        print(request.body)
        return HttpResponse()

# 查看设备详情
def deviceResults(request, id):
    device = Devices.objects.get(id=id)
    return render(request, "detail.html", {"device": device})

# 搜索页面
def deviceFilter(request):
    filterdata = request.GET.get("filterdata")
    devices = Devices.objects.filter(Q(sn=filterdata)|Q(bcode=filterdata)|Q(gategory=filterdata) )
    return render(request, "index.html", {"devices": devices})

def deviceDebug(request):
    data = [{ "id": 1, "name": "Item 1", "price": "￥1" },
    { "id": 2, "name": "Item 2", "price": "￥2" },
    { "id": 3, "name": "Item 3", "price": "￥3" }]
    return  HttpResponse(json.dumps({'data': data}))

def deviceTest(request):
    return render(request, "test.html")