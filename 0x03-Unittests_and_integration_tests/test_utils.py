#!/usr/bin/env python3
"""Test case for unitls
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the AccessNestedMap function"""

    @parameterized.expand([
           ({"a": 1}, ("a",), 1),
           ({"a": {"b": 2}}, ("a",), {"b": 2}),
           ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs and expected results"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == '__main__':
    unittest.main()
