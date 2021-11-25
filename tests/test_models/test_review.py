#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review
        self.dict = {'place_id': self.place.id, 'user_id': self.user.id,
                     'text': ""}

    def test_place_id(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ """
        new = self.value(**self.dict)
        self.assertEqual(type(new.text), str)
