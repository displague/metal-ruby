# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.operating_system import OperatingSystem  # noqa: E501
from metal.test import BaseTestCase


class TestOperatingSystemVersionsController(BaseTestCase):
    """OperatingSystemVersionsController integration test stubs"""

    def test_find_operating_system_version(self):
        """Test case for find_operating_system_version

        Retrieve all operating system versions
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/operating-system-versions',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
