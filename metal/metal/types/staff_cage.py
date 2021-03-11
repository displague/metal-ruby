# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.staff_facility_room import StaffFacilityRoom
from metal.types.staff_row import StaffRow
from metal import util

from metal.types.staff_facility_room import StaffFacilityRoom  # noqa: E501
from metal.types.staff_row import StaffRow  # noqa: E501

class StaffCage(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, code=None, facility_room=None, rows=None):  # noqa: E501
        """StaffCage - a model defined in OpenAPI

        :param id: The id of this StaffCage.  # noqa: E501
        :type id: str
        :param name: The name of this StaffCage.  # noqa: E501
        :type name: str
        :param code: The code of this StaffCage.  # noqa: E501
        :type code: str
        :param facility_room: The facility_room of this StaffCage.  # noqa: E501
        :type facility_room: StaffFacilityRoom
        :param rows: The rows of this StaffCage.  # noqa: E501
        :type rows: List[StaffRow]
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'code': str,
            'facility_room': StaffFacilityRoom,
            'rows': List[StaffRow]
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'code': 'code',
            'facility_room': 'facility_room',
            'rows': 'rows'
        }

        self._id = id
        self._name = name
        self._code = code
        self._facility_room = facility_room
        self._rows = rows

    @classmethod
    def from_dict(cls, dikt) -> 'StaffCage':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Staff::Cage of this StaffCage.  # noqa: E501
        :rtype: StaffCage
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this StaffCage.


        :return: The id of this StaffCage.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffCage.


        :param id: The id of this StaffCage.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StaffCage.


        :return: The name of this StaffCage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffCage.


        :param name: The name of this StaffCage.
        :type name: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this StaffCage.


        :return: The code of this StaffCage.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StaffCage.


        :param code: The code of this StaffCage.
        :type code: str
        """

        self._code = code

    @property
    def facility_room(self):
        """Gets the facility_room of this StaffCage.


        :return: The facility_room of this StaffCage.
        :rtype: StaffFacilityRoom
        """
        return self._facility_room

    @facility_room.setter
    def facility_room(self, facility_room):
        """Sets the facility_room of this StaffCage.


        :param facility_room: The facility_room of this StaffCage.
        :type facility_room: StaffFacilityRoom
        """

        self._facility_room = facility_room

    @property
    def rows(self):
        """Gets the rows of this StaffCage.


        :return: The rows of this StaffCage.
        :rtype: List[StaffRow]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this StaffCage.


        :param rows: The rows of this StaffCage.
        :type rows: List[StaffRow]
        """

        self._rows = rows