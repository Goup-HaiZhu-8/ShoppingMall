from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from  app.cust.views import customer
from  app.goods.views import goods
from  app.shopCar.views  import shopCar

app.register_blueprint(customer,url_prefix='/customer')
app.register_blueprint(goods,url_prefix='/goods')
app.register_blueprint(shopCar,url_prefix='/shopCar')

from app import models
from app.cust import views
from app.goods  import views

@app.route('/',methods=['GET','POST'])
def homepage():
    if request.method == 'GET':
       return render_template('商城首页.html')
#增加点击进入登录和购买页面
    else:
        pass
        # if  request.args ==


@app.route('/phonePage',methods=['GET','POST'])
def phonePage():
    if request.method == 'GET':
       return render_template('phonePage.html')
    else:
       #获取前端提交数据
       data = request.json
       img_url = data['img_url']
       money = data['money']
       description = data['description']


       print(data)
       print(img_url)
       return 'ok'


#初始化文件
if __name__=='__main__':
    app.run('',8001,threaded=True)

