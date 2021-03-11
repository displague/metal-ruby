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
from models.connections_api import ConnectionsApi  # noqa: E501
from metal.rest import ApiException


class TestConnectionsApi(unittest.TestCase):
    """ConnectionsApi unit test stubs"""

    def setUp(self):
        self.api = models.connections_api.ConnectionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_connection_port_virtual_circuit(self):
        """Test case for create_connection_port_virtual_circuit

        Create a new Virtual Circuit  # noqa: E501
        """
        pass

    def test_create_organization_interconnection(self):
        """Test case for create_organization_interconnection

        Request a new connection for the organization  # noqa: E501
        """
        pass

    def test_create_project_interconnection(self):
        """Test case for create_project_interconnection

        Request a new connection for the project's organization  # noqa: E501
        """
        pass

    def test_delete_interconnection(self):
        """Test case for delete_interconnection

        Delete connection  # noqa: E501
        """
        pass

    def test_delete_virtual_circuit(self):
        """Test case for delete_virtual_circuit

        Delete a virtual circuit  # noqa: E501
        """
        pass

    def test_find_connection_events(self):
        """Test case for find_connection_events

        Retrieve connection events  # noqa: E501
        """
        pass

    def test_find_connection_port_events(self):
        """Test case for find_connection_port_events

        Retrieve connection port events  # noqa: E501
        """
        pass

    def test_find_virtual_circuit_events(self):
        """Test case for find_virtual_circuit_events

        Retrieve connection events  # noqa: E501
        """
        pass

    def test_get_connection_port(self):
        """Test case for get_connection_port

        Get a connection port  # noqa: E501
        """
        pass

    def test_get_interconnection(self):
        """Test case for get_interconnection

        Get connection  # noqa: E501
        """
        pass

    def test_get_virtual_circuit(self):
        """Test case for get_virtual_circuit

        Get a virtual circuit  # noqa: E501
        """
        pass

    def test_list_connection_port_virtual_circuits(self):
        """Test case for list_connection_port_virtual_circuits

        List a connection port's virtual circuits  # noqa: E501
        """
        pass

    def test_list_connection_ports(self):
        """Test case for list_connection_ports

        List a connection's ports  # noqa: E501
        """
        pass

    def test_organization_list_interconnections(self):
        """Test case for organization_list_interconnections

        List organization connections  # noqa: E501
        """
        pass

    def test_project_list_interconnections(self):
        """Test case for project_list_interconnections

        List project connections  # noqa: E501
        """
        pass

    def test_update_interconnection(self):
        """Test case for update_interconnection

        Update connection  # noqa: E501
        """
        pass

    def test_update_virtual_circuit(self):
        """Test case for update_virtual_circuit

        Update a virtual circuit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
