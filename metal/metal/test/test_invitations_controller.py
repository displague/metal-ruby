# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.invitation import Invitation  # noqa: E501
from metal.types.invitation_input import InvitationInput  # noqa: E501
from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.membership import Membership  # noqa: E501
from metal.test import BaseTestCase


class TestInvitationsController(BaseTestCase):
    """InvitationsController integration test stubs"""

    def test_accept_invitation(self):
        """Test case for accept_invitation

        Accept an invitation
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/invitations/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_organization_invitation(self):
        """Test case for create_organization_invitation

        Create an invitation for an organization
        """
        invitation = {
  "projects_ids" : [ "projects_ids", "projects_ids" ],
  "roles" : [ "roles", "roles" ],
  "message" : "message",
  "invitee" : "invitee"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/invitations'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(invitation),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_project_invitation(self):
        """Test case for create_project_invitation

        Create an invitation for a project
        """
        invitation = {
  "projects_ids" : [ "projects_ids", "projects_ids" ],
  "roles" : [ "roles", "roles" ],
  "message" : "message",
  "invitee" : "invitee"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{project_id}/invitations'.format(project_id='project_id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(invitation),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_decline_invitation(self):
        """Test case for decline_invitation

        Decline an invitation
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/invitations/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_invitation_by_id(self):
        """Test case for find_invitation_by_id

        View an invitation
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/invitations/{id}'.format(id='id_example'),
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

    def test_find_organization_invitations(self):
        """Test case for find_organization_invitations

        Retrieve organization invitations
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
            '/metal/v1/organizations/{id}/invitations'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_invitations(self):
        """Test case for find_project_invitations

        Retrieve project invitations
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
            '/metal/v1/projects/{project_id}/invitations'.format(project_id='project_id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
