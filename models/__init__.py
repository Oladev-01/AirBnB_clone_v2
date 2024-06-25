#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.user import User


models_t = os.getenv('HBNB_TYPE_STORAGE')
if models_t == 'db':
    storage = DBStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
