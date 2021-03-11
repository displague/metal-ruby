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
from models.ports_api import PortsApi  # noqa: E501
from metal.rest import ApiException


class TestPortsApi(unittest.TestCase):
    """PortsApi unit test stubs"""

    def setUp(self):
        self.api = models.ports_api.PortsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_assign_native_vlan(self):
        """Test case for assign_native_vlan

        Assign a native VLAN  # noqa: E501
        """
        pass

    def test_assign_port(self):
        """Test case for assign_port

        Assign a port to virtual network  # noqa: E501
        """
        pass

    def test_bond_port(self):
        """Test case for bond_port

        Enabling bonding  # noqa: E501
        """
        pass

    def test_convert_layer2(self):
        """Test case for convert_layer2

        Convert to Layer 2  # noqa: E501
        """
        pass

    def test_convert_layer3(self):
        """Test case for convert_layer3

        Convert to Layer 3  # noqa: E501
        """
        pass

    def test_delete_native_vlan(self):
        """Test case for delete_native_vlan

        Remove native VLAN  # noqa: E501
        """
        pass

    def test_disbond_port(self):
        """Test case for disbond_port

        Disabling bonding  # noqa: E501
        """
        pass

    def test_find_port_by_id(self):
        """Test case for find_port_by_id

        Retrieve a port  # noqa: E501
        """
        pass

    def test_unassign_port(self):
        """Test case for unassign_port

        Unassign a port  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
