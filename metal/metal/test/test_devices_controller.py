# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.bgp_session_input import BGPSessionInput  # noqa: E501
from metal.types.batches_list import BatchesList  # noqa: E501
from metal.types.bgp_session import BgpSession  # noqa: E501
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.types.bgp_session_neighbors import BgpSessionNeighbors  # noqa: E501
from metal.types.device import Device  # noqa: E501
from metal.types.device_create_input import DeviceCreateInput  # noqa: E501
from metal.types.device_list import DeviceList  # noqa: E501
from metal.types.device_update_input import DeviceUpdateInput  # noqa: E501
from metal.types.device_usage_list import DeviceUsageList  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal.types.ip_assignment import IPAssignment  # noqa: E501
from metal.types.ip_assignment_input import IPAssignmentInput  # noqa: E501
from metal.types.ip_assignment_list import IPAssignmentList  # noqa: E501
from metal.types.instances_batch_create_input import InstancesBatchCreateInput  # noqa: E501
from metal.types.project_usage_list import ProjectUsageList  # noqa: E501
from metal.types.timeframe import Timeframe  # noqa: E501
from metal.test import BaseTestCase


class TestDevicesController(BaseTestCase):
    """DevicesController integration test stubs"""

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

    def test_create_device_batch(self):
        """Test case for create_device_batch

        Create a devices batch
        """
        batch = {
  "batches" : [ {
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
    "description" : "description",
    "hostnames" : [ "hostnames", "hostnames" ],
    "termination_time" : "2000-01-23T04:56:07.000+00:00",
    "tags" : [ "tags", "tags" ],
    "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "userdata" : "userdata",
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "operating_system" : "operating_system",
    "billing_cycle" : "billing_cycle",
    "always_pxe" : true,
    "customdata" : "{}",
    "locked" : true,
    "plan" : "plan"
  }, {
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
    "description" : "description",
    "hostnames" : [ "hostnames", "hostnames" ],
    "termination_time" : "2000-01-23T04:56:07.000+00:00",
    "tags" : [ "tags", "tags" ],
    "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "userdata" : "userdata",
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "operating_system" : "operating_system",
    "billing_cycle" : "billing_cycle",
    "always_pxe" : true,
    "customdata" : "{}",
    "locked" : true,
    "plan" : "plan"
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/devices/batch'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(batch),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_ip_assignment(self):
        """Test case for create_ip_assignment

        Create a ip assignment
        """
        ip_assignment = {
  "address" : "address",
  "customdata" : "{}",
  "manageable" : true
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/ips'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(ip_assignment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_device(self):
        """Test case for delete_device

        Delete the device
        """
        query_string = [('force_delete', True)]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}'.format(id='id_example'),
            method='DELETE',
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

    def test_find_device_by_id(self):
        """Test case for find_device_by_id

        Retrieve a device
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_device_customdata(self):
        """Test case for find_device_customdata

        Retrieve the custom metadata of an instance
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/customdata'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_device_events(self):
        """Test case for find_device_events

        Retrieve device's events
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
            '/metal/v1/devices/{id}/events'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_device_usages(self):
        """Test case for find_device_usages

        Retrieve all usages for device
        """
        query_string = [('created[after]', 'created_after_example'),
                        ('created[before]', 'created_before_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/usages'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_instance_bandwidth(self):
        """Test case for find_instance_bandwidth

        Retrieve an instance bandwidth
        """
        query_string = [('from', '_from_example'),
                        ('until', 'until_example')]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/bandwidth'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ip_assignment_customdata(self):
        """Test case for find_ip_assignment_customdata

        Retrieve the custom metadata of an IP Assignment
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{instance_id}/ips/{id}/customdata'.format(instance_id='instance_id_example', id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ip_assignments(self):
        """Test case for find_ip_assignments

        Retrieve all ip assignments
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/ips'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
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

    def test_find_project_usage(self):
        """Test case for find_project_usage

        Retrieve all usages for project
        """
        query_string = [('created[after]', 'created_after_example'),
                        ('created[before]', 'created_before_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/usages'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_traffic(self):
        """Test case for find_traffic

        Retrieve device traffic
        """
        timeframe = {
  "started_at" : "2000-01-23T04:56:07.000+00:00",
  "ended_at" : "2000-01-23T04:56:07.000+00:00"
}
        query_string = [('direction', 'direction_example'),
                        ('interval', 'interval_example'),
                        ('bucket', 'bucket_example')]
        headers = { 
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/traffic'.format(id='id_example'),
            method='GET',
            headers=headers,
            data=json.dumps(timeframe),
            content_type='application/json',
            query_string=query_string)
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

    def test_perform_action(self):
        """Test case for perform_action

        Perform an action
        """
        query_string = [('type', 'type_example')]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}/actions'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_device(self):
        """Test case for update_device

        Update the device
        """
        device = {
  "userdata" : "userdata",
  "hostname" : "hostname",
  "spot_instance" : true,
  "description" : "description",
  "billing_cycle" : "billing_cycle",
  "always_pxe" : true,
  "ipxe_script_url" : "ipxe_script_url",
  "customdata" : "{}",
  "locked" : true,
  "tags" : [ "tags", "tags" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/devices/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(device),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
