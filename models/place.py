#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    reviews = relationship('Review', cascade="all, delete-orphan", backref='place')

    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
                          )
    amenities = relationship('Amenity', secondary=place_amenity, viewonly=False)
    amenity_ids = []
    @property
    def amenities(self):
        from models import storage
        """Getter attribute for amenities"""
        print("i was at the amenity getter")
        amenities_list = []
        for am_id in Place.amenity_ids:
            amenity = storage.get(Amenity, am_id)
            if amenity:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        """Setter attribute for amenities"""
        print("amenity setter")
        if isinstance(obj, Amenity):
            Place.amenity_ids.append(obj)

    @property
    def reviews(self):
        """this method return Review instances from the filestorage whose
        place.id is the same as the current instance id"""
        from models import storage
        from models.review import Review
        place_inst = []
        for review in storage.all(Review).values():
            if review.place_id == self.id:
                place_inst.append(review)
        return place_inst
    
