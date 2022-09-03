#!/usr/bin/python3
"""Flask,baby"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    return "HBNB"


@app.route("/c/<path:text>", strict_slashes=False)
def C(text):
    return "C " + text.replace('_', ' ')


@app.route("/python", defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route("/python/<path:text>", strict_slashes=False)
def python(text='is_cool'):
    return "Python " + text.replace('_', ' ')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
