#!/usr/bin/python3
from models import storage
from models.state import State

# Retrieve all states
state_dict = storage.all()
states = list(state_dict.values())
states = sorted(states, key=lambda state: state.name)
for state in states:
    print(f"{state.id} and it's name {state.name}")
# Print each state's id and name
