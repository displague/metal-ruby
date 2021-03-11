# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.user import User  # noqa: E501
from metal.types.user_list import UserList  # noqa: E501
from metal.types.user_update_input import UserUpdateInput  # noqa: E501
from metal.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_find_current_user(self):
        """Test case for find_current_user

        Retrieve the current user
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_invitations(self):
        """Test case for find_invitations

        Retrieve current user invitations
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
            '/metal/v1/invitations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_user_by_id(self):
        """Test case for find_user_by_id

        Retrieve a user
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/users/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_user_customdata(self):
        """Test case for find_user_customdata

        Retrieve the custom metadata of a user
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/users/{id}/customdata'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_users(self):
        """Test case for find_users

        Retrieve all users
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
            '/metal/v1/users',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_current_user(self):
        """Test case for update_current_user

        Update the current user
        """
        user = {
  "password" : "password",
  "timezone" : "timezone",
  "last_name" : "last_name",
  "phone_number" : "phone_number",
  "avatar" : "",
  "customdata" : "{}",
  "first_name" : "first_name"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user',
            method='PUT',
            headers=headers,
            data=json.dumps(user),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
