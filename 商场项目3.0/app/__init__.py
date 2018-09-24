from flask import Flask,render_template,request,session,g
from flask_sqlalchemy import SQLAlchemy
from flask_cache import Cache
from config import  config_redis
from config import  SQLConfig

app = Flask(__name__)
app.config.from_object(SQLConfig)
app.config.from_object(config_redis)
db = SQLAlchemy(app)
# cache = Cache(app)

from  app.cust.views import customer
from  app.goods.views import goods
from  app.shopCar.views  import shopCar

app.register_blueprint(customer,url_prefix='/customer')
app.register_blueprint(goods,url_prefix='/goods')
app.register_blueprint(shopCar,url_prefix='/shopCar')

from app import models
from app.cust import views
from app.goods  import views



@app.before_request           #请求前定义全局变量
def berfore_request():
    if 'user_id' in session:       #如果全局user_id在session内（即用户已经登录），就定义全局变量。否则不定义
        g.customer = customer.query.get(session['user_id'])


@app.route('/',methods=['GET','POST'])
# @cache.cached()
def homepage():
    if request.method == 'GET':
        # print(url_to)
        # if url_to == None:
        return render_template('商城首页.html')
        # if url_to == 'login.html':
        #     return render_template('login.html')
#增加点击进入登录和购买页面
    else:
        pass
        # if  request.args ==

@app.route('/<msg>',methods=['GET',])
def homepage_login(msg):
    if request.method == 'GET':
        if msg == 'logined':
           login_msg = '已登录'
           return render_template('商城首页.html',msg=login_msg)

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

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404-1.0.html'),404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


#初始化文件
if __name__=='__main__':
    app.run('',8000,threaded=True)

