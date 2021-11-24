#!/usr/bin/python3
""" Place Module for HBNB project """
from os import environ
from sqlalchemy.sql.expression import table
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, Table
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity

Table("place_amenity", Base.metadata,
      Column("place_id", String(60), ForeignKey("places.id"),
             nullable=False, primary_key=True),
      Column("amenity_id", String(60), ForeignKey("amenities.id"),
             nullable=False, primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    try:
        if environ['HBNB_TYPE_STORAGE'] == "db":
            reviews = relationship("Review", backref="place")
            amenities = relationship("Amenity",
                                     secondary="place_amenity", viewonly=False)

    except Exception as ex:
        @property
        def reviews(self):
            """getter for reviews"""
            reviews_list = models.storage.all(type(Review))
            matching_reviews = []
            for i in reviews_list:
                if reviews_list.get(i).place_id == self.id:
                    matching_reviews.append(reviews_list.get(i))
            return matching_reviews

        @property
        def amenities(self):
            """getter for amenities"""
            amenities_list = models.storage.all(Amenity)
            matching_amenities = []
            for i in amenities_list:
                if amenities_list.get(i).id in self.amenity_ids:
                    matching_amenities.append(amenities_list.get(i))
            return matching_amenities

        @amenities.setter
        def size(self, amenity):
            """setter for amenities"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
