#!/usr/bin/env python3
"""Unittest for base_model.py module"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for base_model.py"""

    def setUp(self):
        """Set up testing environment"""

        self.model = BaseModel()

    def test_init(self):
        """Test for proper initialization"""

        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        """Test for proper __str__ output"""

        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test for proper save method"""

        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        """Test for proper to_dict method"""

        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

    def test_kwargs(self):
        """Test for proper instance creation with kwargs"""

        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertNotEqual(self.model, new_model)


if __name__ == '__main__':
    unittest.main()