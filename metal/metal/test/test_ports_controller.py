# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.port import Port  # noqa: E501
from metal.types.port_assign_input import PortAssignInput  # noqa: E501
from metal.types.port_convert_layer3_input import PortConvertLayer3Input  # noqa: E501
from metal.test import BaseTestCase


class TestPortsController(BaseTestCase):
    """PortsController integration test stubs"""

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

    def test_assign_port(self):
        """Test case for assign_port

        Assign a port to virtual network
        """
        vnid = {
  "vnid" : "vnid"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/assign'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(vnid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_bond_port(self):
        """Test case for bond_port

        Enabling bonding
        """
        query_string = [('bulk_enable', True)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/bond'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_convert_layer2(self):
        """Test case for convert_layer2

        Convert to Layer 2
        """
        vnid = {
  "vnid" : "vnid"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/convert/layer-2'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(vnid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_convert_layer3(self):
        """Test case for convert_layer3

        Convert to Layer 3
        """
        request_ips = {
  "request_ips" : [ {
    "address_family" : 0,
    "public" : true
  }, {
    "address_family" : 0,
    "public" : true
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/convert/layer-3'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(request_ips),
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

    def test_disbond_port(self):
        """Test case for disbond_port

        Disabling bonding
        """
        query_string = [('bulk_disable', True)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/disbond'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_port_by_id(self):
        """Test case for find_port_by_id

        Retrieve a port
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_unassign_port(self):
        """Test case for unassign_port

        Unassign a port
        """
        vnid = {
  "vnid" : "vnid"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ports/{id}/unassign'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(vnid),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
