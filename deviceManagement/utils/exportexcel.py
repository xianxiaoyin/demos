'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 导入数据
Date: 2020-12-27 17:45:18
LastEditTime: 2021-02-01 16:41:49
'''
import xlrd
import openpyxl
from devices.models import Devices, Status
from datetime import datetime
import logging
logger = logging.getLogger(__name__)


def getIndex(modes_list, filterdata):
    return {v: k for k, v in dict(modes_list).items()}.get(filterdata)


def readExcel(filename=None):
    print(filename)
    print(filename.name)
    print(type(filename))
    print(type(filename.name))
    print(dir(filename))
    data = []
    if str(filename.name).endswith("xlsx"):
        workbook = openpyxl.load_workbook(filename)
        ws = workbook.active
        for row in ws.rows:
            tmp_list = []
            for cel in row:
                tmp_list.append(cel.value)
            data.append(tmp_list)
    elif str(filename.name).endswith("xls"):
        workbook = xlrd.open_workbook(filename)
        wx = workbook.sheet_by_index(0)
        for rx in range(wx.nrows):
            tmp_list = []
            for cl in wx.row(rx):
                tmp_list.append(cl.value)
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
                logger.warning(e)
        if line[3]:
            try:
                Status.objects.update_or_create(name=line[3], tag="2", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                logger.warning(e)
        if line[7]:
            try:
                Status.objects.update_or_create(name=line[7], tag="3", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                logger.warning(e)

        if line[9]:
            try:
                Status.objects.update_or_create(name=line[9], tag="4", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                logger.warning(e)

        if line[10]:
            try:
                Status.objects.update_or_create(name=line[10], tag="5", update_at=datetime.now(),
                                                create_at=datetime.now())
            except Exception as e:
                 logger.warning(e)


def obj_get(obj, name, tag):
    try:
        return obj.objects.get(name=name, tag=tag)
    except Exception as e:
        logger.warning(e)



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
                logger.warning("************Data exists***************")
                logger.warning(line)
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
