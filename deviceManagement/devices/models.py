# coding:utf-8
'''
Author: xianxiaoyin
@,@LastEditors: ,: xianxiaoyin
Descripttion: 数据库模型
Date: 2020-12-19 12:30:13
@,@LastEditTime: ,: 2021-02-04 14:29:18
'''
from datetime import datetime
from django.db import models
from django.db.models.deletion import SET_NULL

class Status(models.Model):
    '''
    设备状态表
    category =  1
    status = 2
    project = 3
    functeam = 4
    location = 5
    '''
    name = models.CharField(verbose_name="status name", max_length=200, unique=True)
    tag = models.CharField(verbose_name="tag", max_length=5)
    update_at = models.DateTimeField(verbose_name="update time", default=datetime.now)
    create_at = models.DateTimeField(verbose_name="create time", auto_now_add=True)

    class Meta:
        db_table = "status"
    def __str__(self):
        return '{}'.format(self.name)

class Devices(models.Model):
    """设备信息表"""
    sn = models.CharField(verbose_name="Serial Number", max_length=50, null=True, blank=True)
    bcode = models.CharField(verbose_name="Barcode", max_length=50, null=True, blank=True)
    category = models.ForeignKey(Status, on_delete=SET_NULL,
    blank=True, null=True, related_name="category")
    status = models.ForeignKey(Status, on_delete=SET_NULL,
     blank=True, null=True, related_name="status")
    project = models.ForeignKey(Status, on_delete=SET_NULL,
     blank=True, null=True, related_name="project")
    functeam = models.ForeignKey(Status, on_delete=SET_NULL,
     blank=True, null=True, related_name="functeam",default="")
    location = models.ForeignKey(Status, on_delete=SET_NULL,
     blank=True, null=True, related_name="location")
    po = models.CharField(verbose_name="PO#", max_length=200, null=True, blank=True)
    actual_user = models.CharField(verbose_name="actual_user", max_length=200, null=True, blank=True)
    borrow_wwid = models.CharField(verbose_name="borrow_wwid", max_length=200, null=True, blank=True)
    po_requestor = models.CharField(verbose_name=" po_requestor",
     max_length=200, null=True, blank=True)
    comments = models.TextField(verbose_name="comments", max_length=500, null=True, blank=True)
    update_at = models.DateTimeField(verbose_name="update time", auto_now=True)
    create_at = models.DateTimeField(verbose_name="create time", auto_now_add=True)

    class Meta:
        db_table = "devices"
        ordering = ["update_at"]

    def __str__(self):
        return "%s" % self.sn


class HistoryUser(models.Model):
    """操作历史记录"""
    device_number = models.IntegerField(verbose_name="devices ID")
    bcode = models.CharField(verbose_name="change username",
    max_length=200, null=True, blank=True)
    category = models.CharField(verbose_name="change category",
     max_length=200, null=True, blank=True)
    status = models.CharField(verbose_name="change status", max_length=200, null=True, blank=True)
    project = models.CharField(verbose_name="change project", max_length=200, null=True, blank=True)
    location = models.CharField(verbose_name="change location", max_length=200,
    null=True, blank=True)
    actual_user = models.CharField(verbose_name="change actual_user",
    max_length=200, null=True, blank=True)
    borrow_wwid = models.CharField(verbose_name="change borrow_wwid",
    max_length=200, null=True, blank=True)
    comments = models.CharField(verbose_name="change comments",
    max_length=200, null=True, blank=True)
    create_at = models.DateTimeField(verbose_name="create time", auto_now_add=True)
    class Meta:
        db_table = "historyuser"
    def __str__(self):
        return "{}".format(self.device_number)
 