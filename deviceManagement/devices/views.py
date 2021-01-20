# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2021-01-20 10:35:16
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
        print(a)

        try:
            del a["0"]
        except Exception as e:
            print("why 0 ?")
        a["update_at"] = datetime.datetime.now()
        uuid = a.pop("id")
        # 如果更新了actual_user字段，把更新记录存储到HistoryUser表中
        oldDevices, created = Devices.objects.get_or_create(sn=a["sn"])

        if not created:
            try:
                if oldDevices.actual_user and oldDevices.actual_user != a["actual_user"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            actual_user=oldDevices.actual_user
                    )
                if oldDevices.bcode and oldDevices.bcode != a["bcode"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            bcode=oldDevices.bcode
                    )
                if oldDevices.category and oldDevices.category != a["category_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            category=oldDevices.category.name)
                if oldDevices.status and oldDevices.status != a["status_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            status=oldDevices.status.name
                    )
                if oldDevices.project and oldDevices.project != a["project_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            project=oldDevices.project.name
                    )
                if oldDevices.location and oldDevices.location != a["location_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            location=oldDevices.location.name
                    )

                if oldDevices.borrow_wwid and oldDevices.borrow_wwid != a["borrow_wwid"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            borrow_wwid=oldDevices.borrow_wwid
                    )
                if oldDevices.comments and oldDevices.comments != a["comments"]:
                    HistoryUser.objects.create(
                        device_number=uuid,
                        comments=oldDevices.comments
                    )
            except Exception as e:
                print(e)

            Devices.objects.filter(sn=a["sn"]).update(**a)
            return JsonResponse({"status": "update success"}, safe=False)
        else:
            return JsonResponse({"status": "create success"}, safe=False)



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
    return render(request, "history.html", {"data": data})


# 删除数据
def delete(request):
    if request.method == 'DELETE':
        ids = json.loads(request.body.decode("utf-8")).get("ids", "")
        for i in ids:
            HistoryUser.objects.filter(device_number=i).delete()
            Devices.objects.filter(id=i).delete()
        return JsonResponse({"msg": "successful"}, safe=False)

