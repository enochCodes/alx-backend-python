#!/usr/bin/env python3
"""Test case for unitls
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for the AccessNestedMap function"""
    @parameterized.expand
    def test_access_nested_map(self):
        """" Test case for access_nested_map"""
        data = {'a': {'b': {'c': 1}}}
        self.assertEqual(access_nested_map(data, ['a', 'b', 'c']), 1)


if __name__ == '__main__':
    unittest.main()
