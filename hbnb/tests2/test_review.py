#!/usr/bin/python3
"""Test module for Review class"""

from models.base_model import BaseModel
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up a Review instance for testing"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test"""
        del self.review

    def test_place_id_attribute(self):
        """Test place_id attribute existence and default value"""
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertEqual(self.review.place_id, "")

    def test_user_id_attribute(self):
        """Test user_id attribute existence and default value"""
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertEqual(self.review.user_id, "")

    def test_text_attribute(self):
        """Test text attribute existence and default value"""
        self.assertTrue(hasattr(self.review, 'text'))
        self.assertEqual(self.review.text, "")

    def test_inheritance(self):
        """Test inheritance from BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_str_method(self):
        """Test string representation method"""
        expected = "[Review] ({}) {}".format(self.review.id,
                                             self.review.__dict__)
        self.assertEqual(str(self.review), expected)

    def test_created_at_and_updated_at(self):
        """Test created_at and updated_at attributes"""
        self.assertTrue(hasattr(self.review, 'created_at'))
        self.assertTrue(hasattr(self.review, 'updated_at'))
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertAlmostEqual(self.review.created_at, self.review.updated_at,
                               delta=datetime.utcnow())

    def test_to_dict_method(self):
        """Test to_dict method"""
        review_dict = self.review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn("__class__", review_dict)
        self.assertIn("id", review_dict)
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['id'], self.review.id)
        self.assertEqual(review_dict['created_at'],
                         self.review.created_at.isoformat())
        self.assertEqual(review_dict['updated_at'],
                         self.review.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
