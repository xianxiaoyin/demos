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
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import json
import datetime

def Index(request):
    filename = request.FILES.get("excelfile")
    print("---->>> {}".format(filename))
    if filename:
        from utils.exportexcel import saveData, initStatus
        # initStatus(filename)
        saveData(filename)
        return render(request, "testtable.html", {"msg": "file upload successful"})
    else:
        # return render(request, "testtable.html", {"msg": "file upload error"})
        return render(request, "testtable.html")


#  更新设别信息
def deviceEdit(request):
    if request.method == 'POST':
        data = request.POST
        a = json.loads(json.dumps(data))
        a["update_at"] = datetime.datetime.now()
        print(a)
        uuid = a.pop("id")
        Devices.objects.filter(id=uuid).update(**a)
        return JsonResponse({"status": "success"}, safe=False)


# 搜索页面
def deviceFilter(request):
    filterdata = request.GET.get("filterdata")

    # # 对categorys 过滤
    # categorys_index = {v: k for k, v in dict(categorys).items()}.get(filterdata)
    # if not categorys_index:
    #     categorys_index = filterdata
    #
    # # 对status, 过滤
    # status_index = {v: k for k, v in dict(status).items()}.get(filterdata)
    # if not status_index:
    #     status_index = filterdata
    #
    # # 对 projects, 过滤
    # projects_index = {v: k for k, v in dict(projects).items()}.get(filterdata)
    # if not projects_index:
    #     projects_index = filterdata
    #
    # # 对  functeams, 过滤
    # functeams_index = {v: k for k, v in dict(functeams).items()}.get(filterdata)
    # if not functeams_index:
    #     functeams_index = filterdata
    #
    # # 对  locations 过滤
    # locations_index = {v: k for k, v in dict(locations).items()}.get(filterdata)
    # if not locations_index:
    #     locations_index = filterdata

    if filterdata:
        devices = Devices.objects.filter(Q(sn__contains=filterdata) |
                                         Q(bcode__contains=filterdata))
        # |
        # Q(category__contains=categorys_index) |
        # Q(status__contains=status_index) |
        # Q(project__contains=projects_index) |
        # Q(functeam__contains=functeams_index) |
        # Q(location__contains=locations_index))
    else:
        devices = Devices.objects.all()

    paginator = Paginator(devices, 20)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request, "index.html", {"devices": contacts})


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


def devicesAll(request):
    print(request.GET.get("searchString_id"))
    devices = Devices.objects.all().values()
    devices = list(devices)
    return JsonResponse(devices, safe=False)