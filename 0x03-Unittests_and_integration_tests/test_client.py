#!/usr/bin/env python3

import unittest
from typing import Dict
from unittest.mock import patch, Mock, MagicMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Class that inherits from unittest.TestCase"""
    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"})
    ])
    
    @patch('client.get_json')
    def test_org(self, org: str, response: Dict, mocked: MagicMock) -> None:
        """Test that GithubOrgClient.org returns the correct value"""
        mocked.return_value = MagicMock(return_value=response)
        gh_org_client = GithubOrgClient(org)

        self.assertEqual(gh_org_client.org(), response)
        mocked.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )