# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.bgp_session_input import BGPSessionInput  # noqa: E501
from metal.types.bgp_config import BgpConfig  # noqa: E501
from metal.types.bgp_config_request_input import BgpConfigRequestInput  # noqa: E501
from metal.types.bgp_session import BgpSession  # noqa: E501
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.types.bgp_session_neighbors import BgpSessionNeighbors  # noqa: E501
from metal.test import BaseTestCase


class TestBGPController(BaseTestCase):
    """BGPController integration test stubs"""

    def test_create_bgp_session(self):
        """Test case for create_bgp_session

        Create a BGP session
        """
        bgp_session = {
  "address_family" : "address_family",
  "default_route" : true
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/bgp/sessions'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(bgp_session),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_bgp_session(self):
        """Test case for delete_bgp_session

        Delete the BGP session
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/bgp/sessions/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_bgp_config_by_project(self):
        """Test case for find_bgp_config_by_project

        Retrieve a bgp config
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/bgp-config'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_bgp_session_by_id(self):
        """Test case for find_bgp_session_by_id

        Retrieve a BGP session
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/bgp/sessions/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_bgp_sessions(self):
        """Test case for find_bgp_sessions

        Retrieve all BGP sessions
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/bgp/sessions'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_bgp_sessions(self):
        """Test case for find_project_bgp_sessions

        Retrieve all BGP sessions for project
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/bgp/sessions'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_bgp_neighbor_data(self):
        """Test case for get_bgp_neighbor_data

        Retrieve BGP neighbor data for this device
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/bgp/neighbors'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_request_bgp_config(self):
        """Test case for request_bgp_config

        Requesting bgp config
        """
        bgp_config_request = {
  "use_case" : "use_case",
  "deployment_type" : "deployment_type",
  "asn" : 0,
  "md5" : "md5"
}
        headers = { 
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/bgp-configs'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(bgp_config_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_bgp_session(self):
        """Test case for update_bgp_session

        Update the BGP session
        """
        default_route = True
        headers = { 
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/bgp/sessions/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(default_route),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
