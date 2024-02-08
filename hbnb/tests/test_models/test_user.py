#!/usr/bin/python3
"""Test module for User class"""

import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('../../')
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def tearDown(self):
        del self.user

    def test_class_instace(self):
        self.assertEqual(type(User.inst), int)

    def test_email_attribute(self):
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.user, BaseModel)

    def test_str_method(self):
        expected = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected)

    def test_created_at_and_updated_at(self):
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertAlmostEqual(self.user.created_at,
                               datetime.now(), delta=timedelta(minutes=1))
        self.assertAlmostEqual(self.user.updated_at,
                               datetime.now(), delta=timedelta(minutes=1))

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn("__class__", user_dict)
        self.assertIn("id", user_dict)
        self.assertIn("created_at", user_dict)
        self.assertIn("updated_at", user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['id'], self.user.id)
        self.assertEqual(user_dict['created_at'],
                         self.user.created_at.isoformat())
        self.assertEqual(user_dict['updated_at'],
                         self.user.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
