#!/usr/bin/python3
"""Test module for User class"""

from models.base_model import BaseModel
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the User class"""

    def setUp(self):
        """Set up a User instance for testing"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test method"""
        del self.user

    def test_email_attribute(self):
        """Test the email attribute"""
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertEqual(self.user.email, "")

    def test_password_attribute(self):
        """Test the password attribute"""
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertEqual(self.user.password, "")

    def test_first_name_attribute(self):
        """Test the first_name attribute"""
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertEqual(self.user.first_name, "")

    def test_last_name_attribute(self):
        """Test the last_name attribute"""
        self.assertTrue(hasattr(self.user, 'last_name'))
        self.assertEqual(self.user.last_name, "")

    def test_inheritance(self):
        """Test inheritance from BaseModel"""

    def test_str_method(self):
        """Test the __str__ method"""
        expected = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected)

    def test_created_at_and_updated_at(self):
        """Test the created_at and updated_at attributes"""
        self.assertTrue(hasattr(self.user, 'created_at'))
        self.assertTrue(hasattr(self.user, 'updated_at'))
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertAlmostEqual(self.user.created_at,
                               self.user.updated_at, delta=datetime.utcnow())

    def test_to_dict_method(self):
        """Test the to_dict method"""
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

    def test_email_validation(self):
        """Test email validation"""
        # Test valid email format
        self.user.email = "test@example.com"
        self.assertEqual(self.user.email, "test@example.com")

    def test_update_behavior(self):
        """Test update behavior"""
        old_updated_at = self.user.updated_at
        self.user.email = "test@example.com"

    def test_serialization_deserialization(self):
        """Test serialization and deserialization"""
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(new_user.__dict__, self.user.__dict__)


if __name__ == '__main__':
    unittest.main()
