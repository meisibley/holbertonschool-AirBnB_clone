#!/usr/bin/python3
"""Defines the unittests for models/engine/file_storage.py

Unittest classes:
    TestFileStorage_instantiation
    TestFileStorage_methods
"""
import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage_instantiation(unittest.TestCase):
    """Unitests for testing instances of clase: FileStorage"""

    def test_FileStorage_no_arguments(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_with_arguments(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_private_and_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_private_and_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage(self):
        self.assertEqual(type(models.storage), FileStorage)
