#!/usr/bin/python3
"""
Test cases for FileStorage class
"""

import os
import json
import unittest
from datetime import datetime
import sys
sys.path.append('../../../')
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorageInstantiation(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def test_instantiation_no_arguments(self):
        """Test FileStorage instantiation with no arguments."""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_instantiation_with_argument(self):
        """Test FileStorage instantiation with an argument."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_file_path_is_private_string(self):
        """Test if __file_path is a private string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_objects_is_private_dictionary(self):
        """Test if __objects is a private dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_initializes(self):
        """Test if models.storage initializes as an instance of FileStorage"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorageMethods(unittest.TestCase):
    """Test cases for the methods of the FileStorage class."""

    @classmethod
    def setUpClass(cls):
        """Set up the test class."""
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class."""
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test the all() method of FileStorage."""
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_method_with_argument(self):
        """Test the all() method of FileStorage with an argument."""
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method_with_arguments(self):
        """Test the new() method of FileStorage with arguments."""
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_method(self):
        """Test the new() method of FileStorage."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        objects = models.storage.all()
        self.assertIn("<BaseModel>." + base_model.id, objects.keys())
        self.assertIn(base_model, objects.values())
        self.assertIn("<User>." + user.id, objects.keys())
        self.assertIn(user, objects.values())
        self.assertIn("<State>." + state.id, objects.keys())
        self.assertIn(state, objects.values())
        self.assertIn("<Place>." + place.id, objects.keys())
        self.assertIn(place, objects.values())
        self.assertIn("<City>." + city.id, objects.keys())
        self.assertIn(city, objects.values())
        self.assertIn("<Amenity>." + amenity.id, objects.keys())
        self.assertIn(amenity, objects.values())
        self.assertIn("<Review>." + review.id, objects.keys())
        self.assertIn(review, objects.values())

    def test_save_method(self):
        """Test the save() method of FileStorage."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + base_model.id, save_text)
            self.assertIn("User." + user.id, save_text)
            self.assertIn("State." + state.id, save_text)
            self.assertIn("Place." + place.id, save_text)
            self.assertIn("City." + city.id, save_text)
            self.assertIn("Amenity." + amenity.id, save_text)
            self.assertIn("Review." + review.id, save_text)

    def test_save_method_with_argument(self):
        """Test the save() method of FileStorage with an argument."""
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method_with_argument(self):
        """Test the reload() method of FileStorage with an argument."""
        with self.assertRaises(TypeError):
            models.storage.reload(None)

    def test_reload_method(self):
        """Test the reload() method of FileStorage."""
        base_model = BaseModel()
        user = User()
        state = State()
        place = Place()
        city = City()
        amenity = Amenity()
        review = Review()
        models.storage.new(base_model)
        models.storage.new(user)
        models.storage.new(state)
        models.storage.new(place)
        models.storage.new(city)
        models.storage.new(amenity)
        models.storage.new(review)
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects
        self.assertIn("<BaseModel>." + base_model.id, objects)
        self.assertIn("<User>." + user.id, objects)
        self.assertIn("<State>." + state.id, objects)
        self.assertIn("<Place>." + place.id, objects)
        self.assertIn("<City>." + city.id, objects)
        self.assertIn("<Amenity>." + amenity.id, objects)
        self.assertIn("<Review>." + review.id, objects)


if __name__ == "__main__":
    unittest.main()