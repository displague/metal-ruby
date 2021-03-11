# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.ip_assignment import IPAssignment  # noqa: E501
from metal.types.ip_assignment_input import IPAssignmentInput  # noqa: E501
from metal.types.ip_assignment_list import IPAssignmentList  # noqa: E501
from metal.types.ip_availabilities_list import IPAvailabilitiesList  # noqa: E501
from metal.types.ip_reservation import IPReservation  # noqa: E501
from metal.types.ip_reservation_list import IPReservationList  # noqa: E501
from metal.types.ip_reservation_request_input import IPReservationRequestInput  # noqa: E501
from metal.test import BaseTestCase


class TestIPAddressesController(BaseTestCase):
    """IPAddressesController integration test stubs"""

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

    def test_delete_ip_address(self):
        """Test case for delete_ip_address

        Unassign an ip address
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ips/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ip_address_by_id(self):
        """Test case for find_ip_address_by_id

        Retrieve an ip address
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ips/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_ip_address_customdata(self):
        """Test case for find_ip_address_customdata

        Retrieve the custom metadata of an IP Reservation or IP Assignment
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ips/{id}/customdata'.format(id='id_example'),
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

    def test_find_ip_availabilities(self):
        """Test case for find_ip_availabilities

        Retrieve all available subnets of a particular reservation
        """
        query_string = [('cidr', 'cidr_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/ips/{id}/available'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
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


if __name__ == '__main__':
    unittest.main()
