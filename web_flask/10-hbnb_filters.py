#!/usr/bin/python3
"""this module starts up a flask instance"""

from flask import Flask, render_template
from models import *


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def states_amenities():
    """generating states and amenities"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    return render_template('10-hbnb_filters.html',
                           states=states, amenities=amenities)


@app.teardown_appcontext
def close_session(exception):
    """closing currrent session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
