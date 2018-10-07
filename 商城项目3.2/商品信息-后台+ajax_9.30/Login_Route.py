from flask import Flask,request,render_template,session,url_for,redirect

from .form import Form


app = Flask(__name__)

@app.route('login',methods=['GET','POST'])
def login():
    form = Form()
    if form.validate_on_submit():
        