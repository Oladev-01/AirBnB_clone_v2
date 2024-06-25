#!/usr/bin/python3
"""this module creates a flask instance listening on 0.0.0.0
port 5000"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)  # instantiating flask


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returning string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def accept_var(text):
    """return string"""
    safe = escape(text).replace('_', ' ')
    return f"C {safe}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<var>', strict_slashes=False)
def some_str(var="is cool"):
    """return str along with var or default"""
    safe = escape(var).replace('_', ' ')
    return f"Python {safe}"


@app.route('/number/<int:var>', strict_slashes=False)
def must_be_num(var):
    """must be num"""
    return f"{escape(var)} is a number"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
