#!/usr/bin/env python3
"""
class TestAccessNestedMap
"""
import unittest
from unittest.mock import Mock, patch

from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    test access nested map
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Compares the maps vs the expected
        :return: True or False
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b'),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_key):
        with self.assertRaises(KeyError) as context_manager:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context_manager.exception), f"'{expected_key}'")


class TestGetJson(unittest.TestCase):
    """
    class TestGetJson
    to test http requests
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),

    ])
    @patch('utils.requests.get')
    def test_get_json(self, url, payload, mock):
        """
        Mocks the API Json response
        :return: True or False
        """
        mock_response = Mock()
        mock_response.json.return_value = payload
        mock.return_value = mock_response

        result = get_json(url)

        mock.assert_called_once_with(url)
        self.assertEqual(result, payload)


class TestMemoize(unittest.TestCase):
    """
    class TestMemoize
    """
    def test_memoize(self):
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42):
            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
