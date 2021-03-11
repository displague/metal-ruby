# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.new_password import NewPassword  # noqa: E501
from metal.test import BaseTestCase


class TestPasswordResetTokensController(BaseTestCase):
    """PasswordResetTokensController integration test stubs"""

    def test_create_password_reset_token(self):
        """Test case for create_password_reset_token

        Create a password reset token
        """
        query_string = [('email', 'email_example')]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/reset-password',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_reset_password(self):
        """Test case for reset_password

        Reset current user password
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/reset-password',
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
