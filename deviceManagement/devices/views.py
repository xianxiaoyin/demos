# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2021-01-19 16:45:56
'''
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Devices, Status, HistoryUser
from django.db.models import Q
import json
import datetime


# 首页
def Index(request):
    filename = request.FILES.get("excelfile")
    if filename:
        from utils.exportexcel import saveData, initStatus
        initStatus(filename)
        saveData(filename)
        return render(request, "index.html", {"msg": "file upload successful"})
    else:
        return render(request, "index.html")


#  更新设别信息
def deviceEdit(request):
    if request.method == 'POST':
        data = request.POST
        a = json.loads(json.dumps(data))
        try:
            del a["0"]
        except Exception as e:
            print("why 0 ?")
        a["update_at"] = datetime.datetime.now()
        uuid = a.pop("id")
        # 如果更新了actual_user字段，把更新记录存储到HistoryUser表中
        oldDevices = Devices.objects.get(id=uuid)
        if  oldDevices.actual_user and oldDevices.actual_user != a["actual_user"]  :
            HistoryUser.objects.create(
                    device_number = uuid,
                    change_user = oldDevices.actual_user
            )

        Devices.objects.filter(id=uuid).update(**a)
        return JsonResponse({"status": "success"}, safe=False)



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
                                         Q(bcode__contains=inputsearch)|
                                         Q(comments__contains=inputsearch)).order_by("-update_at").values()
    else:
        devices = Devices.objects.all().order_by("-update_at").values()
    devices = list(devices)
    return JsonResponse(devices, safe=False)


# 获取当前设备的借用记录

def historyuser(request, number):
    if number:
        data = HistoryUser.objects.filter(device_number=number).order_by("-create_at")
    else:
        data = {}
    # return JsonResponse(list(data), safe=False)
    return render(request, "history.html", {"data": data})

# 删除数据
def deletes(request):
    if request.method == 'DELETE':
        ids1 = request.POST
        print(ids1) 
        ids = request.body.decode("utf-8")
        print(ids)
        for i in ids:
            print(i)
            HistoryUser.objects.filter(tag=i).delete()
            Devices.objects.filter(id=i).delete()
        return JsonResponse({"msg": "successful"}, safe=False)