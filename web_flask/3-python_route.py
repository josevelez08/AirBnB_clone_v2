#!/usr/bin/python3
""" python return page"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def router():
    """ return hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb')
def router1():
    """return HBNB"""
    return "HBNB"


@app.route('/python/')
@app.route('/python/<text>')
def hello(text="is cool"):
    """ return python and parameters"""
    var = text.replace("_", " ")
    return "Python {}".format(var)


@app.route('/c/<text>')
def print_variable(text):
    """ return c and parameters"""
    var = text.replace("_", " ")
    return "C is {}".format(var)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
