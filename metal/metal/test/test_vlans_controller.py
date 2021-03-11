# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.internet_gateway import InternetGateway  # noqa: E501
from metal.types.port import Port  # noqa: E501
from metal.types.virtual_network import VirtualNetwork  # noqa: E501
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput  # noqa: E501
from metal.types.virtual_network_list import VirtualNetworkList  # noqa: E501
from metal.test import BaseTestCase


class TestVLANsController(BaseTestCase):
    """VLANsController integration test stubs"""

    def test_assign_native_vlan(self):
        """Test case for assign_native_vlan

        Assign a native VLAN
        """
        query_string = [('vnid', 'vnid_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/native-vlan'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_internet_gateway(self):
        """Test case for create_internet_gateway

        Create an internet gateway
        """
        query_string = [('length', 'length_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-networks/{id}/internet-gateways'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_virtual_network(self):
        """Test case for create_virtual_network

        Create an virtual network
        """
        virtual_network = {
  "vxlan" : 0,
  "vlan" : 6,
  "project_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "description" : "description",
  "facility" : "facility"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/virtual-networks'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(virtual_network),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_native_vlan(self):
        """Test case for delete_native_vlan

        Remove native VLAN
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/native-vlan'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_virtual_network(self):
        """Test case for delete_virtual_network

        Delete a virtual network
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-networks/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_virtual_networks(self):
        """Test case for find_virtual_networks

        Retrieve all virtual networks
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/virtual-networks'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_virtual_network(self):
        """Test case for get_virtual_network

        Get a virtual network
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-networks/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
