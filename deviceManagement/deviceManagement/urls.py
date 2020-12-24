'''
Author: xianxiaoyin
LastEditors: xianxiaoyin
Descripttion: 
Date: 2020-12-19 12:28:05
LastEditTime: 2020-12-24 22:40:06
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
from django_filters.views import object_filter
from devices.views import devices, deviceResults, deviceFilter, deviceDebug, deviceTest, deviceEdit
 

urlpatterns = [
    path('', devices),
    # path('', object_filter, {'model': devices}),
    path('device/<int:id>/', deviceResults),
    path('devicefilter', deviceFilter),
    path('devicedebug', deviceDebug),
    path('devicetest', deviceTest),
    path('deviceedit', deviceEdit),
    path('admin/', admin.site.urls),
]