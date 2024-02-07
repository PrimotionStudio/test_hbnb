#!/usr/bin/python3
"""Test module for Place class"""

from models.base_model import BaseModel
from models.place import Place
import unittest
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def setUp(self):
        """Set up a Place instance for testing"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test"""
        del self.place

    def test_city_id_attribute(self):
        """Test city_id attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        """Test user_id attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        """Test name attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        """Test description attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attribute(self):
        """Test number_rooms attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        """Test number_bathrooms attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        """Test max_guest attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attribute(self):
        """Test price_by_night attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attribute(self):
        """Test latitude attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_attribute(self):
        """Test longitude attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        """Test amenity_ids attribute existence and default value"""
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        """Test if Place inherits from BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_str_method(self):
        """Test the __str__ method"""
        expected = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes"""
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertAlmostEqual(self.place.created_at, self.place.updated_at,
                               delta=datetime.utcnow())

    def test_to_dict_method(self):
        """Test the to_dict method"""
        place_dict = self.place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn("__class__", place_dict)
        self.assertIn("id", place_dict)
        self.assertIn("created_at", place_dict)
        self.assertIn("updated_at", place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['id'], self.place.id)
        self.assertEqual(place_dict['created_at'],
                         self.place.created_at.isoformat())
        self.assertEqual(place_dict['updated_at'],
                         self.place.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
