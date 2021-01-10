# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2021-01-05 18:24:07
'''
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Devices, Status
from django.db.models import Q
import json
import datetime


# 首页
def Index(request):
    filename = request.FILES.get("excelfile")
    if filename:
        from utils.exportexcel import saveData, initStatus
        # initStatus(filename)
        saveData(filename)
        return render(request, "testtable.html", {"msg": "file upload successful"})
    else:
        return render(request, "testtable.html")


#  更新设别信息
def deviceEdit(request):
    if request.method == 'POST':
        data = request.POST
        a = json.loads(json.dumps(data))
        a["update_at"] = datetime.datetime.now()
        uuid = a.pop("id")
        Devices.objects.filter(id=uuid).update(**a)
        return JsonResponse({"status": "success"}, safe=False)


#  上传excel
def uploadExcel(request):
    filename = request.FILES.get("excelfile")
    if filename:
        from utils.exportexcel import saveData, initStatus
        # initStatus(filename)
        saveData(filename)
        return render(request, "testtable.html", {"msg": "file upload successful"})
    else:
        return render(request, "testtable.html", {"msg": "file upload error"})


# 获取状态
def status(request):
    tag = request.GET.get("tag")
    data = Status.objects.filter(tag=tag).values()
    data = list(data)
    return JsonResponse(data, safe=False)


# 获取所有信息
def devices(request):
    inputsearch = request.GET.get("inputsearch")
    if inputsearch:
        devices = Devices.objects.filter(Q(sn__contains=inputsearch) |
                                         Q(bcode__contains=inputsearch)).order_by("-update_at").values()
    else:
        devices = Devices.objects.all().order_by("-update_at").values()
    devices = list(devices)
    return JsonResponse(devices, safe=False)
