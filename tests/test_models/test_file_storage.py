#!/usr/bin/python3
"""unit test for FileStorage class
"""

import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """ class FileStorage with tests """

    def setUp(self):
        """ set up """
        pass

    def tearDown(self):
        """ remove JSON after test run """
        try:
            os.remove("file.json")
        except:
            pass

    def test_doc(self):
        """testing docstrings"""
        self.assertTrue(len(FileStorage.__doc__) > 1)
        self.assertTrue(len(FileStorage.all.__doc__) > 1)
        self.assertTrue(len(FileStorage.new.__doc__) > 1)
        self.assertTrue(len(FileStorage.save.__doc__) > 1)
        self.assertTrue(len(FileStorage.reload.__doc__) > 1)

    def test_all(self):
        """ test method all """
        store = FileStorage()
        store_dict = store.all()
        self.assertIsNotNone(store_dict)
        self.assertIs(store_dict, store._FileStorage__objects)
        self.assertEqual(type(store_dict), dict)

    def test_new(self):
        """ test method new """
        store = FileStorage()
        store_dict = store.all()
        gary = User()
        gary.id = 123
        gary.name = "Link"
        store.new(gary)
        key = "{}.{}".format(gary.__class__.__name__, gary.id)
        self.assertIsNotNone(store_dict[key])


    def test_save(self):
        """ test if file.json is saved or created"""
        store = FileStorage()
        self.assertIsInstance(store, FileStorage)
        b1 = BaseModel()
        store.new(b1)
        store.name = "Gary"
        store.my_number = 89
        store.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ test method reload """
        store = FileStorage()
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(store.reload(), None)


if __name__ == "__main__":
    unittest.main()
