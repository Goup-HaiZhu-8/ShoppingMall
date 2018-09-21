from flask import request,Blueprint
from flask import render_template,redirect,url_for
# from  app import db
from app.models import Goods
from app import app
from sqlalchemy import MetaData,create_engine,Table
from sqlalchemy.ext.automap import  automap_base
from sqlalchemy.orm import sessionmaker

goods = Blueprint('goods',__name__)




@goods.route('/goodlist',methods=['GET',])
def goodlist():
    if request.method == 'GET':
        uri = 'mysql+pymysql://root:123456@localhost:3306/HUAWEI'
        engine = create_engine(uri, echo=False)  #创建引擎

        metadata = MetaData(engine)

        apply_info = Table('Goods', metadata, autoload=True)
        keys = apply_info.columns.keys()

        Session = sessionmaker(bind=engine)

        session = Session()

        goods = session.query(apply_info).all()
        print(goods[1])

        return render_template('phonePage.html',goods = goods)


if __name__ == '__main__':
    app.run('',8000)