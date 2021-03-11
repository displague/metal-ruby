# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.device_usage_list import DeviceUsageList  # noqa: E501
from metal.types.project_usage_list import ProjectUsageList  # noqa: E501
from metal.test import BaseTestCase


class TestUsagesController(BaseTestCase):
    """UsagesController integration test stubs"""

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


if __name__ == '__main__':
    unittest.main()
