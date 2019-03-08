from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get('name', '游客')

    return render_template('index.html', name = name)

@app.route('/bye')
def bye():
    return '拜拜！'
