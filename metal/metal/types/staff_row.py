# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from metal.configuration import Configuration


class StaffRow(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'id': 'str',
        'name': 'str',
        'code': 'str',
        'cage': 'StaffCage',
        'server_racks': 'list[StaffServerRack]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'code': 'code',
        'cage': 'cage',
        'server_racks': 'server_racks'
    }

    def __init__(self, id=None, name=None, code=None, cage=None, server_racks=None, local_vars_configuration=None):  # noqa: E501
        """StaffRow - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._code = None
        self._cage = None
        self._server_racks = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if code is not None:
            self.code = code
        if cage is not None:
            self.cage = cage
        if server_racks is not None:
            self.server_racks = server_racks

    @property
    def id(self):
        """Gets the id of this StaffRow.  # noqa: E501


        :return: The id of this StaffRow.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffRow.


        :param id: The id of this StaffRow.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StaffRow.  # noqa: E501


        :return: The name of this StaffRow.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffRow.


        :param name: The name of this StaffRow.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def code(self):
        """Gets the code of this StaffRow.  # noqa: E501


        :return: The code of this StaffRow.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this StaffRow.


        :param code: The code of this StaffRow.  # noqa: E501
        :type code: str
        """

        self._code = code

    @property
    def cage(self):
        """Gets the cage of this StaffRow.  # noqa: E501


        :return: The cage of this StaffRow.  # noqa: E501
        :rtype: StaffCage
        """
        return self._cage

    @cage.setter
    def cage(self, cage):
        """Sets the cage of this StaffRow.


        :param cage: The cage of this StaffRow.  # noqa: E501
        :type cage: StaffCage
        """

        self._cage = cage

    @property
    def server_racks(self):
        """Gets the server_racks of this StaffRow.  # noqa: E501


        :return: The server_racks of this StaffRow.  # noqa: E501
        :rtype: list[StaffServerRack]
        """
        return self._server_racks

    @server_racks.setter
    def server_racks(self, server_racks):
        """Sets the server_racks of this StaffRow.


        :param server_racks: The server_racks of this StaffRow.  # noqa: E501
        :type server_racks: list[StaffServerRack]
        """

        self._server_racks = server_racks

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StaffRow):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffRow):
            return True

        return self.to_dict() != other.to_dict()
