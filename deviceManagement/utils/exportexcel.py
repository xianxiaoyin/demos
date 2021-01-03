'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-27 17:45:18
LastEditTime: 2020-12-27 21:32:39
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
                Status.objects.update_or_create(name=line[2], tag="1", update_at=datetime.now(), create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        elif line[3]:
            try:
                Status.objects.update_or_create(name=line[3], tag="2", update_at=datetime.now(), create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        elif line[7]:
            try:
                Status.objects.update_or_create(name=line[7], tag="3", update_at=datetime.now(), create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        elif line[9]:
            try:
                Status.objects.update_or_create(name=line[9], tag="4", update_at=datetime.now(), create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)
        elif line[10]:
            try:
                Status.objects.update_or_create(name=line[10], tag="5", update_at=datetime.now(), create_at=datetime.now())
            except Exception as e:
                print(e)
                print(line)

def saveData(filename):
    obj = []
    for line in readExcel(filename)[1:]:
        if line[3]:
            # obj.append(Devices(sn=line[1], bcode=line[2], category=getIndex(categorys, line[3]),
            #             status=getIndex(status, line[4]), project=getIndex(projects, line[5]),
            #             functeam=getIndex(functeams, line[6]),location=getIndex(locations, line[7]),
            #             po=line[8], rowner=line[9],wwid=line[10],
            #             comments=line[12] )) 
            # Devices.objects.bulk_create(obj)
            try:
                Devices.objects.get_or_create(sn=line[0], bcode=line[1], category=getIndex(categorys, line[2]),
                                              status=getIndex(status, line[3]), project=getIndex(projects, line[9]),
                                              functeam=" ", po_requestor=line[11],
                                              location=getIndex(locations, line[7]),
                                              po=line[10], actual_user=line[4], borrow_wwid=line[5],
                                              comments=line[8], update_at=datetime.now(), create_at=datetime.now())
            except Exception as e:
                print(getIndex(categorys, line[3]))
                print(e)
                print(line)


if __name__ == "__main__":
    initStatus("1.xlsx ")
    # saveData("1.xlsx ")
