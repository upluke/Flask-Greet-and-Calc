# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)


@app.route('/add')
def myAdd():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(add(a, b))


@app.route('/sub')
def mySub():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(sub(a, b))


@app.route('/mult')
def myMult():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(mult(a, b))


@app.route('/div')
def myDiv():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(div(a, b))


# Further Study
# Make a single route/view function that can deal with 4 different kinds of URLs:
OPERATORS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}


@app.route('/math/<operator>')
def cal(operator):
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = OPERATORS[operator](a, b)
    return str(res)
