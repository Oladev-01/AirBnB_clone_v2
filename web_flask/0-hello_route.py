#!/usr/bin/python3
"""this module creates a flask instance routing to root
which is listening for any incoming external connections
on port 5000"""

from flask import Flask

app = Flask(__name__)  # creating flask instance


@app.route('/', strict_slashes=False)
def hello_hnbb():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
