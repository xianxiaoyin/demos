# coding:utf-8
'''
需要手动创建数据库，否则会提示OperationalError 错误
'''

from app import db
import datetime


class User(db.Model):
    # 定义表名
    __tablename__ = 'spike_users'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    create = db.Column(db.DateTime(), default=datetime.datetime.now())


class Product(db.Model):
    # 定义表名
    __tablename__ = 'spike_product'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), unique=True, index=True)
    desc = db.Column(db.Text(100), unique=True)
    price = db.Column(db.String(12), unique=True)
    inventory = db.Column(db.Integer, default=0)
    create = db.Column(db.DateTime(), default=datetime.datetime.now())

    def to_json(self):
            return {
                'id': self.id,
                'username': self.name,
                'desc': self.desc,
                'price': self.price,
                'inventory': self.inventory,
                'create': self.create,
            }

class Order(db.Model):
    # 定义表名
    __tablename__ = 'spike_order'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer)
    product = db.Column(db.Integer)
    state = db.Column(db.String(6))
    create = db.Column(db.DateTime(), default=datetime.datetime.now())



