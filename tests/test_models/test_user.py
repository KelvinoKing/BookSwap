#!/usr/bin/python3
"""This is the test for User class"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    """This is the unittest for User class"""

    def setUp(self):
        """Set up for the tests"""
        self.my_user = User()

    def tearDown(self):
        """Tearing down at the end of the test"""
        del self.my_user

    def test_is_instance(self):
        """Test for an instance of User"""
        self.assertIsInstance(self.my_user, User)

    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.my_user.__class__, BaseModel))