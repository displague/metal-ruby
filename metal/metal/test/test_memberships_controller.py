# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.membership import Membership  # noqa: E501
from metal.types.membership_input import MembershipInput  # noqa: E501
from metal.types.membership_list import MembershipList  # noqa: E501
from metal.test import BaseTestCase


class TestMembershipsController(BaseTestCase):
    """MembershipsController integration test stubs"""

    def test_delete_membership(self):
        """Test case for delete_membership

        Delete the membership
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/memberships/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_membership_by_id(self):
        """Test case for find_membership_by_id

        Retrieve a membership
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/memberships/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_memberships(self):
        """Test case for find_project_memberships

        Retrieve project memberships
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
            '/metal/v1/projects/{project_id}/memberships'.format(project_id='project_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_membership(self):
        """Test case for update_membership

        Update the membership
        """
        membership = {
  "role" : [ "role", "role" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/memberships/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(membership),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
