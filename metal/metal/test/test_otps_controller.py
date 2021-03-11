# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.recovery_code_list import RecoveryCodeList  # noqa: E501
from metal.test import BaseTestCase


class TestOtpsController(BaseTestCase):
    """OtpsController integration test stubs"""

    def test_find_ensure_otp(self):
        """Test case for find_ensure_otp

        Verify user by providing an OTP
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/verify/{otp}'.format(otp='otp_example'),
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_recovery_codes(self):
        """Test case for find_recovery_codes

        Retrieve my recovery codes
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/recovery-codes',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_receive_codes(self):
        """Test case for receive_codes

        Receive an OTP per sms
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/sms/receive',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_regenerate_codes(self):
        """Test case for regenerate_codes

        Generate new recovery codes
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/user/otp/recovery-codes',
            method='POST',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
