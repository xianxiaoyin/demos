#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 7/17/2020 1:28 PM
# @Author : XianXiaoYin

from flask import Flask, request
from flask_restful import Api
from flask_restful import Resource
from flask_redis import FlaskRedis
from flask_cors import CORS

redis_client = FlaskRedis()
app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True)  # 支持跨域
redis_client.init_app(app)


class Spike(Resource):
    @staticmethod
    def get():
        data = {"msg": 'get get get'}
        return data, 200

    @staticmethod
    def post():
        """
        保存index  name如果超过到达10个就返回提示信息
        """
        name = request.form.get("name")
        total = redis_client.scard('spike')
        print(total)
        if total > 10-1:
            return {"msg": '你来晚了，已经抢没了！'}, 302
        if name:
            redis_client.sadd('spike', name)
        print(total)
        data = {'msg': "当前秒杀用户：{}".format(name)}
        return data, 201


api.add_resource(Spike, '/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
