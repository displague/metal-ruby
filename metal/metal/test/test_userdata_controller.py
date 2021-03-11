# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.test import BaseTestCase


class TestUserdataController(BaseTestCase):
    """UserdataController integration test stubs"""

    def test_validate_userdata(self):
        """Test case for validate_userdata

        Validate user data
        """
        query_string = [('userdata', 'userdata_example')]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/userdata/validate',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
