#!/usr/bin/python3
"""Test Module for State"""

import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('../../')
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):

    def setUp(self):
        self.state = State()

    def tearDown(self):
        del self.state

    def test_class_instace(self):
        self.assertEqual(type(State.inst), int)

    def test_name_attribute(self):
        self.assertTrue(hasattr(self.state, 'name'))
        self.assertEqual(self.state.name, "")

    def test_inheritance(self):
        self.assertIsInstance(self.state, BaseModel)

    def test_str_method(self):
        expected = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected)

    def test_created_at_and_updated_at(self):
        self.assertTrue(hasattr(self.state, 'created_at'))
        self.assertTrue(hasattr(self.state, 'updated_at'))
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertAlmostEqual(self.state.created_at,
                               datetime.now(), delta=timedelta(minutes=1))
        self.assertAlmostEqual(self.state.updated_at,
                               datetime.now(), delta=timedelta(minutes=1))

    def test_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertIn("__class__", state_dict)
        self.assertIn("id", state_dict)
        self.assertIn("created_at", state_dict)
        self.assertIn("updated_at", state_dict)
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['id'], self.state.id)
        self.assertEqual(state_dict['created_at'],
                         self.state.created_at.isoformat())
        self.assertEqual(state_dict['updated_at'],
                         self.state.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
