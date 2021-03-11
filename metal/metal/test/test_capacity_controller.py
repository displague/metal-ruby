# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.capacity_check_per_facility_list import CapacityCheckPerFacilityList  # noqa: E501
from metal.types.capacity_input import CapacityInput  # noqa: E501
from metal.types.capacity_list import CapacityList  # noqa: E501
from metal.test import BaseTestCase


class TestCapacityController(BaseTestCase):
    """CapacityController integration test stubs"""

    def test_check_capacity_for_facility(self):
        """Test case for check_capacity_for_facility

        Check capacity
        """
        facility = {
  "servers" : [ {
    "quantity" : "quantity",
    "facility" : "facility",
    "plan" : "plan"
  }, {
    "quantity" : "quantity",
    "facility" : "facility",
    "plan" : "plan"
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/capacity',
            method='POST',
            headers=headers,
            data=json.dumps(facility),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_capacity_for_facility(self):
        """Test case for find_capacity_for_facility

        View capacity
        """
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/capacity',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
