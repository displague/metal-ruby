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

import metal
from models.market_api import MarketApi  # noqa: E501
from metal.rest import ApiException


class TestMarketApi(unittest.TestCase):
    """MarketApi unit test stubs"""

    def setUp(self):
        self.api = models.market_api.MarketApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_find_spot_market_prices(self):
        """Test case for find_spot_market_prices

        Get current spot market prices  # noqa: E501
        """
        pass

    def test_find_spot_market_prices_history(self):
        """Test case for find_spot_market_prices_history

        Get spot market prices for a given period of time  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()