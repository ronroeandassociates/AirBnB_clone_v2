#!/usr/bin/python3
"""Module for testing BaseModel Class"""
from models import BaseModel, City, Place, State, User
import unittest
import datetime
from uuid import UUID
import json
import os


class test_basemodel(unittest.TestCase):
    """BaseModel testing"""

    def __init__(self, *args, **kwargs):
        """Init for basemodel testing"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel
        self.dict = {}
        self.state = State(**{'name': "test_state"})
        self.city = City(**{'state_id': self.state.id, 'name': "test_city"})
        self.user = User(**{'email': "test@test.net",
                            'password': "test_password"})
        self.place = Place(**{'city_id': self.city.id, 'user_id': self.user.id,
                              'description': "", 'latitude': 0.0,
                              'longitude': 0.0, 'name': 'test_place'})

    def setUp(self):
        """pre-test actions"""
        pass

    def tearDown(self):
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """type of initialized class"""
        i = self.value(**self.dict)
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """kwargs creation with a copy """
        i = self.value(**self.dict)
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """try creating with incorrect kwargs """
        i = self.value(**self.dict)
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "test relies on filestorage")
    def test_save(self):
        """ Testing save """
        i = self.value(**self.dict)
        i.save()
        key = f"{self.name}.{i.id}"
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """str method"""
        i = self.value(**self.dict)
        self.assertEqual(str(i), f'[{self.name}] ({i.id}) {i.__dict__}')

    def test_todict(self):
        """to_dict method"""
        i = self.value(**self.dict)
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test creation with None for Kwarg key:value"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """kwargs with one value, prev failed"""
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertIsInstance(new, self.value)

    def test_id(self):
        """confirm id is a str"""
        new = self.value(**self.dict)
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """conform created_at is datetime"""
        new = self.value(**self.dict)
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """confirm updated_at is datetime & is updated when needed"""
        new = self.value(**self.dict)
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
