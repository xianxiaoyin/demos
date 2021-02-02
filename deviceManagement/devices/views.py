# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 逻辑处理
Date: 2020-12-19 12:30:13
LastEditTime: 2021-02-02 15:23:38
'''
import json
import copy
import datetime
import logging
from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from utils.exportexcel import saveData, initStatus
from .models import Devices, Status, HistoryUser

logger = logging.getLogger(__name__)

def index(request):
    '''首页'''
    filename = request.FILES.get("excelfile")
    if filename:
        logger.info("复制2份内存数据，给2个脚本用")
        file_name_data_init = copy.deepcopy(filename)
        file_name_data_save = copy.deepcopy(filename)
        logger.info("开始初始化数据库······")
        initStatus(file_name_data_init)
        logger.info("初始化数据库结束······")
        logger.info("开始导入数据······")
        saveData(file_name_data_save)
        logger.info("导入数据结束······")
        del file_name_data_init
        del file_name_data_save
        logger.info("删除复制的数据")
        return render(request, "index.html", {"msg": "file upload successful"})
    return render(request, "index.html")


def device_edit(request):
    '''更新设别信息'''
    if request.method == 'POST':
        post = request.POST
        data = json.loads(json.dumps(post))
        try:
            del data["0"]
        except KeyError as keyerr:
            logger.error(keyerr)
            logger.warning("删除临时数据错误，忽略此信息~")
        data["update_at"] = datetime.datetime.now()
        oldid = data.get("id", "")
        # uuid = data.pop("id")
        # 如果更新了actual_user字段，把更新记录存储到HistoryUser表中
        if oldid:
            uuid = data.pop("id")
            old_devices= Devices.objects.get(id=uuid)
            try:
                if old_devices.actual_user and old_devices.actual_user != data["actual_user"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            actual_user=old_devices.actual_user
                    )
                if old_devices.bcode and old_devices.bcode != data["bcode"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            bcode=old_devices.bcode
                    )
                if old_devices.category and old_devices.category != data["category_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            category=old_devices.category.name)
                if old_devices.status and old_devices.status != data["status_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            status=old_devices.status.name
                    )
                if old_devices.project and old_devices.project != data["project_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            project=old_devices.project.name
                    )
                if old_devices.location and old_devices.location != data["location_id"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            location=old_devices.location.name
                    )

                if old_devices.borrow_wwid and old_devices.borrow_wwid != data["borrow_wwid"]:
                    HistoryUser.objects.create(
                            device_number=uuid,
                            borrow_wwid=old_devices.borrow_wwid
                    )
                if old_devices.comments and old_devices.comments != data["comments"]:
                    HistoryUser.objects.create(
                        device_number=uuid,
                        comments=old_devices.comments
                    )
            except Exception as error:
                logger.warning("操作日志记录错误，请管理员修复问题")
                logger.error(error)

            Devices.objects.filter(id=uuid).update(**data)
            return JsonResponse({"status": "update success"}, safe=False)
        Devices.objects.create(**data)
        return JsonResponse({"status": "create success"}, safe=False)
    return JsonResponse({"status": "Wrong way to request"}, safe=False)


def status(request):
    '''获取状态'''
    tag = request.GET.get("tag")
    data = Status.objects.filter(tag=tag).values()
    data = list(data)
    return JsonResponse(data, safe=False)


def devices(request):
    '''获取所有信息'''
    inputsearch = request.GET.get("inputsearch")
    if inputsearch:
        device_all = Devices.objects.filter(Q(sn__contains=inputsearch) |
                                         Q(bcode__contains=inputsearch)|
                                         Q(comments__contains=inputsearch
                                         )).order_by("-update_at").values()
    else:
        device_all = Devices.objects.all().order_by("-update_at").values()
    device_all = list(device_all)
    return JsonResponse(device_all, safe=False)



def history_user(request, number):
    '''获取当前设备的借用记录'''
    if number:
        data = HistoryUser.objects.filter(device_number=number).order_by("-create_at")
    else:
        data = {}
    return render(request, "history.html", {"data": data})


def delete(request):
    '''删除数据'''
    if request.method == 'DELETE':
        ids = json.loads(request.body.decode("utf-8")).get("ids", "")
        for i in ids:
            HistoryUser.objects.filter(device_number=i).delete()
            Devices.objects.filter(id=i).delete()
        return JsonResponse({"msg": "successful"}, safe=False)
    return JsonResponse({"status": "Wrong way to request"}, safe=False)
