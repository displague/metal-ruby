# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.test import BaseTestCase


class TestTwoFactorAuthController(BaseTestCase):
    """TwoFactorAuthController integration test stubs"""

    def test_disable_tfa_app(self):
        """Test case for disable_tfa_app

        Disable two factor authentication
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/app',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_disable_tfa_sms(self):
        """Test case for disable_tfa_sms

        Disable two factor authentication
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/sms',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_enable_tfa_app(self):
        """Test case for enable_tfa_app

        Enable two factor auth using app
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/app',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_enable_tfa_sms(self):
        """Test case for enable_tfa_sms

        Enable two factor auth using sms
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/sms',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
