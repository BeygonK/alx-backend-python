#!/usr/bin/env python3
"""This module test a method"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Any, Sequence, Mapping


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({}, ("a",), "'a'"),
        ({"a": 1}, ("a", "b"), "'b'"),
        ])
    def test_access_nested_map_exception(self,
                                         nested_map: Mapping,
                                         path: Sequence,
                                         expected_message: str) -> None:
        """Test access_nested_map with exception"""
        with self.assertRaises(Exception) as e:
            access_nested_map(nested_map, path)
        self.assertEqual(str(e.exception), expected_message)

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping,
                               path: Sequence,
                               expected: Any) -> None:
        """Method to test"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


if __name__ == "__main__":
    unittest.main()
