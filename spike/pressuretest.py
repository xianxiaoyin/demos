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
    r = httpx.post("http://192.168.1.11:5000/shop/1", data={'name': name}, headers=header)
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
class intace{
    Object obj;
    Object get(){
        if(obj ==null){
            syncied{
                if(obj ==null){
                    return new Object();
                }
            }
        }
        return obj;
    }
}
if()


1.商品库存10   存入  redis

2. 判断库存是否充足 ，不充足直接返回库存不足提示，充足：进行资源加锁

3. redis 加锁（死循环+自动失效）
4. redis枷锁成功
5. 从redis在获取一次数据(枷锁成功后，其他线程不能更改库存)
6. 判断库存是否充足 ，不充足直接返回库存不足提示，充足：进行数据库持久化
7. redis库存-1
8.解锁


'''
