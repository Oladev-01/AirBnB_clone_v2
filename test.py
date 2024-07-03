#!/usr/bin/python3
from models.place import Place
from models import *

session = storage._DBStorage__session
owner_name = "Lynn Melton"
query_result = session.query(Place).filter_by(name="Beautiful Home 1 Mile from Downtown").first()
print(query_result.description)
print(type(query_result))