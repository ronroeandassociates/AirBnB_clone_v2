#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey


class Amenity(BaseModel, Base):
    """gives the amenities available for a place"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
