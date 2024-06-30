#!/usr/bin/python3
from models import *
from models import storage

states = list(storage.all(State).values())
states = sorted(states, key=lambda state: state.name)
for state in states:
    print(f"this is the state\t{state.id}:{state.name}")
    print("these are the cities")
    cities = sorted(state.cities, key=lambda city: city.name)
    for city in cities:
        print(f"{city.id}:{city.name}")

