# coding:utf-8
'''
需要手动创建数据库，否则会提示OperationalError 错误
'''

from spike.app import db
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
    create = db.Column(db.DateTime(), default=datetime.datetime.now())


class Order(db.Model):
    # 定义表名
    __tablename__ = 'spike_order'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey("spike_users.id"))
    product = db.relationship("User", backref="spike_product")
    state = db.Column(db.String(6))
    create = db.Column(db.DateTime(), default=datetime.datetime.now())


class Cart(db.Model):
    # 定义表名
    __tablename__ = 'spike_cart'
    # 定义字段
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey("spike_users.id"))
    product = db.Column(db.Integer, db.ForeignKey("spike_product.id"))
    create = db.Column(db.DateTime(), default=datetime.datetime.now())





if __name__ == '__main__':
    # 删除所有表
    db.drop_all()

    # 创建所有表
    db.create_all()

    # 初始化数据
    foods = [
        {"name": "香蕉", "desc": "很香很香的香蕉", "price": "5.5"},
        {"name": "苹果", "desc": "又红又大的苹果", "price": "8.8"},
        {"name": "芒果", "desc": "热带水果", "price": "9.9"},
        {"name": "柠檬", "desc": "泡茶专用", "price": "2.1"},
        {"name": "葡萄", "desc": "自家产的", "price": "1.85"},
        {"name": "草莓", "desc": "奶油味的", "price": "20.5"},
        {"name": "大西瓜", "desc": "我的最爱", "price": "1.98"},
        {"name": "梨", "desc": "清心润肺大鸭梨", "price": "1.1"},
    ]
    for food in foods:
        product = Product(**food)
        db.session.add(product)
    db.session.commit()
