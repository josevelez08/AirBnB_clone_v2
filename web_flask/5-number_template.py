#!/usr/bin/python3
""" return a html page"""
from flask import Flask
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def router():
    """return hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb')
def router1():
    """ return HBNB"""
    return "HBNB"


@app.route('/python/')
@app.route('/python/<text>')
def hello(text="is cool"):
    """ return python and parameters"""
    var = text.replace("_", " ")
    return "Python {}".format(var)


@app.route('/c/<text>')
def print_variable(text):
    """return c and parameters"""
    var = text.replace("_", " ")
    return "C is {}".format(var)


@app.route('/number/<int:n>')
def print_integer(n):
    """ return only integer"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def print_integer_html(n):
    """ return a integer in a html page"""
    return render_template("5-number.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
