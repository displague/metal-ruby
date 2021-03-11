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


class Plan(object):
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
        'slug': 'str',
        'name': 'str',
        'description': 'str',
        'line': 'str',
        'specs': 'object',
        'pricing': 'object',
        'legacy': 'bool',
        '_class': 'str',
        'available_in': 'list[Href]'
    }

    attribute_map = {
        'id': 'id',
        'slug': 'slug',
        'name': 'name',
        'description': 'description',
        'line': 'line',
        'specs': 'specs',
        'pricing': 'pricing',
        'legacy': 'legacy',
        '_class': 'class',
        'available_in': 'available_in'
    }

    def __init__(self, id=None, slug=None, name=None, description=None, line=None, specs=None, pricing=None, legacy=None, _class=None, available_in=None, local_vars_configuration=None):  # noqa: E501
        """Plan - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._slug = None
        self._name = None
        self._description = None
        self._line = None
        self._specs = None
        self._pricing = None
        self._legacy = None
        self.__class = None
        self._available_in = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if slug is not None:
            self.slug = slug
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if line is not None:
            self.line = line
        if specs is not None:
            self.specs = specs
        if pricing is not None:
            self.pricing = pricing
        if legacy is not None:
            self.legacy = legacy
        if _class is not None:
            self._class = _class
        if available_in is not None:
            self.available_in = available_in

    @property
    def id(self):
        """Gets the id of this Plan.  # noqa: E501


        :return: The id of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Plan.


        :param id: The id of this Plan.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this Plan.  # noqa: E501


        :return: The slug of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Plan.


        :param slug: The slug of this Plan.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this Plan.  # noqa: E501


        :return: The name of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Plan.


        :param name: The name of this Plan.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this Plan.  # noqa: E501


        :return: The description of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Plan.


        :param description: The description of this Plan.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def line(self):
        """Gets the line of this Plan.  # noqa: E501


        :return: The line of this Plan.  # noqa: E501
        :rtype: str
        """
        return self._line

    @line.setter
    def line(self, line):
        """Sets the line of this Plan.


        :param line: The line of this Plan.  # noqa: E501
        :type line: str
        """

        self._line = line

    @property
    def specs(self):
        """Gets the specs of this Plan.  # noqa: E501


        :return: The specs of this Plan.  # noqa: E501
        :rtype: object
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this Plan.


        :param specs: The specs of this Plan.  # noqa: E501
        :type specs: object
        """

        self._specs = specs

    @property
    def pricing(self):
        """Gets the pricing of this Plan.  # noqa: E501


        :return: The pricing of this Plan.  # noqa: E501
        :rtype: object
        """
        return self._pricing

    @pricing.setter
    def pricing(self, pricing):
        """Sets the pricing of this Plan.


        :param pricing: The pricing of this Plan.  # noqa: E501
        :type pricing: object
        """

        self._pricing = pricing

    @property
    def legacy(self):
        """Gets the legacy of this Plan.  # noqa: E501


        :return: The legacy of this Plan.  # noqa: E501
        :rtype: bool
        """
        return self._legacy

    @legacy.setter
    def legacy(self, legacy):
        """Sets the legacy of this Plan.


        :param legacy: The legacy of this Plan.  # noqa: E501
        :type legacy: bool
        """

        self._legacy = legacy

    @property
    def _class(self):
        """Gets the _class of this Plan.  # noqa: E501


        :return: The _class of this Plan.  # noqa: E501
        :rtype: str
        """
        return self.__class

    @_class.setter
    def _class(self, _class):
        """Sets the _class of this Plan.


        :param _class: The _class of this Plan.  # noqa: E501
        :type _class: str
        """

        self.__class = _class

    @property
    def available_in(self):
        """Gets the available_in of this Plan.  # noqa: E501


        :return: The available_in of this Plan.  # noqa: E501
        :rtype: list[Href]
        """
        return self._available_in

    @available_in.setter
    def available_in(self, available_in):
        """Sets the available_in of this Plan.


        :param available_in: The available_in of this Plan.  # noqa: E501
        :type available_in: list[Href]
        """

        self._available_in = available_in

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
        if not isinstance(other, Plan):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Plan):
            return True

        return self.to_dict() != other.to_dict()
