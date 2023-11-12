#!/usr/bin/python3
"""module for test base class"""
import unittest
import json
from models.base import Base 
class TestBase(unittest.TestCase):
    """Tests for the Base class"""

    def test_too_many_args(self):
        """Test that initializing with too many arguments raises TypeError"""
        with self.assertRaises(TypeError):
            Base(1, 1)

    def test_default_id(self):
        """Test that id is set to 1 when not provided"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_custom_id(self):
        """Test that id is set to the provided value"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def test_reset_id(self):
        """Test that id is incremented after being set"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_private_nb_objects(self):
        """Test that nb_objects is a private instance attribute"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            getattr(b, 'nb_objects')

    def test_to_json_string(self):
        """Test to_json_string with a list of dictionaries"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertIsInstance(json_s, str)
        self.assertEqual(json.loads(json_s), [d1, d2])

    def test_empty_to_json_string(self):
        """Test to_json_string with an empty list"""
        json_s = Base.to_json_string([])
        self.assertIsInstance(json_s, str)
        self.assertEqual(json_s, "[]")

    def test_none_to_json_string(self):
        """Test to_json_string with None"""
        json_s = Base.to_json_string(None)
        self.assertIsInstance(json_s, str)
        self.assertEqual(json_s, "[]")

    def test_from_json_string(self):
        """Test from_json_string with a valid JSON string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
                     {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertIsInstance(json_l, list)
        self.assertEqual(len(json_l), 2)
        self.assertIsInstance(json_l[0], dict)
        self.assertEqual(json_l[0], {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})

    def test_from_json_string_empty(self):
        """Test from_json_string with an empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def test_from_json_string_none(self):
        """Test from_json_string with None"""
        self.assertEqual([], Base.from_json_string(None))
