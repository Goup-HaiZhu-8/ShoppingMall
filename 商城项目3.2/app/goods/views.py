from flask import request,Blueprint,session
from flask import render_template,redirect,url_for
from  website_flask.app import db
# from sqlalchemy import MetaData,create_engine,Table   #可以直接从models引入
# from sqlalchemy.ext.automap import  automap_base
# from sqlalchemy.orm import sessionmaker
from website_flask.app.models  import Goods,Shoppingcar,Customer


goods = Blueprint('goods',__name__)


@goods.route('/goodlist', methods=['GET','POST'])
def goodlist():
    if request.method == 'GET':
        # goods = Goods()  # 实例化Goods类，进行ORM映射
        # Session = sessionmaker(bind=goods.engine)  # 创建当前会话
        # session = Session()
        # shop_goods = session.query(goods.apply_table).all()

        goods = Goods.query.all()
        return render_template('phonePage.html',goods=goods)
    else:
        # 获取前端提交数据
        data = request.json
        # img_url = data['img_url']
        # money = data['money']
        description = data['description']
        gid = Goods.query.filter_by(gname=description).first().gid
        customer = session.get('username')
        shop_customer = Customer.query.filter_by(user_name=customer).first()
        uid = shop_customer.id

        shopcar_cus = Shoppingcar.query.filter_by(uid=uid)
        #如果该用户有购买记录
        if shopcar_cus:
            shopcar = Shoppingcar.query.filter_by(uid=uid,goods_id=gid).first()
            #如果有购买同类商品记录
            if shopcar:
                  shopcar_amount = shopcar.amount
                  print(shopcar_amount)
                  shopcar_amount += 1
                  Shoppingcar.query.filter_by(goods_id=gid).update({
                      'amount': shopcar_amount}
                  )
                  db.session.commit()
            else:
                good_one = Shoppingcar()
                good_one.uid = uid
                good_one.amount = 1
                good_one.goods_id = gid
                id = Shoppingcar.query.order_by(
                    Shoppingcar.id.desc()
                ).first().id
                good_one.id = id+1

                db.session.add(good_one)
                db.session.commit()
        #如果该用户没有购买记录
        else:
            good_one = Shoppingcar()
            good_one.uid = uid
            good_one.amount = 1
            good_one.goods_id = gid
            id = Shoppingcar.query.order_by(
                Shoppingcar.id.desc()
            ).first().id
            good_one.id = id + 1

            db.session.add(good_one)
            db.session.commit()

        return 'ok'


