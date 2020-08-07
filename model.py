# coding:utf-8
'''
需要手动创建数据库，否则会提示OperationalError 错误
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
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
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 查询时会显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = True

    # 禁止自动提交数据处理
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = False


# 读取配置
app.config.from_object(Config)

# 创建数据库sqlalchemy工具对象
db = SQLAlchemy(app)


class User(db.Model):
    # 定义表名
    __tablename__ = 'spike_users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True)
    pswd = db.Column(db.String(64))
    phone = db.Column(db.String(12), unique=True)
    create = db.Column(db.DateTime())

class Product(db.Model):
    # 定义表名
    __tablename__ = 'spike_product'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    sn = db.Column(db.String(64), unique=True)
    address = db.Column(db.String(64))
    image = db.Column(db.String(12), unique=True)
    desc = db.Column(db.Text(100), unique=True)
    price = db.Column(db.String(12), unique=True)
    create = db.Column(db.DateTime())

class Order(db.Model):
    # 定义表名
    __tablename__ = 'spike_order'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    sn = db.Column(db.String(64), unique=True)
    price = db.Column(db.String(12), unique=True)
    create = db.Column(db.DateTime())
    state = db.Column(db.String(6), unique=True)

class Cart(db.Model):
    # 定义表名
    __tablename__ = 'spike_cart'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey("users.id"))
    product = db.relationship("User",backref="product")
    create = db.Column(db.DateTime())

if __name__ == '__main__':
    # 删除所有表
    db.drop_all()

    # 创建所有表
    db.create_all()
