'''
此模块用于封装登录功能,引用了flask的扩展模块wtforms
也可以不用这个模块,自己对用户信息进行验证
'''

from flask_wtf import Form   #flask扩展
from wtforms import StringField,TextAreaField   #TextAreaField暂时用不到
from wtforms.validators import DataRequired,Email,Length  #Length暂时用不到

class  LoginForm(Form):
    user_name = StringField('Name',
                             validators=[DataRequired()])
    text = StringField('Password',
                         validators=[DataRequired()])
    email = StringField (u'Email',
                           validators=[Email()])

#检测器可以自己重写,例如Email()

