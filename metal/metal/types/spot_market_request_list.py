# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.spot_market_request import SpotMarketRequest
from metal import util

from metal.types.spot_market_request import SpotMarketRequest  # noqa: E501

class SpotMarketRequestList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, spot_market_requests=None):  # noqa: E501
        """SpotMarketRequestList - a model defined in OpenAPI

        :param spot_market_requests: The spot_market_requests of this SpotMarketRequestList.  # noqa: E501
        :type spot_market_requests: List[SpotMarketRequest]
        """
        self.openapi_types = {
            'spot_market_requests': List[SpotMarketRequest]
        }

        self.attribute_map = {
            'spot_market_requests': 'spot_market_requests'
        }

        self._spot_market_requests = spot_market_requests

    @classmethod
    def from_dict(cls, dikt) -> 'SpotMarketRequestList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpotMarketRequestList of this SpotMarketRequestList.  # noqa: E501
        :rtype: SpotMarketRequestList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def spot_market_requests(self):
        """Gets the spot_market_requests of this SpotMarketRequestList.


        :return: The spot_market_requests of this SpotMarketRequestList.
        :rtype: List[SpotMarketRequest]
        """
        return self._spot_market_requests

    @spot_market_requests.setter
    def spot_market_requests(self, spot_market_requests):
        """Sets the spot_market_requests of this SpotMarketRequestList.


        :param spot_market_requests: The spot_market_requests of this SpotMarketRequestList.
        :type spot_market_requests: List[SpotMarketRequest]
        """

        self._spot_market_requests = spot_market_requests