# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class VolumeUpdateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, size=None, locked=None, billing_cycle=None, customdata=None):  # noqa: E501
        """VolumeUpdateInput - a model defined in OpenAPI

        :param description: The description of this VolumeUpdateInput.  # noqa: E501
        :type description: str
        :param size: The size of this VolumeUpdateInput.  # noqa: E501
        :type size: int
        :param locked: The locked of this VolumeUpdateInput.  # noqa: E501
        :type locked: bool
        :param billing_cycle: The billing_cycle of this VolumeUpdateInput.  # noqa: E501
        :type billing_cycle: str
        :param customdata: The customdata of this VolumeUpdateInput.  # noqa: E501
        :type customdata: object
        """
        self.openapi_types = {
            'description': str,
            'size': int,
            'locked': bool,
            'billing_cycle': str,
            'customdata': object
        }

        self.attribute_map = {
            'description': 'description',
            'size': 'size',
            'locked': 'locked',
            'billing_cycle': 'billing_cycle',
            'customdata': 'customdata'
        }

        self._description = description
        self._size = size
        self._locked = locked
        self._billing_cycle = billing_cycle
        self._customdata = customdata

    @classmethod
    def from_dict(cls, dikt) -> 'VolumeUpdateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VolumeUpdateInput of this VolumeUpdateInput.  # noqa: E501
        :rtype: VolumeUpdateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this VolumeUpdateInput.


        :return: The description of this VolumeUpdateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeUpdateInput.


        :param description: The description of this VolumeUpdateInput.
        :type description: str
        """

        self._description = description

    @property
    def size(self):
        """Gets the size of this VolumeUpdateInput.


        :return: The size of this VolumeUpdateInput.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeUpdateInput.


        :param size: The size of this VolumeUpdateInput.
        :type size: int
        """

        self._size = size

    @property
    def locked(self):
        """Gets the locked of this VolumeUpdateInput.


        :return: The locked of this VolumeUpdateInput.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this VolumeUpdateInput.


        :param locked: The locked of this VolumeUpdateInput.
        :type locked: bool
        """

        self._locked = locked

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this VolumeUpdateInput.

        hourly  # noqa: E501

        :return: The billing_cycle of this VolumeUpdateInput.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this VolumeUpdateInput.

        hourly  # noqa: E501

        :param billing_cycle: The billing_cycle of this VolumeUpdateInput.
        :type billing_cycle: str
        """

        self._billing_cycle = billing_cycle

    @property
    def customdata(self):
        """Gets the customdata of this VolumeUpdateInput.


        :return: The customdata of this VolumeUpdateInput.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this VolumeUpdateInput.


        :param customdata: The customdata of this VolumeUpdateInput.
        :type customdata: object
        """

        self._customdata = customdata