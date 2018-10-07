from flask import render_template,request,session,g
from website_flask.app import app
from  website_flask.app.cust.views import customer


@app.before_request           #请求前定义全局变量
def berfore_request():
    if 'user_id' in session:       #如果全局user_id在session内（即用户已经登录），就定义全局变量。否则不定义
        g.customer = customer.query.get(session['user_id'])


@app.route('/',methods=['GET','POST'])
# @cache.cached(timeout=600)
def homepage():
    if request.method == 'GET':
        if session.get('username'):
            msg = u'已登录'
            return render_template('商城首页.html',msg=msg)
        else:
            return render_template('商城首页.html')
#增加点击进入登录和购买页面
    # else:
    #     pass
    #     # if  request.args ==


@app.route('/<msg>',methods=['GET'])
def homepage_login(msg=None):
    if request.method == 'GET':
        if not msg:
           return  render_template('商城首页.html')
        if msg == 'logined':
           login_msg = u'已登录'
           return render_template('商城首页.html',msg=login_msg)
        elif msg == 'logout':
            session.clear()
            return render_template('商城首页.html')



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404-1.0.html'),404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


#初始化文件
if __name__=='__main__':
    app.run('',8000,threaded=True)

