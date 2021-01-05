# coding:utf-8
'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:30:13
LastEditTime: 2021-01-05 15:44:44
'''
from django.db import models
from datetime import datetime
from django.db.models.deletion import SET_NULL



'''
category =  1
status = 2
project = 3
functeam = 4
location = 5
'''
# 状态

class Status(models.Model):
    name = models.CharField(verbose_name="status name", max_length=20)
    tag = models.CharField(verbose_name="tag", max_length=5)
    update_at = models.DateTimeField(verbose_name="update time", default=datetime.now)
    create_at = models.DateTimeField(verbose_name="create time", auto_now_add=True)

    class Meta:
        db_table = "status"
    def __str__(self):
        return self.name

# 设备信息表

class Devices(models.Model):
    sn = models.CharField(verbose_name="Serial Number", max_length=20, null=True, blank=True)
    bcode = models.CharField(verbose_name="Barcode", max_length=20, null=True, blank=True)
    category = models.ForeignKey(Status, on_delete=SET_NULL, blank=True, null=True, related_name="category")
    status = models.ForeignKey(Status, on_delete=SET_NULL, blank=True, null=True, related_name="status")
    project = models.ForeignKey(Status, on_delete=SET_NULL, blank=True, null=True, related_name="project")
    functeam = models.ForeignKey(Status, on_delete=SET_NULL, blank=True, null=True, related_name="functeam")
    location = models.ForeignKey(Status, on_delete=SET_NULL, blank=True, null=True, related_name="location")
    po = models.CharField(verbose_name="PO#", max_length=20, null=True, blank=True)
    actual_user = models.CharField(verbose_name="actual_user", max_length=20, null=True, blank=True)
    borrow_wwid = models.CharField(verbose_name="borrow_wwid", max_length=20, null=True, blank=True)
    po_requestor = models.CharField(verbose_name=" po_requestor", max_length=20, null=True, blank=True)
    comments = models.TextField(verbose_name="comments", null=True, blank=True)
    update_at = models.DateTimeField(verbose_name="update time", default=datetime.now)
    create_at = models.DateTimeField(verbose_name="create time", auto_now_add=True)

    class Meta:
        db_table = "devices"
        ordering = ["update_at"]

    def __str__(self):
        return "%s" % self.sn
