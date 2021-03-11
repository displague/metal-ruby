# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.staff_hardware_little import StaffHardwareLittle
from metal import util

from metal.types.staff_hardware_little import StaffHardwareLittle  # noqa: E501

class StaffServerRack(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, slot_number=None, server_rack=None, hardware=None):  # noqa: E501
        """StaffServerRack - a model defined in OpenAPI

        :param id: The id of this StaffServerRack.  # noqa: E501
        :type id: str
        :param slot_number: The slot_number of this StaffServerRack.  # noqa: E501
        :type slot_number: int
        :param server_rack: The server_rack of this StaffServerRack.  # noqa: E501
        :type server_rack: StaffServerRack
        :param hardware: The hardware of this StaffServerRack.  # noqa: E501
        :type hardware: StaffHardwareLittle
        """
        self.openapi_types = {
            'id': str,
            'slot_number': int,
            'server_rack': StaffServerRack,
            'hardware': StaffHardwareLittle
        }

        self.attribute_map = {
            'id': 'id',
            'slot_number': 'slot_number',
            'server_rack': 'server_rack',
            'hardware': 'hardware'
        }

        self._id = id
        self._slot_number = slot_number
        self._server_rack = server_rack
        self._hardware = hardware

    @classmethod
    def from_dict(cls, dikt) -> 'StaffServerRack':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Staff::ServerRack of this StaffServerRack.  # noqa: E501
        :rtype: StaffServerRack
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this StaffServerRack.


        :return: The id of this StaffServerRack.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffServerRack.


        :param id: The id of this StaffServerRack.
        :type id: str
        """

        self._id = id

    @property
    def slot_number(self):
        """Gets the slot_number of this StaffServerRack.


        :return: The slot_number of this StaffServerRack.
        :rtype: int
        """
        return self._slot_number

    @slot_number.setter
    def slot_number(self, slot_number):
        """Sets the slot_number of this StaffServerRack.


        :param slot_number: The slot_number of this StaffServerRack.
        :type slot_number: int
        """

        self._slot_number = slot_number

    @property
    def server_rack(self):
        """Gets the server_rack of this StaffServerRack.


        :return: The server_rack of this StaffServerRack.
        :rtype: StaffServerRack
        """
        return self._server_rack

    @server_rack.setter
    def server_rack(self, server_rack):
        """Sets the server_rack of this StaffServerRack.


        :param server_rack: The server_rack of this StaffServerRack.
        :type server_rack: StaffServerRack
        """

        self._server_rack = server_rack

    @property
    def hardware(self):
        """Gets the hardware of this StaffServerRack.


        :return: The hardware of this StaffServerRack.
        :rtype: StaffHardwareLittle
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this StaffServerRack.


        :param hardware: The hardware of this StaffServerRack.
        :type hardware: StaffHardwareLittle
        """

        self._hardware = hardware