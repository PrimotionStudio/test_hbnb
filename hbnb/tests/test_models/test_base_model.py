#!/usr/bin/python3
"""Test Module for BaseModel class"""

import unittest
from datetime import datetime, timedelta
from unittest.mock import patch
from io import StringIO
import sys
sys.path.append('../../')
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model = BaseModel()

    def tearDown(self):
        del self.model

    def test_attributes_existence(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_class_instace(self):
        self.assertEqual(type(BaseModel.inst), int)

    def test_id_generation(self):
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at_and_updated_at(self):
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertAlmostEqual(self.model.created_at,
                               datetime.now(), delta=timedelta(minutes=1))
        self.assertAlmostEqual(self.model.updated_at,
                               datetime.now(), delta=timedelta(minutes=1))

    def test_str_method(self):
        expected = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected)

    @patch('sys.stdout', new_callable=StringIO)
    def test_save_method(self, mock_stdout):
        prev_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(prev_updated_at, self.model.updated_at)
        self.assertIn("", mock_stdout.getvalue())

    def test_to_dict_method(self):
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn("__class__", model_dict)
        self.assertIn("id", model_dict)
        self.assertIn("created_at", model_dict)
        self.assertIn("updated_at", model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
