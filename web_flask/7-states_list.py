#!/usr/bin/python3
"""flask instance. defining url that request
from the database"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def clean_up(exception):
    """close the connection"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """listing the states in alphabetical order"""
    states = list(storage.all(State).values())
    states = list(sorted(states, key=lambda state: state.name))
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
