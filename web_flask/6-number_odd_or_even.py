#!/usr/bin/python3
"""this module creates a flask instance listening on 0.0.0.0
port 5000"""

from flask import Flask, render_template
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


@app.route('/number_template/<int:num>', strict_slashes=False)
def html_formatting(num):
    """return dynamic html"""
    return render_template('5-number.html', n=num)


@app.route('/number_odd_or_even/<int:num>', strict_slashes=False)
def check_for_odd(num):
    """check if the value parsed is odd/even"""
    if num % 2 == 0:
        return render_template('6-number_odd_or_even.html',
                               n=f"{escape(num)} is even")
    else:
        return render_template('6-number_odd_or_even.html',
                               n=f"{escape(num)} is odd")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
