from flask import Flask, render_template, request
from json import dumps as jsonstring

app = Flask(__name__)

class OS():
    def __init__(self, name, year, price, image):
        self.name = name
        self.year = year
        self.price = price
        self.image = image

    def __str__(self):
        return ("Название: ", name,
                " Год выхода:", year,
                " Цена:", price,
                " Логотип:", image,)

class Comp():
    def __init__(self, name, os, country):
        self.name = name
        self.os = os
        self.country = country

    def __str__(self):
        return ("Название: ", name,
                " Операционные системы:", os,
                " Страна:", country)

windows = OS("Windows 10",2012,50,"windows.png")
linux = OS("Linux",1995,40,"Linux.png")
macOS = OS("macOS",2000,60,"macOS.jpg")

oss = [windows,linux,macOS]

comp_sm = Comp("ЗИЛ-130",oss,"Россия")

@app.route("/")
def hello_world():
    return render_template('index.html',comp = comp_sm)

@app.route("/new_os")
def adding():
    name = request.args.get('name')
    year = request.args.get('year')
    price = request.args.get('price')
    new_dep = OS(name,year,price,"EZy.jpg")
    comp_sm.os.append(new_dep)
    return "Добавил"

@app.route("/delete")
def deleting():
    name = request.args.get('name')
    c = 0
    for d in comp_sm.os:
        if d.name == name:
            del comp_sm.os[c]
            return "Удалил " + d.name
        else:
            c = c + 1
    return "Не нашёл такую кафедру"

@app.route("/change")
def changing():
    name = request.args.get('name')
    price = request.args.get('price')
    c = 0
    for d in comp_sm.os:
        if d.name == name:
            comp_sm.os[c].price = price
            comp_sm.os[c].name = "Changed"
            return "Поменял цену у " + d.name
        else:
            c = c + 1
    return "Не нашёл такую кафедру"