#!/usr/bin/python3
"""Test module for City class"""

from models.base_model import BaseModel
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City()

    def tearDown(self):
        del self.city

    def test_state_id_attribute(self):
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertEqual(self.city.state_id, "")

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertEqual(self.city.name, "")

    def test_City_attributes(self):
        """
        Test the presence of 'state_id' and 'name' attributes
        in the City class.
        """
        new_city = City()
        self.assertTrue("state_id" in new_city.__dir__())
        self.assertTrue("name" in new_city.__dir__())

    def test_inheritance(self):
        self.assertIsInstance(self.city, BaseModel)

    def test_str_method(self):
        expected = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected)

    def test_created_at_and_updated_at(self):
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertAlmostEqual(self.city.created_at, self.city.updated_at,
                               delta=datetime.utcnow())

    def test_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn("__class__", city_dict)
        self.assertIn("id", city_dict)
        self.assertIn("created_at", city_dict)
        self.assertIn("updated_at", city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['id'], self.city.id)
        self.assertEqual(city_dict['created_at'],
                         self.city.created_at.isoformat())
        self.assertEqual(city_dict['updated_at'],
                         self.city.updated_at.isoformat())

    def test_type_name_attribute(self):
        """
        Test the type of the 'name' attribute in the City class.
        """
        new_city = City()
        name = getattr(new_city, "name")
        self.assertIsInstance(name, str)

    def test_type_state_id_attribute(self):
        """
        Test the type of the 'state_id' attribute in the City class.
        """
        new_city = City()
        state_id = getattr(new_city, "state_id")
        self.assertIsInstance(state_id, str)


if __name__ == '__main__':
    unittest.main()
