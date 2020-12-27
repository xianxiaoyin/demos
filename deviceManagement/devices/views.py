# encoding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2020-12-27 21:04:59
'''
from django.shortcuts import render
from django.http import HttpResponse
from .models  import Devices, categorys, status, projects, functeams, locations
from django.db.models import Q
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

    # 对categorys 过滤
    categorys_index = {v:k for k,v in dict(categorys).items()}.get(filterdata)
    if not categorys_index:
        categorys_index = filterdata

    # 对status, 过滤
    status_index = {v:k for k,v in dict(status).items()}.get(filterdata)
    if not status_index:
        status_index = filterdata

    # 对 projects, 过滤
    projects_index = {v:k for k,v in dict(projects).items()}.get(filterdata)
    if not projects_index:
        projects_index = filterdata

    # 对  functeams, 过滤
    functeams_index = {v:k for k,v in dict(functeams).items()}.get(filterdata)
    if not functeams_index:
        functeams_index = filterdata

     # 对  locations 过滤
    locations_index = {v:k for k,v in dict(locations).items()}.get(filterdata)
    if not locations_index:
        locations_index = filterdata

    print(filterdata)
    print(projects_index)
    if filterdata:
        devices = Devices.objects.filter(Q(sn__contains=filterdata)|
                                         Q(bcode__contains=filterdata)|
                                         Q(category__contains=categorys_index)|
                                         Q(status__contains=status_index) |
                                         Q(project__contains=projects_index) |
                                         Q(functeam__contains=functeams_index) | 
                                         Q(location__contains=locations_index) )
    else:
         devices = Devices.objects.all()
    return render(request, "index.html", {"devices": devices})








def deviceDebug(request):
    data = [{ "id": 1, "name": "Item 1", "price": "￥1" },
    { "id": 2, "name": "Item 2", "price": "￥2" },
    { "id": 3, "name": "Item 3", "price": "￥3" }]
    return  HttpResponse(json.dumps({'data': data}))

def deviceTest(request):
    from utils.exportexcel import saveData
    saveData(r"D:\learn\demos\deviceManagement\utils\1.xlsx")
    return render(request, "test.html")


