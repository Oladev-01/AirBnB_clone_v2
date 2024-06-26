#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    __cities = relationship("City", cascade="all,\
                           delete-orphan", backref="state")

    @property
    def cities(self):
        """this method returns City instances from file storage
          whose state id is the
        same as the current instance id"""
        if models.models_t != 'db':
            from models import storage
            from models.city import City
            cities_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
        else:
            return self.__cities
