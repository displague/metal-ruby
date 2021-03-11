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


class Address(object):
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
        'address': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'zip_code': 'str',
        'country': 'str',
        'coordinates': 'Coordinates'
    }

    attribute_map = {
        'address': 'address',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'zip_code': 'zip_code',
        'country': 'country',
        'coordinates': 'coordinates'
    }

    def __init__(self, address=None, address2=None, city=None, state=None, zip_code=None, country=None, coordinates=None, local_vars_configuration=None):  # noqa: E501
        """Address - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._address = None
        self._address2 = None
        self._city = None
        self._state = None
        self._zip_code = None
        self._country = None
        self._coordinates = None
        self.discriminator = None

        self.address = address
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        self.zip_code = zip_code
        self.country = country
        if coordinates is not None:
            self.coordinates = coordinates

    @property
    def address(self):
        """Gets the address of this Address.  # noqa: E501


        :return: The address of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Address.


        :param address: The address of this Address.  # noqa: E501
        :type address: str
        """
        if self.local_vars_configuration.client_side_validation and address is None:  # noqa: E501
            raise ValueError("Invalid value for `address`, must not be `None`")  # noqa: E501

        self._address = address

    @property
    def address2(self):
        """Gets the address2 of this Address.  # noqa: E501


        :return: The address2 of this Address.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this Address.


        :param address2: The address2 of this Address.  # noqa: E501
        :type address2: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this Address.  # noqa: E501


        :return: The city of this Address.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.  # noqa: E501
        :type city: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Address.  # noqa: E501


        :return: The state of this Address.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.


        :param state: The state of this Address.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this Address.  # noqa: E501


        :return: The zip_code of this Address.  # noqa: E501
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Address.


        :param zip_code: The zip_code of this Address.  # noqa: E501
        :type zip_code: str
        """
        if self.local_vars_configuration.client_side_validation and zip_code is None:  # noqa: E501
            raise ValueError("Invalid value for `zip_code`, must not be `None`")  # noqa: E501

        self._zip_code = zip_code

    @property
    def country(self):
        """Gets the country of this Address.  # noqa: E501


        :return: The country of this Address.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.  # noqa: E501
        :type country: str
        """
        if self.local_vars_configuration.client_side_validation and country is None:  # noqa: E501
            raise ValueError("Invalid value for `country`, must not be `None`")  # noqa: E501

        self._country = country

    @property
    def coordinates(self):
        """Gets the coordinates of this Address.  # noqa: E501


        :return: The coordinates of this Address.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Address.


        :param coordinates: The coordinates of this Address.  # noqa: E501
        :type coordinates: Coordinates
        """

        self._coordinates = coordinates

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
        if not isinstance(other, Address):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Address):
            return True

        return self.to_dict() != other.to_dict()
