#!/usr/bin/python3
# page return Hello wit flask
from flask import Flask

app = Flask(__name__)
app.strict_slashes=False

@app.route('/')
def router():
    """ return hello HBNB"""
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
