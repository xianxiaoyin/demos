# coding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2020-12-19 17:23:25
'''
from django.db import models
from datetime import datetime

# 设备信息表

status = [
    ("u", "In Use"),
    ("d", "Damage"),
    ("s", "In Stock"),
]

projects = [
    ("1", "Purley-R"),
    ("2", "Eagle Stream"),
    ("3", "Whitley-PI"),
    ("4", "Whitley-PV"),
    ("5", "Cedar Island"),
    ("6", "NPX-D"),
    ("7", "NPX-SP"),
    ("8", "DL Boost"),
    ("9", "CLX-AP"),
    ("10", "IPU"),
]

categorys = [
    ("1", "Host"),
    ("2", "Server"),
    ("3", "Switch"),
    ("4", "SF100"),
    ("5", "EM100"),
    ("6", "Control box"),
    ("7", "SF600"),
    ("8", "KVM"),
    ("9", "KVM Dongle"),
    ("10", "ITP"),
    ("11", "LAUTERBACH "),
    ("12", "Loopback"),
    ("13", "Banino Village "),
    ("14", "Power Meter"),
    ("15", "RSC2"),
    ("16", "PDU"),
    ("17", "SSD"),
    ("18", "Network Card"),
    ("19", "DIMM"),
    ("20", "U-Disk"),
    ("21", "HSBP"),
    ("22", "Others"),
]

functeams = [
    ("1", "Pnp"),
    ("2", "Validation"),
    ("3", "Auto"),
    ("4", "Semi-Auto"),
]

locations = [
    ("1", "Lab"),
    ("2", "ISMP "),
    ("3", "Office"),
]





class Devices(models.Model):
    sn = models.CharField(verbose_name="Serial Number", max_length=20)
    bcode =  models.CharField(verbose_name="Barcode", max_length=20, null=True, blank=True)
    gategory = models.CharField(verbose_name="gategory", max_length=6,  choices=categorys)
    status = models.CharField(verbose_name="status", max_length=6, choices=status)
    project =  models.CharField(verbose_name="project", max_length=6, choices=projects)
    functeam =  models.CharField(verbose_name="function team", max_length=6, choices=functeams)
    location = models.CharField(verbose_name="location", max_length=6, choices=locations)
    po = models.CharField(verbose_name="PO#", max_length=20)
    rowner = models.CharField(verbose_name="requestor(Owner)", max_length=20)
    wwid = models.CharField(verbose_name="BorrowWWID", max_length=10)
    comments = models.TextField(verbose_name="comments")
    update_at = models.DateTimeField(verbose_name="update time", default=datetime.now)
    create_at = models.DateTimeField(verbose_name="create time", auto_now_add=True) 
    class  Meta:
        db_table = "devices"
        ordering = ["update_at"]
    def __str__(self):
        return "%s" %self.sn
    