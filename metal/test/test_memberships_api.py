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
from models.memberships_api import MembershipsApi  # noqa: E501
from metal.rest import ApiException


class TestMembershipsApi(unittest.TestCase):
    """MembershipsApi unit test stubs"""

    def setUp(self):
        self.api = models.memberships_api.MembershipsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_membership(self):
        """Test case for delete_membership

        Delete the membership  # noqa: E501
        """
        pass

    def test_find_membership_by_id(self):
        """Test case for find_membership_by_id

        Retrieve a membership  # noqa: E501
        """
        pass

    def test_find_project_memberships(self):
        """Test case for find_project_memberships

        Retrieve project memberships  # noqa: E501
        """
        pass

    def test_update_membership(self):
        """Test case for update_membership

        Update the membership  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
