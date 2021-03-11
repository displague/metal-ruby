# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.regions_list import RegionsList  # noqa: E501
from metal.test import BaseTestCase


class TestRegionsController(BaseTestCase):
    """RegionsController integration test stubs"""

    def test_find_regions(self):
        """Test case for find_regions

        Retrieve all regions
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example']),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/regions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
