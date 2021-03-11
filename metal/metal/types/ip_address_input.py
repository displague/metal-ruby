# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class IpAddressInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address_family=None):  # noqa: E501
        """IpAddressInput - a model defined in OpenAPI

        :param address_family: The address_family of this IpAddressInput.  # noqa: E501
        :type address_family: float
        """
        self.openapi_types = {
            'address_family': float
        }

        self.attribute_map = {
            'address_family': 'address_family'
        }

        self._address_family = address_family

    @classmethod
    def from_dict(cls, dikt) -> 'IpAddressInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IpAddressInput of this IpAddressInput.  # noqa: E501
        :rtype: IpAddressInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address_family(self):
        """Gets the address_family of this IpAddressInput.

        Address Family for IP Address  # noqa: E501

        :return: The address_family of this IpAddressInput.
        :rtype: float
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this IpAddressInput.

        Address Family for IP Address  # noqa: E501

        :param address_family: The address_family of this IpAddressInput.
        :type address_family: float
        """

        self._address_family = address_family