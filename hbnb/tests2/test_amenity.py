#!/usr/bin/python3
"""Test module for Amenity class"""
import sys
sys.path.append("../")
import models
from models.base_model import BaseModel
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """
        Set up method to create an instance of Amenity before each test.
        """
        self.amenity = Amenity()

    def tearDown(self):
        """
        Tear down method to delete the instance of Amenity after each test.
        """
        del self.amenity

    def test_attributes_existence(self):
        """
        Test case to check the existence of attributes.
        """
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))

    def test_attribute_initialization(self):
        """
        Test case to check the initialization of attributes.
        """
        self.assertEqual(self.amenity.name, "")
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_attributes(self):
        """
            Test case to check that Amenity class had name attribute.
        """
        new_amenity = Amenity()
        self.assertTrue("name" in new_amenity.__dir__())

    def test_inheritance(self):
        """
        Test case to check if Amenity inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_str_method(self):
        """
        Test case to check the __str__ method.
        """
        expected = "[Amenity] ({}) {}".format(self.amenity.id,
                                              self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected)

    def test_attribute_type(self):
        """
            Test case to check that Amenity class had name attribute's type.
        """
        amenity_dict = Amenity()
        name_value = getattr(amenity_dict, "name")
        self.assertIsInstance(name_value, str)

    def test_to_dict_method(self):
        """
        Test case to check the to_dict method.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn("__class__", amenity_dict)
        self.assertIn("id", amenity_dict)
        self.assertIn("created_at", amenity_dict)
        self.assertIn("updated_at", amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['id'], self.amenity.id)
        self.assertEqual(amenity_dict['created_at'],
                         self.amenity.created_at.isoformat())
        self.assertEqual(amenity_dict['updated_at'],
                         self.amenity.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
