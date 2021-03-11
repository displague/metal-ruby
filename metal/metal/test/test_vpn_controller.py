# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.vpn_config import VPNConfig  # noqa: E501
from metal.test import BaseTestCase


class TestVPNController(BaseTestCase):
    """VPNController integration test stubs"""

    def test_find_current_user_vpn_config(self):
        """Test case for find_current_user_vpn_config

        Retrieve the client vpn config for current user
        """
        query_string = [('code', 'code_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/vpn',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_turn_off_current_user_vpn(self):
        """Test case for turn_off_current_user_vpn

        Turn off vpn for the current user
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/vpn',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_turn_on_current_user_vpn(self):
        """Test case for turn_on_current_user_vpn

        Turn on vpn for the current user
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/vpn',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
