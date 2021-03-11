# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.event import Event  # noqa: E501
from metal.types.interconnection import Interconnection  # noqa: E501
from metal.types.interconnection_create_input import InterconnectionCreateInput  # noqa: E501
from metal.types.interconnection_list import InterconnectionList  # noqa: E501
from metal.types.interconnection_port import InterconnectionPort  # noqa: E501
from metal.types.interconnection_port_list import InterconnectionPortList  # noqa: E501
from metal.types.interconnection_update_input import InterconnectionUpdateInput  # noqa: E501
from metal.types.virtual_circuit import VirtualCircuit  # noqa: E501
from metal.types.virtual_circuit_create_input import VirtualCircuitCreateInput  # noqa: E501
from metal.types.virtual_circuit_list import VirtualCircuitList  # noqa: E501
from metal.types.virtual_circuit_update_input import VirtualCircuitUpdateInput  # noqa: E501
from metal.test import BaseTestCase


class TestConnectionsController(BaseTestCase):
    """ConnectionsController integration test stubs"""

    def test_create_connection_port_virtual_circuit(self):
        """Test case for create_connection_port_virtual_circuit

        Create a new Virtual Circuit
        """
        virtual_circuit = {
  "vnid" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "nni_vlan" : 2468,
  "name" : "name",
  "description" : "description",
  "project" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "speed" : 0,
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}/ports/{port_id}/virtual-circuits'.format(connection_id='connection_id_example', port_id='port_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(virtual_circuit),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_organization_interconnection(self):
        """Test case for create_organization_interconnection

        Request a new connection for the organization
        """
        connection = {
  "name" : "name",
  "description" : "description",
  "project" : "project",
  "redundancy" : "redundancy",
  "type" : "type",
  "facility" : "facility",
  "speed" : "speed",
  "contact_email" : "contact_email",
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{organization_id}/connections'.format(organization_id='organization_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(connection),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_project_interconnection(self):
        """Test case for create_project_interconnection

        Request a new connection for the project's organization
        """
        connection = {
  "name" : "name",
  "description" : "description",
  "project" : "project",
  "redundancy" : "redundancy",
  "type" : "type",
  "facility" : "facility",
  "speed" : "speed",
  "contact_email" : "contact_email",
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{project_id}/connections'.format(project_id='project_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(connection),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_interconnection(self):
        """Test case for delete_interconnection

        Delete connection
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_virtual_circuit(self):
        """Test case for delete_virtual_circuit

        Delete a virtual circuit
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-circuits/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_connection_events(self):
        """Test case for find_connection_events

        Retrieve connection events
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example']),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}/events'.format(connection_id='connection_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_connection_port_events(self):
        """Test case for find_connection_port_events

        Retrieve connection port events
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example']),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}/ports/{id}/events'.format(connection_id='connection_id_example', id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_virtual_circuit_events(self):
        """Test case for find_virtual_circuit_events

        Retrieve connection events
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example']),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-circuit/{id}/events'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_connection_port(self):
        """Test case for get_connection_port

        Get a connection port
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}/ports/{id}'.format(connection_id='connection_id_example', id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_interconnection(self):
        """Test case for get_interconnection

        Get connection
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_virtual_circuit(self):
        """Test case for get_virtual_circuit

        Get a virtual circuit
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-circuits/{id}'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_connection_port_virtual_circuits(self):
        """Test case for list_connection_port_virtual_circuits

        List a connection port's virtual circuits
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}/ports/{port_id}/virtual-circuits'.format(connection_id='connection_id_example', port_id='port_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_connection_ports(self):
        """Test case for list_connection_ports

        List a connection's ports
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}/ports'.format(connection_id='connection_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_organization_list_interconnections(self):
        """Test case for organization_list_interconnections

        List organization connections
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{organization_id}/connections'.format(organization_id='organization_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_project_list_interconnections(self):
        """Test case for project_list_interconnections

        List project connections
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{project_id}/connections'.format(project_id='project_id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_interconnection(self):
        """Test case for update_interconnection

        Update connection
        """
        connection = {
  "name" : "name",
  "description" : "description",
  "redundancy" : "redundancy",
  "contact_email" : "contact_email",
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/connections/{connection_id}'.format(connection_id='connection_id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(connection),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_virtual_circuit(self):
        """Test case for update_virtual_circuit

        Update a virtual circuit
        """
        virtual_circuit = {
  "vnid" : "vnid",
  "name" : "name",
  "description" : "description",
  "speed" : "speed",
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-circuits/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(virtual_circuit),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
