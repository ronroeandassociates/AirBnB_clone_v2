#!/usr/bin/python3
"""This module defines a class to manage DataBase storage for hbnb clone"""
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import os
from sqlalchemy import create_engine


# SQL engine test will be needed
# New engine DBStorage: (models/engine/db_storage.py)

class DBStorage:
    """ SQL DB Storage"""
# Private class attributes
    __engine = None
    __session = None

    def __init__(self):
        """Initializes the DBStroage"""
        # create the engine
        # linked to the MySQL database and user created before
        # (hbnb_dev and hbnb_dev_db):
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")

        self.__engine = create_engine(
            f'mysql+mysqldb://{user}:{pwd}@{host}/{db}', pool_pre_ping=True
        )


        if os.getenv("HBNB_ENV") == "test":
            Base.matadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        Returns all instances of a class if the class name is passed.
        If it's empty, return all instances of valid classes.
        """
        all_dict = {}
        # classes = ['Places', 'State', 'Review', 'City', 'User', 'Amenity']
        if cls:
            result = self.__session.query(cls).all()
            for item in result:
                key = f'{item.__class__.__name__}.{item.id}'
                all_dict[key] = item
        else:
            for x in Base.__subclasses__():
                result = self.__session.query(x).all()
                for item in result:
                    key = f'{item.__class__.__name__}.{item.id}'
                    all_dict[key] = item
        return all_dict

    def new(self, obj):
        """NEW"""
        try:
            self.__session.add(obj)
        except Exception:
            pass

    def save(self):
        """Save"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload """
        Base.metadata.create_all(self.__engine)
        curr = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(curr)
        self.__session = Session()
        self.save()

    def close(self):
        """END the  session"""
        self.__session.close()
