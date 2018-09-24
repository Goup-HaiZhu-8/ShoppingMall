from flask import request,Blueprint,session,jsonify
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
          username = request.form.get('username')
          password = request.form.get('password')
          # email =  request.form.get('email')
          customer = Customer.query.filter_by(user_name = username).first()
          if customer:
              print(customer)
              print(customer.password)
              #判断密码和邮箱是否正确
              if customer.password == password :
                  # session['username'] = username
                  # session['password'] = password
                  # session['email'] = email
                  msg = 'logined'
                  return redirect(url_for('homepage_login',msg = msg))
              #密码或者邮箱不正确,返回提示信息
              else:
                  err_msg = 'psw_error'
                  return  redirect(url_for('customer.login_err',err_msg= err_msg))   #注意一定是要为customer.login,因为注册了蓝图

          #如果用户不存在,提示用户进行注册
          else:
              #重组客户端传过来的信息
              register_msg = 'no_register'
              return  redirect(url_for('customer.login_err',err_msg=register_msg))  #参数键名必须与接收的路由参数名相同


@customer.route('/<err_msg>',methods=['GET',])
def login_err(err_msg):
    if request.method == 'GET':
        if err_msg == 'psw_error':
            err = u'您的密码输入错误'             #注意：传递的一定要是unicode码
            return render_template('login.html',err=err)
        elif err_msg == 'no_register':
            err = u'您还没注册'
            return render_template('login.html',err=err)


#登录过程账号提示没有注册时，需要用户点击链接进行注册
#功能实现：

@customer.route('/register',methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html',customer='')
    #注册用户，调用数据库
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('passowrd2')
        email = request.form.get('email')
        nickname = request.form.get('nickname')

        customer = Customer.query.filter_by(user_name=username).first()

        #用户名已经存在
        if  username == customer.user_name:
            reg_err = 'name_exit'
            return redirect(url_for('register_err',reg_err=reg_err))
        #两次输入的密码不相同
        elif password != password2:
            reg_err = 'pwd_err'
            return redirect(url_for('register_err',reg_err=reg_err))
        #email地址已存在




        #成功注册
        msg = u'已登录'
        return render_template('商城首页.html',msg = msg)


#功能没完整
@customer.route('<reg_err>',methods=['GET',])
def  register_err(reg_err):
    if request.method == 'GET':
         if  reg_err == 'name_exit':
             msg = u'您注册的用户名已存在'
             return render_template('register.html',msg = msg)
         return render_template('register.html')




#测试用
# if __name__ == '__main__':
#     app.run('',7001)