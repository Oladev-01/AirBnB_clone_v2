#!/usr/bin/python3
"""flask instance. defining url that request
from the database"""

from flask import Flask, render_template
from models import storage
from models import *


app = Flask(__name__)


@app.teardown_appcontext
def clean_up(exception):
    """close the connection"""
    storage.close()


@app.route('/states', strict_slashes=False)
def list_states():
    """listing the states in alphabetical order"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_city_by_state_id(id):
    """list cities by state id"""
    state = storage.all(State).get('State.' + id)
    if state:
        cities = list(sorted(state.cities, key=lambda city: city.name))
        return render_template('9-states.html', state=state,
                               cities=cities, not_found=False)
    elif state is None:
        return render_template('9-states.html', not_found=True)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
