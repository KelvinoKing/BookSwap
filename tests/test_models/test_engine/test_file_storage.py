#!/usr/bin/python3
"""Unittest for file_storage.py"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """Tests for the file storage class"""
    def setUp(self):
        """Sets up testing methods"""
        self.b1 = BaseModel()
        self.b1.save()
        self.b2 = BaseModel()
        self.b2.save()
        self.b3 = BaseModel()
        self.b3.save()

    def tearDown(self):
        """Tears down testing methods"""
        try:
            os.remove("file.json")
        except:
            pass

    def test_all(self):
        """Tests the all method"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIsNotNone(all_objs)
        self.assertEqual(type(all_objs), dict)
        self.assertIs(all_objs, storage._FileStorage__objects)

    def test_new(self):
        """Tests the new method"""
        storage = FileStorage()
        all_objs = storage.all()
        self.assertIn("BaseModel." + self.b1.id, all_objs.keys())
        self.assertIn("BaseModel." + self.b2.id, all_objs.keys())
        self.assertIn("BaseModel." + self.b3.id, all_objs.keys())
        self.assertIs(all_objs["BaseModel." + self.b1.id], self.b1)
        self.assertIs(all_objs["BaseModel." + self.b2.id], self.b2)
        self.assertIs(all_objs["BaseModel." + self.b3.id], self.b3)

    def test_save(self):
        """Tests the save method"""
        storage = FileStorage()
        all_objs = storage.all()
        self.b1.save()
        self.b2.save()
        self.b3.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue(len(all_objs) > 0)

    def test_reload(self):
        """Tests the reload method"""
        storage = FileStorage()
        all_objs = storage.all()
        self.b1.save()
        self.b2.save()
        self.b3.save()
        self.assertTrue(os.path.isfile("file.json"))
        self.assertTrue(len(all_objs) > 0)
        storage.reload()
        all_objs = storage.all()
        self.assertIn("BaseModel." + self.b1.id, all_objs.keys())
        self.assertIn("BaseModel." + self.b2.id, all_objs.keys())
        self.assertIn("BaseModel." + self.b3.id, all_objs.keys())