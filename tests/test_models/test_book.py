#!/usr/bin/python3
"""This is the test for Book class"""
import unittest
import os
from models.user import User
from models.base_model import BaseModel
from models.book import Book
from models import storage


class TestBook(unittest.TestCase):
    """This is the unittest for Book class"""

    def setUp(self):
        """Set up for the tests"""
        self.my_book = Book()

    def tearDown(self):
        """Tearing down at the end of the test"""
        del self.my_book

    def test_is_instance(self):
        """Test for an instance of Book"""
        self.assertIsInstance(self.my_book, Book)

    def test_is_subclass(self):
        """Test if Book is a subclass of BaseModel"""
        self.assertTrue(issubclass(self.my_book.__class__, BaseModel))