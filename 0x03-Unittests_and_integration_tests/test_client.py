#!/usr/bin/env python3

import unittest
from typing import Dict
from unittest.mock import patch, Mock, MagicMock, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient

class TestGithubOrgClient(unittest.TestCase):
    """Tests for the GithubOrgClient class."""
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

    def test_public_repos_url(self) -> None:
        """Tests that _public_repos_url returns the expected URL."""
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )