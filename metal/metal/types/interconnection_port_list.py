# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.interconnection_port import InterconnectionPort
from metal import util

from metal.types.interconnection_port import InterconnectionPort  # noqa: E501

class InterconnectionPortList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ports=None):  # noqa: E501
        """InterconnectionPortList - a model defined in OpenAPI

        :param ports: The ports of this InterconnectionPortList.  # noqa: E501
        :type ports: List[InterconnectionPort]
        """
        self.openapi_types = {
            'ports': List[InterconnectionPort]
        }

        self.attribute_map = {
            'ports': 'ports'
        }

        self._ports = ports

    @classmethod
    def from_dict(cls, dikt) -> 'InterconnectionPortList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InterconnectionPortList of this InterconnectionPortList.  # noqa: E501
        :rtype: InterconnectionPortList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ports(self):
        """Gets the ports of this InterconnectionPortList.


        :return: The ports of this InterconnectionPortList.
        :rtype: List[InterconnectionPort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """Sets the ports of this InterconnectionPortList.


        :param ports: The ports of this InterconnectionPortList.
        :type ports: List[InterconnectionPort]
        """

        self._ports = ports