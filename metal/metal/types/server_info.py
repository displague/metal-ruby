# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class ServerInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, facility=None, plan=None, quantity=None):  # noqa: E501
        """ServerInfo - a model defined in OpenAPI

        :param facility: The facility of this ServerInfo.  # noqa: E501
        :type facility: str
        :param plan: The plan of this ServerInfo.  # noqa: E501
        :type plan: str
        :param quantity: The quantity of this ServerInfo.  # noqa: E501
        :type quantity: str
        """
        self.openapi_types = {
            'facility': str,
            'plan': str,
            'quantity': str
        }

        self.attribute_map = {
            'facility': 'facility',
            'plan': 'plan',
            'quantity': 'quantity'
        }

        self._facility = facility
        self._plan = plan
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> 'ServerInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ServerInfo of this ServerInfo.  # noqa: E501
        :rtype: ServerInfo
        """
        return util.deserialize_model(dikt, cls)

    @property
    def facility(self):
        """Gets the facility of this ServerInfo.


        :return: The facility of this ServerInfo.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this ServerInfo.


        :param facility: The facility of this ServerInfo.
        :type facility: str
        """

        self._facility = facility

    @property
    def plan(self):
        """Gets the plan of this ServerInfo.


        :return: The plan of this ServerInfo.
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this ServerInfo.


        :param plan: The plan of this ServerInfo.
        :type plan: str
        """

        self._plan = plan

    @property
    def quantity(self):
        """Gets the quantity of this ServerInfo.


        :return: The quantity of this ServerInfo.
        :rtype: str
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ServerInfo.


        :param quantity: The quantity of this ServerInfo.
        :type quantity: str
        """

        self._quantity = quantity
