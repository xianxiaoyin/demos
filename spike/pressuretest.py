#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 7/17/2020 1:28 PM
# @Author : XianXiaoYin

import httpx
from random import randint
import asyncio

taskList = []


async def Tests(name):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}
    r = httpx.post("http://10.238.0.119/", data={'name': name}, headers=header)
    return r.json()

for i in range(50):
    name = 'name_{}'.format(randint(1, 100))
    t = Tests(name)
    taskList.append(asyncio.ensure_future(t))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(taskList))
for task in taskList:
    print("task result is {}".format(task.result()))