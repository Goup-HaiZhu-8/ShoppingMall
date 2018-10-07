from flask import request,Blueprint,session,jsonify
from flask import render_template,redirect,url_for
from website_flask.app.models import Customer
from website_flask.app import app  #测试用
from  website_flask.app import db    #测试用

customer = Blueprint('customer',__name__)

@customer.route('/login',methods=['GET','POST'])
def login():
     if request.method == 'GET':
         return render_template('login.html',customer='')
     else:
          username = request.form.get('username')
          password = request.form.get('password')
          #加判断，是否已经登录
          if session.get('username'):
              err_msg = 'logined'
              return redirect(url_for('customer.login_err', err_msg=err_msg))
          else:
              # 加判断,是否是已经注册用户
              customer = Customer.query.filter_by(user_name = username).first()
              if customer:
                  #判断密码和邮箱是否正确
                  if customer.password == password :
                      session['username'] = username
                      print(session['username'])
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
            err = u'您还没注册,请前往注册'
            return render_template('login.html',err=err)
        elif err_msg == 'logined':
            err = u'您已经登录了'
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
        password2 = request.form.get('password2')
        email = request.form.get('email')
        nickname = request.form.get('nickname')

        customer = Customer.query.filter_by(user_name=username).first()

        #如果用户不存在
        if not customer:
            #检查两次输入密码
            if  password != password2:
                err_msg = 'pwd_err'
                return redirect(url_for('customer.register_err',register='register',reg_err=err_msg))
            elif  Customer.query.filter_by(email=email).first():
                err_msg = 'email_err'
                return redirect(url_for('customer.register_err',register='register', reg_err=err_msg))
            elif Customer.query.filter_by(nickname=nickname).first():
                err_msg = 'nickname_err'
                return redirect(url_for('customer.register_err',register='register', reg_err=err_msg))
            else:
                user = Customer(user_name=username,password=password,email=email,nickname=nickname)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('customer.login'))
        #用户名已经存在
        else:
            err_msg = 'name_exit'
            return redirect(url_for('customer.register_err',register='register',reg_err=err_msg))





#功能没完整
@customer.route('/<register>/<reg_err>',methods=['GET','POST'])
def register_err(register,reg_err):
    if request.method == 'GET':
         if reg_err == 'name_exit':
             msg = u'您注册的用户名已存在'
             return render_template('register.html',msg=msg)
         elif reg_err == 'pwd_err':
             msg = u'您两次输入的密码不相同'
             return render_template('register.html',msg=msg)
         elif reg_err == 'email_err':
             msg = u'您输入的邮箱已注册'
             return render_template('register.html',msg=msg)
         elif reg_err == 'nickname_err':
             msg = u'您输入的昵称已注册'
             return render_template('register.html',msg=msg)

         else:
             return render_template('register.html')




#测试用
# if __name__ == '__main__':
#     app.run('',7001)