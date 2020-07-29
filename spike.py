#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 7/17/2020 1:28 PM
# @Author : xianxiaoyin

from flask import Flask, request
from flask_restful import Api
from flask_restful import Resource, reqparse
from flask_redis import FlaskRedis


redis_client = FlaskRedis()
app = Flask(__name__)
api = Api(app)
redis_client.init_app(app)

class Spike(Resource):
    def get(self):
        data = {"msg": 'get get get'}
        print(redis_client.get(111))
        return data, 200





    def post(self):
        """
        保存index  name如果超过到达10个就返回提示信息
        """
        name = request.form.get("name")
        total = redis_client.scard('spike')
        if total > 10:
            return {"msg": '你来晚了，已经抢没了！'}, 302
        if name:
            redis_client.sadd('spike', name)

        data = {'msg': "当前秒杀用户：{}".format(name)}
        return data, 201





api.add_resource(Spike, '/')

 
if __name__ == '__main__':
    app.run(debug=False)
