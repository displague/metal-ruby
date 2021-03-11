# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.staff_hardware import StaffHardware  # noqa: E501
from metal.types.staff_hardware_create_input import StaffHardwareCreateInput  # noqa: E501
from metal.types.staff_hardware_list import StaffHardwareList  # noqa: E501
from metal.types.staff_hardware_update_input import StaffHardwareUpdateInput  # noqa: E501
from metal.test import BaseTestCase


class TestStaffHardwareController(BaseTestCase):
    """StaffHardwareController integration test stubs"""

    def test_staff_create_server_rack_hardware(self):
        """Test case for staff_create_server_rack_hardware

        Create hardware for server rack
        """
        hardware = metal.StaffHardwareCreateInput()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/staff/server-rack/{id}/hardware'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(hardware),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_staff_delete_hardware_metadata(self):
        """Test case for staff_delete_hardware_metadata

        Delete metadata for hardware
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/staff/hardware/{id}/metadata'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_staff_find_hardware_by_id(self):
        """Test case for staff_find_hardware_by_id

        Retrieve hardware
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/staff/hardware/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_staff_find_server_rack_hardware(self):
        """Test case for staff_find_server_rack_hardware

        Retrieve all hardware for server rack
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
            '/metal/v1/staff/server-rack/{id}/hardware'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_staff_update_hardware(self):
        """Test case for staff_update_hardware

        Update hardware
        """
        hardware = metal.StaffHardwareUpdateInput()
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/staff/hardware/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(hardware),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_staff_update_hardware_provisioner(self):
        """Test case for staff_update_hardware_provisioner

        Update provisioner for hardware
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/staff/hardware/{id}/update-provisioner'.format(id='id_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
