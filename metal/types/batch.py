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


class Batch(object):
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
        'error_messages': 'list[str]',
        'quantity': 'int',
        'state': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'devices': 'list[Href]',
        'project': 'Href'
    }

    attribute_map = {
        'id': 'id',
        'error_messages': 'error_messages',
        'quantity': 'quantity',
        'state': 'state',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'devices': 'devices',
        'project': 'project'
    }

    def __init__(self, id=None, error_messages=None, quantity=None, state=None, created_at=None, updated_at=None, devices=None, project=None, local_vars_configuration=None):  # noqa: E501
        """Batch - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._error_messages = None
        self._quantity = None
        self._state = None
        self._created_at = None
        self._updated_at = None
        self._devices = None
        self._project = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if error_messages is not None:
            self.error_messages = error_messages
        if quantity is not None:
            self.quantity = quantity
        if state is not None:
            self.state = state
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if devices is not None:
            self.devices = devices
        if project is not None:
            self.project = project

    @property
    def id(self):
        """Gets the id of this Batch.  # noqa: E501


        :return: The id of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Batch.


        :param id: The id of this Batch.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def error_messages(self):
        """Gets the error_messages of this Batch.  # noqa: E501


        :return: The error_messages of this Batch.  # noqa: E501
        :rtype: list[str]
        """
        return self._error_messages

    @error_messages.setter
    def error_messages(self, error_messages):
        """Sets the error_messages of this Batch.


        :param error_messages: The error_messages of this Batch.  # noqa: E501
        :type error_messages: list[str]
        """

        self._error_messages = error_messages

    @property
    def quantity(self):
        """Gets the quantity of this Batch.  # noqa: E501


        :return: The quantity of this Batch.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this Batch.


        :param quantity: The quantity of this Batch.  # noqa: E501
        :type quantity: int
        """

        self._quantity = quantity

    @property
    def state(self):
        """Gets the state of this Batch.  # noqa: E501


        :return: The state of this Batch.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Batch.


        :param state: The state of this Batch.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def created_at(self):
        """Gets the created_at of this Batch.  # noqa: E501


        :return: The created_at of this Batch.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Batch.


        :param created_at: The created_at of this Batch.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Batch.  # noqa: E501


        :return: The updated_at of this Batch.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Batch.


        :param updated_at: The updated_at of this Batch.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def devices(self):
        """Gets the devices of this Batch.  # noqa: E501


        :return: The devices of this Batch.  # noqa: E501
        :rtype: list[Href]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this Batch.


        :param devices: The devices of this Batch.  # noqa: E501
        :type devices: list[Href]
        """

        self._devices = devices

    @property
    def project(self):
        """Gets the project of this Batch.  # noqa: E501


        :return: The project of this Batch.  # noqa: E501
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this Batch.


        :param project: The project of this Batch.  # noqa: E501
        :type project: Href
        """

        self._project = project

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
        if not isinstance(other, Batch):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Batch):
            return True

        return self.to_dict() != other.to_dict()