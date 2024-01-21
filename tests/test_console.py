#!/usr/bin/python3
"""
Contains the class TestConsoleDocs
"""

import console
import inspect
import pycodestyle as pep8
import unittest
BookSwapCommand = console.BookSwapCommand


class TestConsoleDocs(unittest.TestCase):
    """Class for testing documentation of the console"""
    
    def test_console_module_docstring(self):
        """Test for the console.py module docstring"""
        self.assertIsNot(console.__doc__, None,
                         "console.py needs a docstring")
        self.assertTrue(len(console.__doc__) >= 1,
                        "console.py needs a docstring")

    def test_BookSwapCommand_class_docstring(self):
        """Test for the BookSwapCommand class docstring"""
        self.assertIsNot(BookSwapCommand.__doc__, None,
                         "BookSwapCommand class needs a docstring")
        self.assertTrue(len(BookSwapCommand.__doc__) >= 1,
                        "BookSwapCommand class needs a docstring")