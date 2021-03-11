# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.device_list import DeviceList  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal.types.facility_list import FacilityList  # noqa: E501
from metal.types.invitation import Invitation  # noqa: E501
from metal.types.invitation_input import InvitationInput  # noqa: E501
from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.operating_system import OperatingSystem  # noqa: E501
from metal.types.organization import Organization  # noqa: E501
from metal.types.organization_input import OrganizationInput  # noqa: E501
from metal.types.organization_list import OrganizationList  # noqa: E501
from metal.types.payment_method import PaymentMethod  # noqa: E501
from metal.types.payment_method_create_input import PaymentMethodCreateInput  # noqa: E501
from metal.types.payment_method_list import PaymentMethodList  # noqa: E501
from metal.types.plan_list import PlanList  # noqa: E501
from metal.types.project import Project  # noqa: E501
from metal.types.project_create_input import ProjectCreateInput  # noqa: E501
from metal.types.project_list import ProjectList  # noqa: E501
from metal.types.transfer_request_list import TransferRequestList  # noqa: E501
from metal.test import BaseTestCase


class TestOrganizationsController(BaseTestCase):
    """OrganizationsController integration test stubs"""

    def test_create_organization(self):
        """Test case for create_organization

        Create an organization
        """
        organization = {
  "website" : "website",
  "twitter" : "twitter",
  "address" : {
    "country" : "country",
    "address" : "address",
    "address2" : "address2",
    "city" : "city",
    "coordinates" : {
      "latitude" : "latitude",
      "longitude" : "longitude"
    },
    "state" : "state",
    "zip_code" : "zip_code"
  },
  "name" : "name",
  "description" : "description",
  "logo" : "",
  "billing_address" : {
    "country" : "country",
    "address" : "address",
    "address2" : "address2",
    "city" : "city",
    "coordinates" : {
      "latitude" : "latitude",
      "longitude" : "longitude"
    },
    "state" : "state",
    "zip_code" : "zip_code"
  },
  "customdata" : "{}",
  "enforce_2fa_at" : "2000-01-23T04:56:07.000+00:00"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations',
            method='POST',
            headers=headers,
            data=json.dumps(organization),
            content_type='application/json')
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

    def test_create_organization_project(self):
        """Test case for create_organization_project

        Create a project for the organization
        """
        project = {
  "payment_method_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "name" : "name",
  "customdata" : "{}"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/projects'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(project),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_payment_method(self):
        """Test case for create_payment_method

        Create a payment method for the given organization
        """
        payment_method = {
  "default" : true,
  "name" : "name",
  "nonce" : "nonce"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/payment-methods'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(payment_method),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_organization(self):
        """Test case for delete_organization

        Delete the organization
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_facilities_by_organization(self):
        """Test case for find_facilities_by_organization

        Retrieve all facilities visible by the organization
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/facilities'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_operating_systems_by_organization(self):
        """Test case for find_operating_systems_by_organization

        Retrieve all operating systems visible by the organization
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/operating-systems'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_by_id(self):
        """Test case for find_organization_by_id

        Retrieve an organization's details
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_customdata(self):
        """Test case for find_organization_customdata

        Retrieve the custom metadata of an organization
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/customdata'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_devices(self):
        """Test case for find_organization_devices

        Retrieve all devices of an organization
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
            '/metal/v1/organizations/{id}/devices'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_events(self):
        """Test case for find_organization_events

        Retrieve organization's events
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
            '/metal/v1/organizations/{id}/events'.format(id='id_example'),
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

    def test_find_organization_payment_methods(self):
        """Test case for find_organization_payment_methods

        Retrieve all payment methods of an organization
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
            '/metal/v1/organizations/{id}/payment-methods'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_projects(self):
        """Test case for find_organization_projects

        Retrieve all projects of an organization
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
            '/metal/v1/organizations/{id}/projects'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_transfers(self):
        """Test case for find_organization_transfers

        Retrieve all project transfer requests from or to an organization
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/transfers'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organizations(self):
        """Test case for find_organizations

        Retrieve all organizations
        """
        query_string = [('personal', 'personal_example'),
                        ('without_projects', 'without_projects_example'),
                        ('include', ['include_example']),
                        ('exclude', ['exclude_example']),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_plans_by_organization(self):
        """Test case for find_plans_by_organization

        Retrieve all plans visible by the organization
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/plans'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_organization(self):
        """Test case for update_organization

        Update the organization
        """
        organization = {
  "website" : "website",
  "twitter" : "twitter",
  "address" : {
    "country" : "country",
    "address" : "address",
    "address2" : "address2",
    "city" : "city",
    "coordinates" : {
      "latitude" : "latitude",
      "longitude" : "longitude"
    },
    "state" : "state",
    "zip_code" : "zip_code"
  },
  "name" : "name",
  "description" : "description",
  "logo" : "",
  "billing_address" : {
    "country" : "country",
    "address" : "address",
    "address2" : "address2",
    "city" : "city",
    "coordinates" : {
      "latitude" : "latitude",
      "longitude" : "longitude"
    },
    "state" : "state",
    "zip_code" : "zip_code"
  },
  "customdata" : "{}",
  "enforce_2fa_at" : "2000-01-23T04:56:07.000+00:00"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(organization),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
