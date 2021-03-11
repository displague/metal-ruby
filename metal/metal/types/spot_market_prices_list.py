# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.spot_prices_report import SpotPricesReport
from metal import util

from metal.types.spot_prices_report import SpotPricesReport  # noqa: E501

class SpotMarketPricesList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, spot_market_prices=None):  # noqa: E501
        """SpotMarketPricesList - a model defined in OpenAPI

        :param spot_market_prices: The spot_market_prices of this SpotMarketPricesList.  # noqa: E501
        :type spot_market_prices: SpotPricesReport
        """
        self.openapi_types = {
            'spot_market_prices': SpotPricesReport
        }

        self.attribute_map = {
            'spot_market_prices': 'spot_market_prices'
        }

        self._spot_market_prices = spot_market_prices

    @classmethod
    def from_dict(cls, dikt) -> 'SpotMarketPricesList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpotMarketPricesList of this SpotMarketPricesList.  # noqa: E501
        :rtype: SpotMarketPricesList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def spot_market_prices(self):
        """Gets the spot_market_prices of this SpotMarketPricesList.


        :return: The spot_market_prices of this SpotMarketPricesList.
        :rtype: SpotPricesReport
        """
        return self._spot_market_prices

    @spot_market_prices.setter
    def spot_market_prices(self, spot_market_prices):
        """Sets the spot_market_prices of this SpotMarketPricesList.


        :param spot_market_prices: The spot_market_prices of this SpotMarketPricesList.
        :type spot_market_prices: SpotPricesReport
        """

        self._spot_market_prices = spot_market_prices