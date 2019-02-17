#!/usr/bin/python3
"""unit test for BaseModel class
"""
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
        """ tear down """
        try:
            os.remove("file.json")
        except:
            pass

    def test_doc(self):
        """testing docstrings"""
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertIsNotNone(FileStorage.reload.__doc__)    

    def test_all(self):
        """ test method all """
        my_model = FileStorage()
        my_model_dict = my_model.all()
        self.assertIsNotNone(my_model_dict)
        self.assertIs(my_model_dict, my_model._FileStorage__objects)
        self.assertEqual(type(my_model_dict), dict)

    def test_new(self):
        """ test method new """
        my_model = FileStorage()
        my_model_dict = my_model.all()
        gary = User()
        gary.id = 123
        gary.name = "Link"
        my_model.new(gary)
        key = "{}.{}".format(gary.__class__.__name__, gary.id)
        self.assertIsNotNone(my_model_dict[key])


    def test_save(self):
        """ test if file.json is saved or created"""
        my_model = FileStorage()
        my_model.name = "Gary"
        my_model.my_number = 89
        my_model.save()
        self.assertTrue(os.path.isfile('file.json'))

    def test_reload(self):
        """ test method reload """
        my_model = FileStorage()
        with open("file.json", "w") as f:
            f.write("{}")
        with open("file.json", "r") as r:
            for line in r:
                self.assertEqual(line, "{}")
        self.assertIs(my_model.reload(), None)


if __name__ == "__main__":
    unittest.main()
