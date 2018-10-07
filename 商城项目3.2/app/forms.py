from flask_wtf import Form    #必须要的flask扩展
from wtforms  import  StringField,BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):  #继承自werkzurg的form
    openid = StringField('openid',validators=[DataRequired()])  #获取文本域内容
    remember_me = BooleanField('remember_me',default=False)  #获取布尔值域内容





