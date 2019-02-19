#!/usr/bin/python3
"""unit test for BaseModel class
"""
from models.base_model import BaseModel
import unittest
import json
import os


class TestBaseModel(unittest.TestCase):
    """ class Base Model with tests """

    def setUp(self):
        """ set up """
        pass

    def tearDown(self):
        """ tear down """
        try:
            del file.json
        except:
            pass
    
    def test_doc(self):
        """testing docstrings"""
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_save(self):
        """ test if current datetime is updated """
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    def test_attr(self):
        """ test for attributes of BaseModel """
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertTrue(hasattr(my_model, "__init__")) 
        self.assertTrue(hasattr(my_model, "id"))
        self.assertTrue(hasattr(my_model, "created_at"))
        self.assertTrue(hasattr(my_model, "updated_at"))

if __name__ == "__main__":
    unittest.main()
