#!/usr/bin/python3
""" page return only integers"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def router():
    """return HEllo HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb')
def router1():
    """return HBNH"""
    return "HBNB"


@app.route('/python/')
@app.route('/python/<text>')
def hello(text="is cool"):
    """ return parameters and python"""
    var = text.replace("_", " ")
    return "Python {}".format(var)


@app.route('/c/<text>')
def print_variable(text):
        """ return c and parameters"""
        var = text.replace("_", " ")
        return "C is {}".format(var)


@app.route('/number/<int:n>')
def print_integer(n):
        """return only integers"""
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
