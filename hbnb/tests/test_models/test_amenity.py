#!/usr/bin/python3
"""Test Module for Amenity class"""

import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('../../')
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        del self.amenity

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(self.amenity.name, "")

    def test_class_instace(self):
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertEqual(Amenity.inst, 1)

    def test_inheritance(self):
        self.assertIsInstance(self.amenity, BaseModel)

    def test_str_method(self):
        expected = "[Amenity] ({}) <{}>".format(
            self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected)

    def test_to_dict_method(self):
        amenity_dict = self.amenity.to_dict()
        expected_dict = {
            '__class__': 'Amenity',
            'id': self.amenity.id,
            'created_at': self.amenity.created_at.isoformat(),
            'updated_at': self.amenity.updated_at.isoformat(),
            'name': ''
        }
        self.assertEqual(self.amenity.to_dict(), expected_dict)
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

    def test_created_at_and_updated_at(self):
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertAlmostEqual(self.amenity.created_at,
                               datetime.now(), delta=timedelta(minutes=1))
        self.assertAlmostEqual(self.amenity.updated_at,
                               datetime.now(), delta=timedelta(minutes=1))


if __name__ == '__main__':
    unittest.main()
