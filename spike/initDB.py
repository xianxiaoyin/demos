
from app import db
from app.models import Product, User

foods = [
    {"name": "香蕉", "desc": "很香很香的香蕉", "price": "5.5", "inventory": 10},
    {"name": "苹果", "desc": "又红又大的苹果", "price": "8.8", "inventory": 10},
    {"name": "芒果", "desc": "热带水果", "price": "9.9", "inventory": 10},
    {"name": "柠檬", "desc": "泡茶专用", "price": "2.1", "inventory": 10},
    {"name": "葡萄", "desc": "自家产的", "price": "1.85", "inventory": 10},
    {"name": "草莓", "desc": "奶油味的", "price": "20.5", "inventory": 10},
    {"name": "大西瓜", "desc": "我的最爱", "price": "1.98", "inventory": 10},
    {"name": "梨", "desc": "清心润肺大鸭梨", "price": "1.1", "inventory": 10},
]
# 初始化一些商品
for food in foods:
    product = Product(**food)
    db.session.add(product)

# 初始化一个用户
users = {"name": "admin"}
user = User(** users)
db.session.add(user)

db.session.commit()


