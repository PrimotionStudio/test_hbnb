#!/usr/bin/python3
"""Test module for Place class"""

import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('../../')
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):

    def setUp(self):
        self.place = Place()

    def tearDown(self):
        del self.place

    def test_class_instace(self):
        self.assertEqual(type(Place.inst), int)

    def test_city_id_attribute(self):
        self.assertTrue(hasattr(self.place, 'city_id'))
        self.assertEqual(self.place.city_id, "")

    def test_user_id_attribute(self):
        self.assertTrue(hasattr(self.place, 'user_id'))
        self.assertEqual(self.place.user_id, "")

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.place, 'name'))
        self.assertEqual(self.place.name, "")

    def test_description_attribute(self):
        self.assertTrue(hasattr(self.place, 'description'))
        self.assertEqual(self.place.description, "")

    def test_number_rooms_attribute(self):
        self.assertTrue(hasattr(self.place, 'number_rooms'))
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms_attribute(self):
        self.assertTrue(hasattr(self.place, 'number_bathrooms'))
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest_attribute(self):
        self.assertTrue(hasattr(self.place, 'max_guest'))
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night_attribute(self):
        self.assertTrue(hasattr(self.place, 'price_by_night'))
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude_attribute(self):
        self.assertTrue(hasattr(self.place, 'latitude'))
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude_attribute(self):
        self.assertTrue(hasattr(self.place, 'longitude'))
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids_attribute(self):
        self.assertTrue(hasattr(self.place, 'amenity_ids'))
        self.assertEqual(self.place.amenity_ids, [])

    def test_inheritance(self):
        self.assertIsInstance(self.place, BaseModel)

    def test_str_method(self):
        expected = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected)

    def test_created_at_and_updated_at(self):
        self.assertTrue(hasattr(self.place, 'created_at'))
        self.assertTrue(hasattr(self.place, 'updated_at'))
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertAlmostEqual(self.place.created_at,
                               datetime.now(), delta=timedelta(minutes=1))
        self.assertAlmostEqual(self.place.updated_at,
                               datetime.now(), delta=timedelta(minutes=1))

    def test_to_dict_method(self):
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
