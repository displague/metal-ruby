# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import metal
from metal.types.spot_market_request_list import SpotMarketRequestList  # noqa: E501
from metal.rest import ApiException

class TestSpotMarketRequestList(unittest.TestCase):
    """SpotMarketRequestList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SpotMarketRequestList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.spot_market_request_list.SpotMarketRequestList()  # noqa: E501
        if include_optional :
            return SpotMarketRequestList(
                spot_market_requests = [
                    metal.models.spot_market_request.SpotMarketRequest(
                        id = '', 
                        devices_min = 56, 
                        devices_max = 56, 
                        max_bid_price = 1.337, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        end_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        href = '', 
                        facilities = metal.models.href.Href(
                            href = '', ), 
                        project = metal.models.href.Href(
                            href = '', ), 
                        instances = metal.models.href.Href(
                            href = '', ), )
                    ]
            )
        else :
            return SpotMarketRequestList(
        )

    def testSpotMarketRequestList(self):
        """Test SpotMarketRequestList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
