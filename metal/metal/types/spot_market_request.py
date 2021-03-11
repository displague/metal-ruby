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


class SpotMarketRequest(object):
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
        'devices_min': 'int',
        'devices_max': 'int',
        'max_bid_price': 'float',
        'created_at': 'datetime',
        'end_at': 'datetime',
        'href': 'str',
        'facilities': 'Href',
        'project': 'Href',
        'instances': 'Href'
    }

    attribute_map = {
        'id': 'id',
        'devices_min': 'devices_min',
        'devices_max': 'devices_max',
        'max_bid_price': 'max_bid_price',
        'created_at': 'created_at',
        'end_at': 'end_at',
        'href': 'href',
        'facilities': 'facilities',
        'project': 'project',
        'instances': 'instances'
    }

    def __init__(self, id=None, devices_min=None, devices_max=None, max_bid_price=None, created_at=None, end_at=None, href=None, facilities=None, project=None, instances=None, local_vars_configuration=None):  # noqa: E501
        """SpotMarketRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._devices_min = None
        self._devices_max = None
        self._max_bid_price = None
        self._created_at = None
        self._end_at = None
        self._href = None
        self._facilities = None
        self._project = None
        self._instances = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if devices_min is not None:
            self.devices_min = devices_min
        if devices_max is not None:
            self.devices_max = devices_max
        if max_bid_price is not None:
            self.max_bid_price = max_bid_price
        if created_at is not None:
            self.created_at = created_at
        if end_at is not None:
            self.end_at = end_at
        if href is not None:
            self.href = href
        if facilities is not None:
            self.facilities = facilities
        if project is not None:
            self.project = project
        if instances is not None:
            self.instances = instances

    @property
    def id(self):
        """Gets the id of this SpotMarketRequest.  # noqa: E501


        :return: The id of this SpotMarketRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpotMarketRequest.


        :param id: The id of this SpotMarketRequest.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def devices_min(self):
        """Gets the devices_min of this SpotMarketRequest.  # noqa: E501


        :return: The devices_min of this SpotMarketRequest.  # noqa: E501
        :rtype: int
        """
        return self._devices_min

    @devices_min.setter
    def devices_min(self, devices_min):
        """Sets the devices_min of this SpotMarketRequest.


        :param devices_min: The devices_min of this SpotMarketRequest.  # noqa: E501
        :type devices_min: int
        """

        self._devices_min = devices_min

    @property
    def devices_max(self):
        """Gets the devices_max of this SpotMarketRequest.  # noqa: E501


        :return: The devices_max of this SpotMarketRequest.  # noqa: E501
        :rtype: int
        """
        return self._devices_max

    @devices_max.setter
    def devices_max(self, devices_max):
        """Sets the devices_max of this SpotMarketRequest.


        :param devices_max: The devices_max of this SpotMarketRequest.  # noqa: E501
        :type devices_max: int
        """

        self._devices_max = devices_max

    @property
    def max_bid_price(self):
        """Gets the max_bid_price of this SpotMarketRequest.  # noqa: E501


        :return: The max_bid_price of this SpotMarketRequest.  # noqa: E501
        :rtype: float
        """
        return self._max_bid_price

    @max_bid_price.setter
    def max_bid_price(self, max_bid_price):
        """Sets the max_bid_price of this SpotMarketRequest.


        :param max_bid_price: The max_bid_price of this SpotMarketRequest.  # noqa: E501
        :type max_bid_price: float
        """

        self._max_bid_price = max_bid_price

    @property
    def created_at(self):
        """Gets the created_at of this SpotMarketRequest.  # noqa: E501


        :return: The created_at of this SpotMarketRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SpotMarketRequest.


        :param created_at: The created_at of this SpotMarketRequest.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def end_at(self):
        """Gets the end_at of this SpotMarketRequest.  # noqa: E501


        :return: The end_at of this SpotMarketRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        """Sets the end_at of this SpotMarketRequest.


        :param end_at: The end_at of this SpotMarketRequest.  # noqa: E501
        :type end_at: datetime
        """

        self._end_at = end_at

    @property
    def href(self):
        """Gets the href of this SpotMarketRequest.  # noqa: E501


        :return: The href of this SpotMarketRequest.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this SpotMarketRequest.


        :param href: The href of this SpotMarketRequest.  # noqa: E501
        :type href: str
        """

        self._href = href

    @property
    def facilities(self):
        """Gets the facilities of this SpotMarketRequest.  # noqa: E501


        :return: The facilities of this SpotMarketRequest.  # noqa: E501
        :rtype: Href
        """
        return self._facilities

    @facilities.setter
    def facilities(self, facilities):
        """Sets the facilities of this SpotMarketRequest.


        :param facilities: The facilities of this SpotMarketRequest.  # noqa: E501
        :type facilities: Href
        """

        self._facilities = facilities

    @property
    def project(self):
        """Gets the project of this SpotMarketRequest.  # noqa: E501


        :return: The project of this SpotMarketRequest.  # noqa: E501
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this SpotMarketRequest.


        :param project: The project of this SpotMarketRequest.  # noqa: E501
        :type project: Href
        """

        self._project = project

    @property
    def instances(self):
        """Gets the instances of this SpotMarketRequest.  # noqa: E501


        :return: The instances of this SpotMarketRequest.  # noqa: E501
        :rtype: Href
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this SpotMarketRequest.


        :param instances: The instances of this SpotMarketRequest.  # noqa: E501
        :type instances: Href
        """

        self._instances = instances

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
        if not isinstance(other, SpotMarketRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpotMarketRequest):
            return True

        return self.to_dict() != other.to_dict()
