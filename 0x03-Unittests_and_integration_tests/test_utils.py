#!/usr/bin/env python3
"""
Unit test for utils.access_nested_map.
"""
import unittest
from parameterized import parameterized

access_nested_map = __import__('utils').access_nested_map

class TestAccessNestedMap(unittest.TestCase):
    """
    Class that inherits from unittest.TestCase.
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that the method returns what it is supposed to"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

