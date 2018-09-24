from flask import request,Blueprint
from flask import render_template,redirect,url_for
# from  app import db    #测试用
# from app import app
from sqlalchemy import MetaData,create_engine,Table   #可以直接从models引入
# from sqlalchemy.ext.automap import  automap_base
from sqlalchemy.orm import sessionmaker
from app.models  import Goods

goods = Blueprint('goods',__name__)




@goods.route('/goodlist',methods=['GET',])
def goodlist():
    if request.method == 'GET':
        goods = Goods()                              #实例化Goods类，进行ORM映射
        Session = sessionmaker(bind=goods.engine)    #创建当前会话
        session = Session()

        shop_goods = session.query(goods.apply_table).first()
        print(shop_goods)

        return 'ok'


# if __name__ == '__main__':
#     app.run('',8003)