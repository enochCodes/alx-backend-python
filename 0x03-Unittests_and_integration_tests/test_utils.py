#!/usr/bin/env python3
"""Test case for unitls
"""
import unittest
from parameterized import parameterized
from typing import Any, Dict, Tuple
from unittest.mock import patch, Mock
from utils import access_nested_map
from utils import get_json


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
        path: Tuple[str],
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


class TestGetJson(unittest.TestCase):
    """Test cases for the get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch("requests.get")
    def test_get_json(
        self,
        test_url: str,
        test_payload: Dict,
        mock_get: Mock
    ) -> None:
        """Test get_json with a parameterized url and payload"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)


if __name__ == '__main__':
    unittest.main()
