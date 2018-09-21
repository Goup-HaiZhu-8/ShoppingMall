from flask import request,Blueprint,session
from flask import render_template,redirect,url_for
from  app import db    #测试用
from app.models import Customer
from app import app  #测试用

customer = Blueprint('customer',__name__)

@customer.route('/login',methods=['GET','POST'])
def login():
     if request.method == 'GET':
         return render_template('login.html',customer='')
     else:
          #加判断,是否是已经注册用户
          #如果已经注册
          user_name = request.form.get('user_name')
          password = request.form.get('password')
          email =  request.form.get('email')
          customer = Customer.query.filter_by(user_name = user_name).first()
          if customer:
              #判断密码和邮箱是否正确
              if customer.password == password and customer.email == email:
                  session['username'] = user_name
                  session['password'] = password
                  session['email'] = email
                  msg = '已经登录'
                  return render_template('商城首页.html',msg = msg)  #测试
              #密码或者邮箱不正确,返回提示信息
              else:
                  err_msg = '密码或者邮箱不正确'
                  return  redirect(url_for('customer.login',err_msg= err_msg))   #注意一定是要为customer.login,因为注册了蓝图

          #如果用户不存在,提示用户进行注册
          else:
              #重组客户端传过来的信息
              customer_msg = {}
              register_msg = '您还没注册,请进行注册'
              return  redirect(url_for('customer.login',
                                       customer=customer_msg,
                                       register= register_msg))



#测试用
if __name__ == '__main__':
    app.run('',7001)