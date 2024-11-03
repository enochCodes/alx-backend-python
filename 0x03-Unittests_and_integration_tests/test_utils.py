#!/usr/bin/env python3
"""Test case for unitls
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Dict, Tuple


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the AccessNestedMap function"""

    @parameterized.expand([
           ({"a": 1}, ("a",), 1),
           ({"a": {"b": 2}}, ("a",), {"b": 2}),
           ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
        self,
        nested_map: Dict,
        path:Tuple[str],
        expected: Any,
    ) -> None:
        """Test access_nested_map with various inputs and expected results"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
        ])
    def test_access_nested_map_exception(
        self,
        nested_map: Dict,
        path: Tuple[str],
        exception: Exception
    ) -> None:
        """Tests `access_nested_map`'s exception raising."""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()
