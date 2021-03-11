# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class ParentBlock(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, network=None, netmask=None, cidr=None, href=None):  # noqa: E501
        """ParentBlock - a model defined in OpenAPI

        :param network: The network of this ParentBlock.  # noqa: E501
        :type network: str
        :param netmask: The netmask of this ParentBlock.  # noqa: E501
        :type netmask: str
        :param cidr: The cidr of this ParentBlock.  # noqa: E501
        :type cidr: int
        :param href: The href of this ParentBlock.  # noqa: E501
        :type href: str
        """
        self.openapi_types = {
            'network': str,
            'netmask': str,
            'cidr': int,
            'href': str
        }

        self.attribute_map = {
            'network': 'network',
            'netmask': 'netmask',
            'cidr': 'cidr',
            'href': 'href'
        }

        self._network = network
        self._netmask = netmask
        self._cidr = cidr
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'ParentBlock':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ParentBlock of this ParentBlock.  # noqa: E501
        :rtype: ParentBlock
        """
        return util.deserialize_model(dikt, cls)

    @property
    def network(self):
        """Gets the network of this ParentBlock.


        :return: The network of this ParentBlock.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this ParentBlock.


        :param network: The network of this ParentBlock.
        :type network: str
        """

        self._network = network

    @property
    def netmask(self):
        """Gets the netmask of this ParentBlock.


        :return: The netmask of this ParentBlock.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this ParentBlock.


        :param netmask: The netmask of this ParentBlock.
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def cidr(self):
        """Gets the cidr of this ParentBlock.


        :return: The cidr of this ParentBlock.
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this ParentBlock.


        :param cidr: The cidr of this ParentBlock.
        :type cidr: int
        """

        self._cidr = cidr

    @property
    def href(self):
        """Gets the href of this ParentBlock.


        :return: The href of this ParentBlock.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ParentBlock.


        :param href: The href of this ParentBlock.
        :type href: str
        """

        self._href = href