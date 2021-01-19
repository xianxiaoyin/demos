'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:28:05
LastEditTime: 2021-01-19 16:06:20
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
from devices.views import deviceEdit, status, devices, Index, historyuser, deletes


urlpatterns = [
    path('', Index),
    path('status', status),
    path('devices', devices),
    path('edit', deviceEdit),
    path('deletes', deletes),
    path('history/<int:number>', historyuser),
    
    path('admin/', admin.site.urls),
]
