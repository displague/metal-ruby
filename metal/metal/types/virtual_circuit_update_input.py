# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class VirtualCircuitUpdateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, name=None, speed=None, tags=None, vnid=None):  # noqa: E501
        """VirtualCircuitUpdateInput - a model defined in OpenAPI

        :param description: The description of this VirtualCircuitUpdateInput.  # noqa: E501
        :type description: str
        :param name: The name of this VirtualCircuitUpdateInput.  # noqa: E501
        :type name: str
        :param speed: The speed of this VirtualCircuitUpdateInput.  # noqa: E501
        :type speed: str
        :param tags: The tags of this VirtualCircuitUpdateInput.  # noqa: E501
        :type tags: List[str]
        :param vnid: The vnid of this VirtualCircuitUpdateInput.  # noqa: E501
        :type vnid: str
        """
        self.openapi_types = {
            'description': str,
            'name': str,
            'speed': str,
            'tags': List[str],
            'vnid': str
        }

        self.attribute_map = {
            'description': 'description',
            'name': 'name',
            'speed': 'speed',
            'tags': 'tags',
            'vnid': 'vnid'
        }

        self._description = description
        self._name = name
        self._speed = speed
        self._tags = tags
        self._vnid = vnid

    @classmethod
    def from_dict(cls, dikt) -> 'VirtualCircuitUpdateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VirtualCircuitUpdateInput of this VirtualCircuitUpdateInput.  # noqa: E501
        :rtype: VirtualCircuitUpdateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this VirtualCircuitUpdateInput.


        :return: The description of this VirtualCircuitUpdateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualCircuitUpdateInput.


        :param description: The description of this VirtualCircuitUpdateInput.
        :type description: str
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this VirtualCircuitUpdateInput.


        :return: The name of this VirtualCircuitUpdateInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VirtualCircuitUpdateInput.


        :param name: The name of this VirtualCircuitUpdateInput.
        :type name: str
        """

        self._name = name

    @property
    def speed(self):
        """Gets the speed of this VirtualCircuitUpdateInput.


        :return: The speed of this VirtualCircuitUpdateInput.
        :rtype: str
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this VirtualCircuitUpdateInput.


        :param speed: The speed of this VirtualCircuitUpdateInput.
        :type speed: str
        """

        self._speed = speed

    @property
    def tags(self):
        """Gets the tags of this VirtualCircuitUpdateInput.


        :return: The tags of this VirtualCircuitUpdateInput.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this VirtualCircuitUpdateInput.


        :param tags: The tags of this VirtualCircuitUpdateInput.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def vnid(self):
        """Gets the vnid of this VirtualCircuitUpdateInput.

        A Virtual Network record UUID or the VNID of a Virtual Network in your project.  # noqa: E501

        :return: The vnid of this VirtualCircuitUpdateInput.
        :rtype: str
        """
        return self._vnid

    @vnid.setter
    def vnid(self, vnid):
        """Sets the vnid of this VirtualCircuitUpdateInput.

        A Virtual Network record UUID or the VNID of a Virtual Network in your project.  # noqa: E501

        :param vnid: The vnid of this VirtualCircuitUpdateInput.
        :type vnid: str
        """

        self._vnid = vnid