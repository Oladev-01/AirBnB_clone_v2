#!/usr/bin/python3
"""flask instance. defining url that request
from the database"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def clean_up(exception):
    """close the connection"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_cities_states():
    """listing the states in alphabetical order"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda state: state.name)
    cities = list(storage.all(City).values())
    cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html',
                           states=states, cities=cities)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
