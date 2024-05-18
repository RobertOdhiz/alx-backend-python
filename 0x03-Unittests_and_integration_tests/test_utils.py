#!/usr/bin/env python3
""" module with TestAccesssNestedMap """
import unittest
from parameterized import parameterized
from typing import Dict, Tuple, Union


class TestAccessNestedMap(unittest.TestCase):
    """ TestAccessNestedMap class definition """
    @parametarized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
            ) -> None:
        """ to test that the method returns what it is supposed to. """
        self.assertEqual(access_nested_map(nested_map, path), expected)
