#!/usr/bin/env python3
"""This module contains tests for the clients file"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from clients import GithubOrgClient
from typing import List, Dict


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""
    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('clients.get_json', return_value={"key": "value"})
    def test_org(self, org_name, mock_get_json):
        """Test organization"""
        client = GithubOrgClient(org_name)
        result = client.org
        mock_get_json.assert_called_once_with(GithubOrgClient.ORG_URL.format
                                              (org=org_name))
        self.assertEqual(result, {"key": "value"})


if __name__ == "__main__":
    unittest.main()
