#!/usr/bin/python3
"""Unittest for BaseModel class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def setUp(self):
        """Set up for all tests"""
        self.b1 = BaseModel()

    def tearDown(self):
        """Tear down for all tests"""
        pass

    def test_init(self):
        """Test initialization of BaseModel class"""
        self.assertTrue(isinstance(self.b1, BaseModel))

    def test_id(self):
        """Test that id is a string"""
        self.assertTrue(isinstance(self.b1.id, str))

    def test_id_unique(self):
        """Test that each id is unique"""
        b2 = BaseModel()
        self.assertNotEqual(self.b1.id, b2.id)

    def test_created_at_exists(self):
        """Test that created_at is created for each instance"""
        self.assertTrue(self.b1.created_at)

    def test_updated_at_exists(self):
        """Test that updated_at is created for each instance"""
        self.assertTrue(self.b1.updated_at)

    def test_created_at_datetime(self):
        """Test that created_at is datetime"""
        self.assertTrue(isinstance(self.b1.created_at, datetime))

    def test_updated_at_datetime(self):
        """Test that updated_at is datetime"""
        self.assertTrue(isinstance(self.b1.updated_at, datetime))

    def test_kwargs(self):
        """Test that kwargs are saved as instance attributes"""
        b2 = BaseModel(id="1234", created_at="2017-09-28T21:05:54.119427",
                       updated_at="2017-09-28T21:05:54.119572")
        self.assertTrue(isinstance(b2.id, str))
        self.assertTrue(isinstance(b2.created_at, datetime))
        self.assertTrue(isinstance(b2.updated_at, datetime))

    def test_kwargs_more(self):
        """Test that kwargs are saved as instance attributes"""
        b2 = BaseModel(name="John", number=89)
        self.assertTrue(isinstance(b2.name, str))
        self.assertTrue(isinstance(b2.number, int))

    def test_kwargs_empty(self):
        """Test that kwargs are saved as instance attributes"""
        b2 = BaseModel()
        self.assertTrue(isinstance(b2, BaseModel))

    def test_kwargs_my_model_is_not_my_new_model(self):
        """Test that kwargs are saved as instance attributes"""
        b2 = BaseModel()
        b2.name = "John"
        b2.number = 89
        b2_json = b2.to_dict()
        b3 = BaseModel(**b2_json)
        self.assertFalse(b2 is b3)

    def test_uuid(self):
        """Test that uuid is a string"""
        self.assertTrue(isinstance(self.b1.id, str))

    def test_created_at(self):
        """Test that created_at is datetime"""
        self.assertTrue(isinstance(self.b1.created_at, datetime))

    def test_updated_at(self):
        """Test that updated_at is datetime"""
        self.assertTrue(isinstance(self.b1.updated_at, datetime))

    def test_str(self):
        """Test that the str method has the correct output"""
        self.assertEqual(str(self.b1), "[{}] ({}) {}".format(
            self.b1.__class__.__name__, self.b1.id, self.b1.__dict__))

    def test_save(self):
        """Test that save method updates updated_at"""
        old_updated_at = self.b1.updated_at
        self.b1.save()
        self.assertNotEqual(old_updated_at, self.b1.updated_at)

    def test_to_dict(self):
        """Test that to_dict method returns correct output"""
        b1_dict = self.b1.to_dict()
        self.assertEqual(b1_dict["__class__"], "BaseModel")
        self.assertEqual(type(b1_dict["created_at"]), str)
        self.assertEqual(type(b1_dict["updated_at"]), str)