#!/usr/bin/python3
"""dynamic html"""

from flask import Flask, render_template
from models import *
from models.place import Place


app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def load_html():
    """load dynamic html"""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda amenity: amenity.name)
    places = sorted(storage.all(Place).values(), key=lambda place: place.name)
    return render_template('100-hbnb.html', states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def close_session(exception):
    """close session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)