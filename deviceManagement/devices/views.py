# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2021-01-27 14:21:32
'''
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Devices, Status, HistoryUser
from django.db.models import Q
import json
import datetime
import logging
logger = logging.getLogger(__name__)
 

# 首页
def Index(request):
    filename = request.FILES.get("excelfile")
    if filename:
        from utils.exportexcel import saveData, initStatus
        logger.info("开始初始化数据库······")
        initStatus(filename)
        logger.info("初始化数据库结束······")
        logger.info("开始导入数据······")
        saveData(filename)
        logger.info("导入数据结束······")
        return render(request, "index.html", {"msg": "file upload successful"})
    else:
        return render(request, "index.html")


#  更新设别信息
def deviceEdit(request):
    if request.method == 'POST':
        post = request.POST
        data = json.loads(json.dumps(post))
        try:
            del data["0"]
        except Exception as e:
            logger.warning("删除临时数据错误，忽略此信息~")
        data["update_at"] = datetime.datetime.now()
        oldid = data.get("id", "")
        # uuid = data.pop("id")
        # 如果更新了actual_user字段，把更新记录存储到HistoryUser表中
        if oldid:
            uuid = data.pop("id")
            oldDevices= Devices.objects.get(id=uuid)
            try:
                if oldDevices.actual_user and oldDevices.actual_user != data["actual_user"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            actual_user=oldDevices.actual_user
                    )
                if oldDevices.bcode and oldDevices.bcode != data["bcode"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            bcode=oldDevices.bcode
                    )
                if oldDevices.category and oldDevices.category != data["category_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            category=oldDevices.category.name)
                if oldDevices.status and oldDevices.status != data["status_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            status=oldDevices.status.name
                    )
                if oldDevices.project and oldDevices.project != data["project_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            project=oldDevices.project.name
                    )
                if oldDevices.location and oldDevices.location != data["location_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            location=oldDevices.location.name
                    )

                if oldDevices.borrow_wwid and oldDevices.borrow_wwid != data["borrow_wwid"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            borrow_wwid=oldDevices.borrow_wwid
                    )
                if oldDevices.comments and oldDevices.comments != data["comments"]:
                    HistoryUser.objects.create(
                        device_number=uuid,
                        comments=oldDevices.comments
                    )
            except Exception as e:
                logger.warning("操作日志记录错误，请管理员修复问题")
                logger.error(e)

            Devices.objects.filter(id=uuid).update(**data)
            return JsonResponse({"status": "update success"}, safe=False)
        else:
            Devices.objects.create(**data)
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

