#!/usr/bin/python3
from models import storage
from models.state import State

# Retrieve all states
states = storage.all(State)
for state in states.values():
    if state.name == 'Nigeria':
        storage.delete(state)
        storage.save()
# Print each state's id and name
