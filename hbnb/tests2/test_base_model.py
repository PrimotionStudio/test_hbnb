#!/usr/bin/python3
"""
Test module for BaseModel class
"""

from time import sleep
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class
    """

    def setUp(self):
        """
        Set up test fixtures
        """
        self.model = BaseModel()

    def tearDown(self):
        """
        Clean up after each test method
        """
        del self.model

    def test_attributes_existence(self):
        """
        Test existence of id, created_at, and updated_at attributes
        """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))

    def test_id_generation(self):
        """
        Test generation of id attribute
        """
        self.assertTrue(hasattr(self.model, 'id'))
        self.assertIsNotNone(self.model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at_and_updated_at(self):
        """
        Test creation and update timestamps
        """
        self.assertTrue(hasattr(self.model, 'created_at'))
        self.assertTrue(hasattr(self.model, 'updated_at'))
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """
        Test string representation of BaseModel instance
        """
        expected = "[BaseModel] ({}) {}".format(self.model.id,
                                                self.model.__dict__)
        self.assertEqual(str(self.model), expected)

    def test_to_dict_method(self):
        """
        Test conversion of BaseModel instance to dictionary
        """
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

    def test_to_dict_datetime_attributes_are_strs(self):
        """Test if the 'created_at' and 'updated_at' attributes in the
        dictionary returned by the 'to_dict' are converted to strings."""
        base_model_insta = BaseModel()
        base_model_dict = base_model_insta.to_dict()
        self.assertEqual(str, type(base_model_dict["created_at"]))
        self.assertEqual(str, type(base_model_dict["updated_at"]))

    def test_to_dict_type(self):
        """Test if the 'to_dict' method returns a dictionary."""
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))

    def test_to_dict_contains_correct_keys(self):
        """Test if the dictionary returned by the 'to_dict' method contains
        the correct keys."""
        bm = BaseModel()
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    def test_to_dict_contains_added_attributes(self):
        """Test if the dictionary returned by the 'to_dict' method contains
        the attributes added to the BaseModel instance."""
        bm = BaseModel()
        bm.name = "Hello"
        bm.my_number = 90
        self.assertIn("name", bm.to_dict())
        self.assertIn("my_number", bm.to_dict())

    def test_docstring(self):
        """
        Test docstring
        """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_kwarg(self):
        """
        Test instantiation with keyword arguments
        """
        base_model = BaseModel(name="base")
        self.assertEqual(type(base_model).__name__, "BaseModel")
        self.assertFalse(hasattr(base_model, "id"))
        self.assertFalse(hasattr(base_model, "created_at"))
        self.assertTrue(hasattr(base_model, "name"))
        self.assertFalse(hasattr(base_model, "updated_at"))
        self.assertTrue(hasattr(base_model, "__class__"))

    def test_two_models_different_created_at(self):
        """
        Test creation of two BaseModel instances
        with different created_at times
        """
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_instantiation_with_kwargs(self):
        """
        Test instantiation of BaseModel with keyword arguments
        """
        date_time = datetime.today()
        date_time_iso = date_time.isoformat()
        base_model = BaseModel(id="345", created_at=date_time_iso,
                               updated_at=date_time_iso)
        self.assertEqual(base_model.id, "345")
        self.assertEqual(base_model.created_at, date_time)
        self.assertEqual(base_model.updated_at, date_time)

    def test_no_args_instantiates(self):
        """
        Test instantiation of BaseModel with no arguments
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_two_instances_unique_ids(self):
        """
        Test uniqueness of ids for two BaseModel instances
        """
        base_model_insta1 = BaseModel()
        base_model_insta2 = BaseModel()
        self.assertNotEqual(base_model_insta1.id, base_model_insta2.id)

    def test_str_representation(self):
        """
        Test string representation of BaseModel instance
        """
        date_time = datetime.today()
        date_time_repr = repr(date_time)
        bm = BaseModel()
        bm.id = "123456"
        bm.created_at = bm.updated_at = date_time
        bm_str = bm.__str__()
        self.assertIn("[BaseModel] (123456)", bm_str)
        self.assertIn("'id': '123456'", bm_str)
        self.assertIn("'created_at': " + date_time_repr, bm_str)
        self.assertIn("'updated_at': " + date_time_repr, bm_str)

    def test_save_updates_file(self):
        """
        Test if saving BaseModel updates the file
        """
        bm = BaseModel()
        bm.save()
        bm_id = "BaseModel." + bm.id
        with open("file.json", "r") as f:
            self.assertIn(bm_id, f.read())

    def test_one_save(self):
        """
        Test if saving BaseModel updates the 'updated_at' attribute
        """
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        self.assertLess(first_updated_at, bm.updated_at)

    def test_two_saves(self):
        """
        Test if two consecutive saves update the 'updated_at'
        attribute accordingly
        """
        bm = BaseModel()
        sleep(0.05)
        first_updated_at = bm.updated_at
        bm.save()
        second_updated_at = bm.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        bm.save()
        self.assertLess(second_updated_at, bm.updated_at)

    def test_save_with_arg(self):
        """
        Test if saving BaseModel raises TypeError when an argument is provided
        """
        bm = BaseModel()
        with self.assertRaises(TypeError):
            bm.save(None)


if __name__ == '__main__':
    unittest.main()
