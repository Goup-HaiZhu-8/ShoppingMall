from flask import Flask,render_template,request

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'GET':
       return  render_template('phonePage.html')
    elif request.method == 'POST':
       data = request.get_json()
       print(data.get('data'))
       return 'get_data'


if __name__ == '__main__':
    app.run('',port='9999',debug=True)
