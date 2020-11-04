from flask import Response, jsonify, request
from app import app, db
from app.models import Product, Order, User 
from app.redis import Redis



# 首页展示所有商品
@app.route('/')
def index():
    data = {}
    data["msg"] = "success"
    data["data"] =  [i.to_json() for i in Product.query.all()]
    return jsonify(data)

# 展示单个商品
@app.route('/food/<food_id>')
def food(food_id):
    data = {}
    data["msg"] = "success"
    data["data"] = Product.query.get(int(food_id)).to_json()
    return jsonify(data)

# 购买/秒杀商品
@app.route('/shop/<food_id>', methods=["GET", "POST"])
def shop(food_id):
    data = {}
    data["msg"] = "success"


    #  redis
    redis = Redis()
    inventory = int(redis.read("sum"))
    if inventory <= 0:
        data["data"] = "商品已售馨， 秒杀已完成，请等待下次 活动!!!!"
        return jsonify(data), 302

    # 检查用户是否已经购买过（每个用户只能购买一次）
    name = request.form.get('name')
    name_id = User.query.filter_by(name=name).first()
    if name_id:
        order_name = Order.query.filter_by(user=name_id.id)
        if order_name.count() >0:  
            data["data"] = "该用户已购买，请不要重复购买"
            return jsonify(data), 302
    else:
        data["data"] = "用户不存在"
        return jsonify(data), 302

    # redis 中扣除库存
    inventory -=1
    redis.write("sum", inventory)

    #  更新订单表
    product = Product.query.get(int(food_id))
    product.inventory -=1
    order_dict = {"user": name_id.id, "product": product.id, "state": "已支付"}
    order = Order(**order_dict)
    db.session.add(order)

    db.session.commit()
    data["data"] = "恭喜你抢到心爱的商品 ！！！"
    return jsonify(data), 200


    
