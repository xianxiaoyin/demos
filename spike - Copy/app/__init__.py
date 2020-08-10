#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 7/17/2020 1:28 PM
# @Author : XianXiaoYin

from flask import Flask, request
from flask_restful import Api
from flask_restful import Resource
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

pymysql.install_as_MySQLdb()
app = Flask(__name__)

class Config:
    """配置参数"""
    # 设置连接数据库的URL
    host = "127.0.0.1"
    port = 3306
    user = 'root'
    password = r'love.1993'
    database = 'spike'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://%s:%s@%s:%s/%s' % (user, password, host, port, database)

    # 设置sqlalchemy自动更跟踪数据库
    # SQLALCHEMY_TRACK_MODIFICATIONS = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


redis_client = FlaskRedis()
api = Api(app)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
redis_client.init_app(app)


@app.route("/")
def index():
    return {"msg": "111111"}, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80, debug=True)
