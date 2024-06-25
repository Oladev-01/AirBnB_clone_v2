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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
