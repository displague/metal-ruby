# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.internet_gateway import InternetGateway  # noqa: E501
from metal.test import BaseTestCase


class TestInternetGatewaysController(BaseTestCase):
    """InternetGatewaysController integration test stubs"""

    def test_create_internet_gateway(self):
        """Test case for create_internet_gateway

        Create an internet gateway
        """
        query_string = [('length', 'length_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/virtual-networks/{id}/internet-gateways'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
