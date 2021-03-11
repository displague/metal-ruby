# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.batches_list import BatchesList  # noqa: E501
from metal.types.bgp_config import BgpConfig  # noqa: E501
from metal.types.bgp_config_request_input import BgpConfigRequestInput  # noqa: E501
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.types.device import Device  # noqa: E501
from metal.types.device_create_input import DeviceCreateInput  # noqa: E501
from metal.types.device_list import DeviceList  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal.types.facility_list import FacilityList  # noqa: E501
from metal.types.hardware_reservation_list import HardwareReservationList  # noqa: E501
from metal.types.ip_reservation import IPReservation  # noqa: E501
from metal.types.ip_reservation_list import IPReservationList  # noqa: E501
from metal.types.ip_reservation_request_input import IPReservationRequestInput  # noqa: E501
from metal.types.invitation import Invitation  # noqa: E501
from metal.types.invitation_input import InvitationInput  # noqa: E501
from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.license import License  # noqa: E501
from metal.types.license_create_input import LicenseCreateInput  # noqa: E501
from metal.types.license_list import LicenseList  # noqa: E501
from metal.types.membership_list import MembershipList  # noqa: E501
from metal.types.plan_list import PlanList  # noqa: E501
from metal.types.project import Project  # noqa: E501
from metal.types.project_create_from_root_input import ProjectCreateFromRootInput  # noqa: E501
from metal.types.project_create_input import ProjectCreateInput  # noqa: E501
from metal.types.project_list import ProjectList  # noqa: E501
from metal.types.project_update_input import ProjectUpdateInput  # noqa: E501
from metal.types.ssh_key import SSHKey  # noqa: E501
from metal.types.ssh_key_input import SSHKeyInput  # noqa: E501
from metal.types.ssh_key_list import SSHKeyList  # noqa: E501
from metal.types.spot_market_request import SpotMarketRequest  # noqa: E501
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput  # noqa: E501
from metal.types.spot_market_request_list import SpotMarketRequestList  # noqa: E501
from metal.types.transfer_request import TransferRequest  # noqa: E501
from metal.types.transfer_request_input import TransferRequestInput  # noqa: E501
from metal.types.virtual_network import VirtualNetwork  # noqa: E501
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput  # noqa: E501
from metal.types.virtual_network_list import VirtualNetworkList  # noqa: E501
from metal.test import BaseTestCase


