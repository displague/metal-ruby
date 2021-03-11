# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.ip_assignment import IPAssignment
from metal import util

from metal.types.ip_assignment import IPAssignment  # noqa: E501

class IPAssignmentList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ip_addresses=None):  # noqa: E501
        """IPAssignmentList - a model defined in OpenAPI

        :param ip_addresses: The ip_addresses of this IPAssignmentList.  # noqa: E501
        :type ip_addresses: List[IPAssignment]
        """
        self.openapi_types = {
            'ip_addresses': List[IPAssignment]
        }

        self.attribute_map = {
            'ip_addresses': 'ip_addresses'
        }

        self._ip_addresses = ip_addresses

    @classmethod
    def from_dict(cls, dikt) -> 'IPAssignmentList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The IPAssignmentList of this IPAssignmentList.  # noqa: E501
        :rtype: IPAssignmentList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this IPAssignmentList.


        :return: The ip_addresses of this IPAssignmentList.
        :rtype: List[IPAssignment]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this IPAssignmentList.


        :param ip_addresses: The ip_addresses of this IPAssignmentList.
        :type ip_addresses: List[IPAssignment]
        """

        self._ip_addresses = ip_addresses
