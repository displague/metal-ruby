# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.ssh_key import SSHKey  # noqa: E501
from metal.types.ssh_key_input import SSHKeyInput  # noqa: E501
from metal.types.ssh_key_list import SSHKeyList  # noqa: E501
from metal.test import BaseTestCase


class TestSSHKeysController(BaseTestCase):
    """SSHKeysController integration test stubs"""

    def test_create_project_ssh_key(self):
        """Test case for create_project_ssh_key

        Create a ssh key for the given project
        """
        ssh_key = {
  "label" : "label",
  "key" : "key"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/ssh-keys'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(ssh_key),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_ssh_key(self):
        """Test case for create_ssh_key

        Create a ssh key for the current user
        """
        ssh_key = {
  "label" : "label",
  "key" : "key"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ssh-keys',
            method='POST',
            headers=headers,
            data=json.dumps(ssh_key),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_ssh_key(self):
        """Test case for delete_ssh_key

        Delete the ssh key
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ssh-keys/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_device_ssh_keys(self):
        """Test case for find_device_ssh_keys

        Retrieve a device's ssh keys
        """
        query_string = [('Search string', 'search_string_example'),
                        ('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/ssh-keys'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_ssh_keys(self):
        """Test case for find_project_ssh_keys

        Retrieve a project's ssh keys
        """
        query_string = [('Search string', 'search_string_example'),
                        ('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/ssh-keys'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ssh_key_by_id(self):
        """Test case for find_ssh_key_by_id

        Retrieve a ssh key
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ssh-keys/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ssh_keys(self):
        """Test case for find_ssh_keys

        Retrieve all ssh keys
        """
        query_string = [('Search string', 'search_string_example'),
                        ('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ssh-keys',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_ssh_key(self):
        """Test case for update_ssh_key

        Update the ssh key
        """
        ssh_key = {
  "label" : "label",
  "key" : "key"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ssh-keys/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(ssh_key),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
