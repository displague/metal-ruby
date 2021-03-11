# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.device import Device  # noqa: E501
from metal.types.hardware_reservation import HardwareReservation  # noqa: E501
from metal.types.hardware_reservation_list import HardwareReservationList  # noqa: E501
from metal.test import BaseTestCase


class TestHardwareReservationsController(BaseTestCase):
    """HardwareReservationsController integration test stubs"""

    def test_find_hardware_reservation_by_id(self):
        """Test case for find_hardware_reservation_by_id

        Retrieve a hardware reservation
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/hardware-reservations/{id}'.format(id='id_example'),
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

    def test_hardware_reservations_id_move_post(self):
        """Test case for hardware_reservations_id_move_post

        Move a hardware reservation
        """
        project_id = 'project_id_example'
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/hardware-reservations/{id}/move'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(project_id),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
