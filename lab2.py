from flask import Flask
from flask import request


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    return "<p>Test</p>"

@app.route("/test/aboba")
def test_aboba():
    return "<p>Test_ABOBUS</p>"

@app.route("/name/<user>")
def name(user):
    return "<p>Привет,{}</p>".format(user)

@app.route("/calc/sum/<a>/<b>")
def calc_sum(a,b):
    a = int(a)
    b = int(b)
    return "<p>Сумма,{}</p>".format(a+b)

@app.route("/calc/scale/<a>/<b>")
def calc_scale(a,b):
    a = int(a)
    b = int(b)
    return "<p>Умножение,{}</p>".format(a*b)

@app.route("/calc/div/<a>/<b>")
def calc_div(a,b):
    a = int(a)
    b = int(b)
    return "<p>Деление, {}</p>".format(a/b)

@app.route("/calc/sub/")
def calc_sub():
    args_dict = request.args
    a = float(args_dict["a"])
    b = float(args_dict["b"])
    return "<p>Вычитание, {}</p>".format(a-b)

@app.route("/calc/food")
def food():
    args_dict = request.args
    p = args_dict["первое"]
    f = 0
    if p == "суп":
        f = 100
    elif p =='бо':
        f = 350
    elif p =='щи':
        f = 55
    b = args_dict["второе"]
    v = 0
    if b == "котлета":
        v = 100
    elif b =='бризоль':
        v = 150
    elif b =='гуляш':
        v = 195
    v = int(v)
    f = int(f)
    return "Сумма за {} и {} = {}".format(p,b,f+v)

@app.route("/pic/<name>")
def pic(name):
    return '<img src ="http://127.0.0.1:5000/static/{}.jpg">'.format(name)


