# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.test import BaseTestCase


class TestUserVerificationTokensController(BaseTestCase):
    """UserVerificationTokensController integration test stubs"""

    def test_consume_verification_request(self):
        """Test case for consume_verification_request

        Verify a user using an email verification token
        """
        query_string = [('token', 'token_example')]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/verify-email',
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_validation_request(self):
        """Test case for create_validation_request

        Create an email verification request
        """
        query_string = [('login', 'login_example')]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/verify-email',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
