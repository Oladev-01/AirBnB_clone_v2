#!/usr/bin/python3
from models import *
from models import storage

states = list(storage.all(State).values())
states = sorted(states, key=lambda state: state.name)
for state in states:
    print(f"this is the state\t{state.id}:{state.name}")
    print("these are the cities")

    cities = list(storage.all(City).values())
    cities = sorted(cities, key=lambda city: city.name)
    for city in cities:
        if city.state_id == state.id:
            print(f"{city.id}:{city.name}")

