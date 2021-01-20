'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-27 17:45:18
LastEditTime: 2021-01-20 10:54:43
'''

import openpyxl
from devices.models import Devices, Status
from datetime import datetime


def getIndex(modes_list, filterdata):
    return {v: k for k, v in dict(modes_list).items()}.get(filterdata)


def readExcel(filename="1.xlsx"):
    data = []
    workbook = openpyxl.load_workbook(filename)
    ws = workbook.active
    for row in ws.rows:
        tmp_list = []
        for cel in row:
            tmp_list.append(cel.value)
        data.append(tmp_list)
    return data


def initStatus(filename):
    obj = []
    for line in readExcel(filename)[1:]:
        if line[2]:
            try:
                Status.objects.update_or_create(name=line[2], tag="1", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        if line[3]:
            try:
                Status.objects.update_or_create(name=line[3], tag="2", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        if line[7]:
            try:
                Status.objects.update_or_create(name=line[7], tag="3", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        if line[9]:
            try:
                Status.objects.update_or_create(name=line[9], tag="4", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        if line[10]:
            try:
                Status.objects.update_or_create(name=line[10], tag="5", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)


def obj_get(obj, name, tag):
    try:
        return obj.objects.get(name=name, tag=tag)
    except Exception as e:
        print("not found")
        print("Error data :  {} --->>> {}".format(name, tag))



def saveData(filename):
    for line in readExcel(filename)[1:]:
        if str(line[0]).strip().lower() == "others":
            Devices.objects.create(sn=line[0], bcode=line[1], category=obj_get(Status, line[2], 1),
                                    status=obj_get(Status, line[3], 2), project=obj_get(Status, line[9], 4),
                                    po_requestor=line[11],
                                    location=obj_get(Status, line[7], 3),
                                    po=line[10], actual_user=line[4], borrow_wwid=line[5],
                                    comments=line[8], update_at=datetime.now(), create_at=datetime.now())
        else:
            data = Devices.objects.filter(sn=line[0])
            if data:
                print("************Data exists***************")
                print(line)
            else:
                Devices.objects.create(sn=line[0], bcode=line[1], category=obj_get(Status, line[2], 1),
                                status=obj_get(Status, line[3], 2), project=obj_get(Status, line[9], 4),
                                po_requestor=line[11],
                                location=obj_get(Status, line[7], 3),
                                po=line[10], actual_user=line[4], borrow_wwid=line[5],
                                comments=line[8], update_at=datetime.now(), create_at=datetime.now())

if __name__ == "__main__":
    initStatus("1.xlsx ")
    # saveData("1.xlsx ")
