# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.spot_market_prices_list import SpotMarketPricesList  # noqa: E501
from metal.types.spot_prices_history_report import SpotPricesHistoryReport  # noqa: E501
from metal.test import BaseTestCase


class TestMarketController(BaseTestCase):
    """MarketController integration test stubs"""

    def test_find_spot_market_prices(self):
        """Test case for find_spot_market_prices

        Get current spot market prices
        """
        query_string = [('facility', 'facility_example'),
                        ('plan', 'plan_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/market/spot/prices',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_spot_market_prices_history(self):
        """Test case for find_spot_market_prices_history

        Get spot market prices for a given period of time
        """
        query_string = [('facility', 'facility_example'),
                        ('plan', 'plan_example'),
                        ('from', '_from_example'),
                        ('until', 'until_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/market/spot/prices/history',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
