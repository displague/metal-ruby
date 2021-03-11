# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.operating_system import OperatingSystem  # noqa: E501
from metal.test import BaseTestCase


class TestOperatingSystemsController(BaseTestCase):
    """OperatingSystemsController integration test stubs"""

    def test_find_operating_systems(self):
        """Test case for find_operating_systems

        Retrieve all operating systems
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/operating-systems',
            method='GET',
            headers=headers)
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


if __name__ == '__main__':
    unittest.main()
