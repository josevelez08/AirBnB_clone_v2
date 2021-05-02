#!/usr/bin/python3
"""page return the url's parameters"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def router():
    return "Hello HBNB!"

@app.route('/hbnb')
def router1():
    return "HBNB"

@app.route('/c/<text>')
def print_variable(text):
        var = text.replace("_", " ")
        return "C is {}".format(var)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)