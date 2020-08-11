from flask import Response, jsonify, request
from app import app, db
from app.models import Product, Order, User

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

    # 检查用户是否已经购买过（每个用户只能购买一次）
    name = request.form.get('name')
    name_id = User.query.filter_by(name=name).first()
    order_name = Order.query.filter_by(user=name_id.id)
    if order_name.count() >0:  
        data["data"] = "该用户已购买，请不要重复购买"
        return jsonify(data)

    # 查询商品信息----检查商品库存
    product = Product.query.get(int(food_id))
    if product.inventory <=0:
        data["data"] = "商品已售馨"
        return jsonify(data)
    product.inventory -=1

    #  更新订单表
    order_dict = {"user": 1, "product": product.id, "state": "已支付"}
    order = Order(**order_dict)
    db.session.add(order)

    db.session.commit()

    return jsonify(data)


    
