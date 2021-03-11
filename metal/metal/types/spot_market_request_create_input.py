# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.spot_market_request_create_input_instance_attributes import SpotMarketRequestCreateInputInstanceAttributes
from metal import util

from metal.types.spot_market_request_create_input_instance_attributes import SpotMarketRequestCreateInputInstanceAttributes  # noqa: E501

class SpotMarketRequestCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, instance_attributes=None, devices_min=None, devices_max=None, max_bid_price=None, end_at=None, facilities=None):  # noqa: E501
        """SpotMarketRequestCreateInput - a model defined in OpenAPI

        :param instance_attributes: The instance_attributes of this SpotMarketRequestCreateInput.  # noqa: E501
        :type instance_attributes: SpotMarketRequestCreateInputInstanceAttributes
        :param devices_min: The devices_min of this SpotMarketRequestCreateInput.  # noqa: E501
        :type devices_min: int
        :param devices_max: The devices_max of this SpotMarketRequestCreateInput.  # noqa: E501
        :type devices_max: int
        :param max_bid_price: The max_bid_price of this SpotMarketRequestCreateInput.  # noqa: E501
        :type max_bid_price: float
        :param end_at: The end_at of this SpotMarketRequestCreateInput.  # noqa: E501
        :type end_at: datetime
        :param facilities: The facilities of this SpotMarketRequestCreateInput.  # noqa: E501
        :type facilities: List[str]
        """
        self.openapi_types = {
            'instance_attributes': SpotMarketRequestCreateInputInstanceAttributes,
            'devices_min': int,
            'devices_max': int,
            'max_bid_price': float,
            'end_at': datetime,
            'facilities': List[str]
        }

        self.attribute_map = {
            'instance_attributes': 'instance_attributes',
            'devices_min': 'devices_min',
            'devices_max': 'devices_max',
            'max_bid_price': 'max_bid_price',
            'end_at': 'end_at',
            'facilities': 'facilities'
        }

        self._instance_attributes = instance_attributes
        self._devices_min = devices_min
        self._devices_max = devices_max
        self._max_bid_price = max_bid_price
        self._end_at = end_at
        self._facilities = facilities

    @classmethod
    def from_dict(cls, dikt) -> 'SpotMarketRequestCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SpotMarketRequestCreateInput of this SpotMarketRequestCreateInput.  # noqa: E501
        :rtype: SpotMarketRequestCreateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def instance_attributes(self):
        """Gets the instance_attributes of this SpotMarketRequestCreateInput.


        :return: The instance_attributes of this SpotMarketRequestCreateInput.
        :rtype: SpotMarketRequestCreateInputInstanceAttributes
        """
        return self._instance_attributes

    @instance_attributes.setter
    def instance_attributes(self, instance_attributes):
        """Sets the instance_attributes of this SpotMarketRequestCreateInput.


        :param instance_attributes: The instance_attributes of this SpotMarketRequestCreateInput.
        :type instance_attributes: SpotMarketRequestCreateInputInstanceAttributes
        """

        self._instance_attributes = instance_attributes

    @property
    def devices_min(self):
        """Gets the devices_min of this SpotMarketRequestCreateInput.


        :return: The devices_min of this SpotMarketRequestCreateInput.
        :rtype: int
        """
        return self._devices_min

    @devices_min.setter
    def devices_min(self, devices_min):
        """Sets the devices_min of this SpotMarketRequestCreateInput.


        :param devices_min: The devices_min of this SpotMarketRequestCreateInput.
        :type devices_min: int
        """

        self._devices_min = devices_min

    @property
    def devices_max(self):
        """Gets the devices_max of this SpotMarketRequestCreateInput.


        :return: The devices_max of this SpotMarketRequestCreateInput.
        :rtype: int
        """
        return self._devices_max

    @devices_max.setter
    def devices_max(self, devices_max):
        """Sets the devices_max of this SpotMarketRequestCreateInput.


        :param devices_max: The devices_max of this SpotMarketRequestCreateInput.
        :type devices_max: int
        """

        self._devices_max = devices_max

    @property
    def max_bid_price(self):
        """Gets the max_bid_price of this SpotMarketRequestCreateInput.


        :return: The max_bid_price of this SpotMarketRequestCreateInput.
        :rtype: float
        """
        return self._max_bid_price

    @max_bid_price.setter
    def max_bid_price(self, max_bid_price):
        """Sets the max_bid_price of this SpotMarketRequestCreateInput.


        :param max_bid_price: The max_bid_price of this SpotMarketRequestCreateInput.
        :type max_bid_price: float
        """

        self._max_bid_price = max_bid_price

    @property
    def end_at(self):
        """Gets the end_at of this SpotMarketRequestCreateInput.


        :return: The end_at of this SpotMarketRequestCreateInput.
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this SpotMarketRequestCreateInput.


        :param end_at: The end_at of this SpotMarketRequestCreateInput.
        :type end_at: datetime
        """

        self._end_at = end_at

    @property
    def facilities(self):
        """Gets the facilities of this SpotMarketRequestCreateInput.


        :return: The facilities of this SpotMarketRequestCreateInput.
        :rtype: List[str]
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this SpotMarketRequestCreateInput.


        :param facilities: The facilities of this SpotMarketRequestCreateInput.
        :type facilities: List[str]
        """

        self._facilities = facilities