class TestProjectsController(BaseTestCase):
    """ProjectsController integration test stubs"""

    def test_create_device(self):
        """Test case for create_device

        Create a device
        """
        device = {
  "user_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
  "ip_addresses" : [ {
    "address_family" : 4.0,
    "public" : false,
    "ip_reservations" : [ "ip_reservations", "ip_reservations" ],
    "cidr" : 28.0
  }, {
    "address_family" : 4.0,
    "public" : false,
    "ip_reservations" : [ "ip_reservations", "ip_reservations" ],
    "cidr" : 28.0
  } ],
  "private_ipv4_subnet_size" : 1.4658129805029452,
  "description" : "description",
  "termination_time" : "2000-01-23T04:56:07.000+00:00",
  "tags" : [ "tags", "tags" ],
  "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
  "userdata" : "userdata",
  "features" : [ "features", "features" ],
  "hostname" : "hostname",
  "spot_instance" : true,
  "public_ipv4_subnet_size" : 6.027456183070403,
  "hardware_reservation_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "operating_system" : "operating_system",
  "billing_cycle" : "billing_cycle",
  "always_pxe" : true,
  "ipxe_script_url" : "ipxe_script_url",
  "customdata" : "{}",
  "locked" : true,
  "spot_price_max" : 0.8008282,
  "facility" : "facility",
  "plan" : "plan"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/devices'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(device),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_license(self):
        """Test case for create_license

        Create a License
        """
        license = {
  "size" : 0.8008281904610115,
  "licensee_product_id" : "licensee_product_id",
  "description" : "description"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/licenses'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(license),
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

    def test_create_project(self):
        """Test case for create_project

        Create a project
        """
        project = {
  "payment_method_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "organization_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "name" : "name",
  "customdata" : "{}"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects',
            method='POST',
            headers=headers,
            data=json.dumps(project),
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

    def test_create_spot_market_request(self):
        """Test case for create_spot_market_request

        Create a spot market request
        """
        spot_market_request = {
  "end_at" : "2000-01-23T04:56:07.000+00:00",
  "instance_attributes" : {
    "user_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "private_ipv4_subnet_size" : 6,
    "description" : "description",
    "hostnames" : [ "hostnames", "hostnames" ],
    "termination_time" : "2000-01-23T04:56:07.000+00:00",
    "tags" : [ "tags", "tags" ],
    "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "userdata" : "userdata",
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "public_ipv4_subnet_size" : 0,
    "operating_system" : "operating_system",
    "billing_cycle" : "billing_cycle",
    "always_pxe" : true,
    "customdata" : "{}",
    "locked" : true,
    "plan" : "plan"
  },
  "devices_min" : 1,
  "devices_max" : 5,
  "max_bid_price" : 5.637377,
  "facilities" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/spot-market-requests'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(spot_market_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_transfer_request(self):
        """Test case for create_transfer_request

        Create a transfer request
        """
        transfer_request = {
  "target_organization_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/transfers'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(transfer_request),
            content_type='application/json')
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

    def test_delete_project(self):
        """Test case for delete_project

        Delete the project
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_batches_by_project(self):
        """Test case for find_batches_by_project

        Retrieve all batches by project
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/batches'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
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

    def test_find_facilities_by_project(self):
        """Test case for find_facilities_by_project

        Retrieve all facilities visible by the project
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/facilities'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ip_reservation_customdata(self):
        """Test case for find_ip_reservation_customdata

        Retrieve the custom metadata of an IP Reservation
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{project_id}/ips/{id}/customdata'.format(project_id='project_id_example', id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ip_reservations(self):
        """Test case for find_ip_reservations

        Retrieve all ip reservations
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/ips'.format(id='id_example'),
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

    def test_find_plans_by_project(self):
        """Test case for find_plans_by_project

        Retrieve all plans visible by the project
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/plans'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
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

    def test_find_project_by_id(self):
        """Test case for find_project_by_id

        Retrieve a project
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_customdata(self):
        """Test case for find_project_customdata

        Retrieve the custom metadata of a project
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/customdata'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_devices(self):
        """Test case for find_project_devices

        Retrieve all devices of a project
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
            '/metal/v1/projects/{id}/devices'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_events(self):
        """Test case for find_project_events

        Retrieve project's events
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
            '/metal/v1/projects/{id}/events'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_hardware_reservations(self):
        """Test case for find_project_hardware_reservations

        Retrieve all hardware reservations for a given project
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
            '/metal/v1/projects/{id}/hardware-reservations'.format(id='id_example'),
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

    def test_find_project_licenses(self):
        """Test case for find_project_licenses

        Retrieve all licenses
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
            '/metal/v1/projects/{id}/licenses'.format(id='id_example'),
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

    def test_find_projects(self):
        """Test case for find_projects

        Retrieve all projects
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
            '/metal/v1/projects',
            method='GET',
            headers=headers,
            query_string=query_string)
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

    def test_list_spot_market_requests(self):
        """Test case for list_spot_market_requests

        List spot market requests
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/spot-market-requests'.format(id='id_example'),
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

    def test_request_ip_reservation(self):
        """Test case for request_ip_reservation

        Requesting IP reservations
        """
        ip_reservation_request = {
  "fail_on_approval_required" : true,
  "quantity" : 0,
  "comments" : "comments",
  "details" : "details",
  "customdata" : "{}",
  "type" : "type",
  "facility" : "facility",
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/ips'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(ip_reservation_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_project(self):
        """Test case for update_project

        Update the project
        """
        project = {
  "payment_method_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91",
  "name" : "name",
  "backend_transfer_enabled" : true,
  "customdata" : "{}"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(project),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
