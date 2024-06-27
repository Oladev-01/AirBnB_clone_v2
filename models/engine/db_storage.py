#!/usr/bin/python3
"""this module defines the database storage for the program"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import Base
import os


class DBStorage():
    """this class defines the database"""
    __all_model = {"State": State, "Amenity": Amenity, 'Place': Place,
                   'Review': Review, 'City': City, 'User': User}
    __engine = None
    __session = None

    def __init__(self):
        mysql_usr = os.getenv('HBNB_MYSQL_USER')
        mysql_pwd = os.getenv('HBNB_MYSQL_PWD')
        mysql_host = os.getenv('HBNB_MYSQL_HOST')
        mysql_db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(mysql_usr, mysql_pwd,
                                              mysql_host, mysql_db),
                                      pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def all(self, cls=None):
        objects = {}
        if cls is None:
            for model in DBStorage.__all_model.values():
                query_selection = self.__session.query(model).all()
                for obj in query_selection:
                    key = f"{obj.__class__.__name__}.{obj.id}"
                    objects[key] = obj

        else:
            if any(cls == value for value in DBStorage.__all_model.values()):
                query_selection = self.__session.query(cls).all()
            for obj in query_selection:
                key = f"{obj.__class__.__name__}.{obj.id}"
                objects[key] = obj
        return objects

    def new(self, obj):
        """this method adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """this method commit all changes of the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """this method deletes from the current
          database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """this method creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(sessionmaker(bind=self.__engine,
                                                     expire_on_commit=False))

    def close(self):
        """this clears existing configuration"""
        self.__session.remove()
