# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import metal
from models.bgp_api import BGPApi  # noqa: E501
from metal.rest import ApiException


class TestBGPApi(unittest.TestCase):
    """BGPApi unit test stubs"""

    def setUp(self):
        self.api = models.bgp_api.BGPApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_bgp_session(self):
        """Test case for create_bgp_session

        Create a BGP session  # noqa: E501
        """
        pass

    def test_delete_bgp_session(self):
        """Test case for delete_bgp_session

        Delete the BGP session  # noqa: E501
        """
        pass

    def test_find_bgp_config_by_project(self):
        """Test case for find_bgp_config_by_project

        Retrieve a bgp config  # noqa: E501
        """
        pass

    def test_find_bgp_session_by_id(self):
        """Test case for find_bgp_session_by_id

        Retrieve a BGP session  # noqa: E501
        """
        pass

    def test_find_bgp_sessions(self):
        """Test case for find_bgp_sessions

        Retrieve all BGP sessions  # noqa: E501
        """
        pass

    def test_find_project_bgp_sessions(self):
        """Test case for find_project_bgp_sessions

        Retrieve all BGP sessions for project  # noqa: E501
        """
        pass

    def test_get_bgp_neighbor_data(self):
        """Test case for get_bgp_neighbor_data

        Retrieve BGP neighbor data for this device  # noqa: E501
        """
        pass

    def test_request_bgp_config(self):
        """Test case for request_bgp_config

        Requesting bgp config  # noqa: E501
        """
        pass

    def test_update_bgp_session(self):
        """Test case for update_bgp_session

        Update the BGP session  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
