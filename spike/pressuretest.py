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
    r = httpx.post("http://127.0.0.1:5000/shop/1", data={'name': name}, headers=header)
    return r.text

for i in range(500):
    name = 'admin{}'.format(randint(1, 50))
    t = Tests(name)
    taskList.append(asyncio.ensure_future(t))

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(taskList))
for task in taskList:
    print("task result is {}".format(task.result()))







'''
1.商品库存   存入  redis

2. 判断库存是否充足 

3.



'''
