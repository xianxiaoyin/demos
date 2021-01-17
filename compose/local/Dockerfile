FROM rackspacedot/python37:latest

RUN pip install django openpyxl  -i http://mirrors.aliyun.com/pypi/simple --trusted-host mirrors.aliyun.com

RUN mkdir -p /root/devices

COPY deviceManagement   /root/devices/deviceManagement

WORKDIR /root/devices/deviceManagement

COPY ./compose/local/start.sh  /root/devices/deviceManagement/start.sh

RUN chmod +x /root/devices/deviceManagement/start.sh
