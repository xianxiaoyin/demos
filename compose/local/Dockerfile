FROM rackspacedot/python37:latest

RUN pip install django openpyxl -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com --proxy=http://child-prc.intel.com:913

RUN mkdir -p /root/devices

COPY "deviceManagement"   "/root/devices/deviceManagement"

WORKDIR /root/devices/deviceManagement

RUN python manage.py migrate

