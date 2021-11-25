#!/usr/bin/python3
""" Module for testing MySQL db storage"""
import unittest
from models import Amenity, City, Place, Review, State, User
from models import storage
from models.engine.db_storage import DBStorage
import os
import MySQLdb


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                 "using database storage")
class test_db_storage(unittest.TestCase):
    """MySQL db tests"""

    @classmethod
    def setUpClass(cls):
        cls.db = MySQLdb.connect(host=os.getenv('HBNB_MYSQL_HOST'),
                                 user=os.getenv('HBNB_MYSQL_USER'),
                                 passwd=os.getenv('HBNB_MYSQL_PWD'),
                                 db=os.getenv('HBNB_MYSQL_DB'),
                                 port=3306
                                 )
        cls.cur = cls.db.cursor()

    @classmethod
    def tearDownClass(cls):
        cls.cur.close()
        cls.db.close()

    def test_instance(self):
        """confirm correct instance"""
        self.assertIsInstance(storage, DBStorage)

    def test_access(self):
        self.cur.execute("SELECT * from states")
        self.assertTrue(self.cur.fetchall() != None)
