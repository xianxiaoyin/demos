'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:28:05
LastEditTime: 2020-12-28 15:23:35
'''
"""deviceManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from devices.views import deviceFilter, uploadExcel, deviceEdit, status, devicesAll


urlpatterns = [
    path('', deviceFilter),
    path('upload', uploadExcel),
    path('test', deviceEdit),
    path('status', status),
    path('all', devicesAll),
    path('admin/', admin.site.urls),
]
