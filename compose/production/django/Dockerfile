FROM rackspacedot/python37:latest

RUN pip install django openpyxl gunicorn xlrd -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com --proxy=http://child-prc.intel.com:913

RUN mkdir -p /root/devices

COPY deviceManagement   /root/devices/deviceManagement

WORKDIR /root/devices/deviceManagement

COPY ./compose/production/django/start.sh  /root/devices/deviceManagement/start.sh

RUN chmod +x /root/devices/deviceManagement/start.sh
