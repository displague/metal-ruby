# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.spot_market_request import SpotMarketRequest  # noqa: E501
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput  # noqa: E501
from metal.types.spot_market_request_list import SpotMarketRequestList  # noqa: E501
from metal.test import BaseTestCase


class TestSpotMarketRequestController(BaseTestCase):
    """SpotMarketRequestController integration test stubs"""

    def test_create_spot_market_request(self):
        """Test case for create_spot_market_request

        Create a spot market request
        """
        spot_market_request = {
  "end_at" : "2000-01-23T04:56:07.000+00:00",
  "instance_attributes" : {
    "user_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "private_ipv4_subnet_size" : 6,
    "description" : "description",
    "hostnames" : [ "hostnames", "hostnames" ],
    "termination_time" : "2000-01-23T04:56:07.000+00:00",
    "tags" : [ "tags", "tags" ],
    "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "userdata" : "userdata",
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "public_ipv4_subnet_size" : 0,
    "operating_system" : "operating_system",
    "billing_cycle" : "billing_cycle",
    "always_pxe" : true,
    "customdata" : "{}",
    "locked" : true,
    "plan" : "plan"
  },
  "devices_min" : 1,
  "devices_max" : 5,
  "max_bid_price" : 5.637377,
  "facilities" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/spot-market-requests'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(spot_market_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_spot_market_request(self):
        """Test case for delete_spot_market_request

        Delete the spot market request
        """
        query_string = [('force_termination', True)]
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/spot-market-requests/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_spot_market_request_by_id(self):
        """Test case for find_spot_market_request_by_id

        Retrieve a spot market request
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/spot-market-requests/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_spot_market_requests(self):
        """Test case for list_spot_market_requests

        List spot market requests
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/spot-market-requests'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
