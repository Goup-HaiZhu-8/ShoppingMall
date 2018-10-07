from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators  import DataRequired


class Form(FlaskForm):
     name = StringField('please input your name',validators=[DataRequired()])
     password = PasswordField(validators=[DataRequired()])
     submit = SubmitField('注册')
     