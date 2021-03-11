# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class HardwareLocation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, cage=None, facility=None, rack=None, row=None, switch=None):  # noqa: E501
        """HardwareLocation - a model defined in OpenAPI

        :param cage: The cage of this HardwareLocation.  # noqa: E501
        :type cage: str
        :param facility: The facility of this HardwareLocation.  # noqa: E501
        :type facility: str
        :param rack: The rack of this HardwareLocation.  # noqa: E501
        :type rack: str
        :param row: The row of this HardwareLocation.  # noqa: E501
        :type row: str
        :param switch: The switch of this HardwareLocation.  # noqa: E501
        :type switch: str
        """
        self.openapi_types = {
            'cage': str,
            'facility': str,
            'rack': str,
            'row': str,
            'switch': str
        }

        self.attribute_map = {
            'cage': 'cage',
            'facility': 'facility',
            'rack': 'rack',
            'row': 'row',
            'switch': 'switch'
        }

        self._cage = cage
        self._facility = facility
        self._rack = rack
        self._row = row
        self._switch = switch

    @classmethod
    def from_dict(cls, dikt) -> 'HardwareLocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HardwareLocation of this HardwareLocation.  # noqa: E501
        :rtype: HardwareLocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def cage(self):
        """Gets the cage of this HardwareLocation.


        :return: The cage of this HardwareLocation.
        :rtype: str
        """
        return self._cage

    @cage.setter
    def cage(self, cage):
        """Sets the cage of this HardwareLocation.


        :param cage: The cage of this HardwareLocation.
        :type cage: str
        """

        self._cage = cage

    @property
    def facility(self):
        """Gets the facility of this HardwareLocation.


        :return: The facility of this HardwareLocation.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this HardwareLocation.


        :param facility: The facility of this HardwareLocation.
        :type facility: str
        """

        self._facility = facility

    @property
    def rack(self):
        """Gets the rack of this HardwareLocation.


        :return: The rack of this HardwareLocation.
        :rtype: str
        """
        return self._rack

    @rack.setter
    def rack(self, rack):
        """Sets the rack of this HardwareLocation.


        :param rack: The rack of this HardwareLocation.
        :type rack: str
        """

        self._rack = rack

    @property
    def row(self):
        """Gets the row of this HardwareLocation.


        :return: The row of this HardwareLocation.
        :rtype: str
        """
        return self._row

    @row.setter
    def row(self, row):
        """Sets the row of this HardwareLocation.


        :param row: The row of this HardwareLocation.
        :type row: str
        """

        self._row = row

    @property
    def switch(self):
        """Gets the switch of this HardwareLocation.


        :return: The switch of this HardwareLocation.
        :rtype: str
        """
        return self._switch

    @switch.setter
    def switch(self, switch):
        """Sets the switch of this HardwareLocation.


        :param switch: The switch of this HardwareLocation.
        :type switch: str
        """

        self._switch = switch
