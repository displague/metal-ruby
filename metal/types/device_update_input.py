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


class DeviceUpdateInput(object):
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
        'hostname': 'str',
        'description': 'str',
        'billing_cycle': 'str',
        'userdata': 'str',
        'locked': 'bool',
        'tags': 'list[str]',
        'always_pxe': 'bool',
        'ipxe_script_url': 'str',
        'spot_instance': 'bool',
        'customdata': 'object'
    }

    attribute_map = {
        'hostname': 'hostname',
        'description': 'description',
        'billing_cycle': 'billing_cycle',
        'userdata': 'userdata',
        'locked': 'locked',
        'tags': 'tags',
        'always_pxe': 'always_pxe',
        'ipxe_script_url': 'ipxe_script_url',
        'spot_instance': 'spot_instance',
        'customdata': 'customdata'
    }

    def __init__(self, hostname=None, description=None, billing_cycle=None, userdata=None, locked=None, tags=None, always_pxe=None, ipxe_script_url=None, spot_instance=None, customdata=None, local_vars_configuration=None):  # noqa: E501
        """DeviceUpdateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._hostname = None
        self._description = None
        self._billing_cycle = None
        self._userdata = None
        self._locked = None
        self._tags = None
        self._always_pxe = None
        self._ipxe_script_url = None
        self._spot_instance = None
        self._customdata = None
        self.discriminator = None

        if hostname is not None:
            self.hostname = hostname
        if description is not None:
            self.description = description
        if billing_cycle is not None:
            self.billing_cycle = billing_cycle
        if userdata is not None:
            self.userdata = userdata
        if locked is not None:
            self.locked = locked
        if tags is not None:
            self.tags = tags
        if always_pxe is not None:
            self.always_pxe = always_pxe
        if ipxe_script_url is not None:
            self.ipxe_script_url = ipxe_script_url
        if spot_instance is not None:
            self.spot_instance = spot_instance
        if customdata is not None:
            self.customdata = customdata

    @property
    def hostname(self):
        """Gets the hostname of this DeviceUpdateInput.  # noqa: E501


        :return: The hostname of this DeviceUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DeviceUpdateInput.


        :param hostname: The hostname of this DeviceUpdateInput.  # noqa: E501
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def description(self):
        """Gets the description of this DeviceUpdateInput.  # noqa: E501


        :return: The description of this DeviceUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceUpdateInput.


        :param description: The description of this DeviceUpdateInput.  # noqa: E501
        :type description: str
        """

        self._description = description

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this DeviceUpdateInput.  # noqa: E501


        :return: The billing_cycle of this DeviceUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this DeviceUpdateInput.


        :param billing_cycle: The billing_cycle of this DeviceUpdateInput.  # noqa: E501
        :type billing_cycle: str
        """

        self._billing_cycle = billing_cycle

    @property
    def userdata(self):
        """Gets the userdata of this DeviceUpdateInput.  # noqa: E501


        :return: The userdata of this DeviceUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._userdata

    @userdata.setter
    def userdata(self, userdata):
        """Sets the userdata of this DeviceUpdateInput.


        :param userdata: The userdata of this DeviceUpdateInput.  # noqa: E501
        :type userdata: str
        """

        self._userdata = userdata

    @property
    def locked(self):
        """Gets the locked of this DeviceUpdateInput.  # noqa: E501


        :return: The locked of this DeviceUpdateInput.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this DeviceUpdateInput.


        :param locked: The locked of this DeviceUpdateInput.  # noqa: E501
        :type locked: bool
        """

        self._locked = locked

    @property
    def tags(self):
        """Gets the tags of this DeviceUpdateInput.  # noqa: E501


        :return: The tags of this DeviceUpdateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeviceUpdateInput.


        :param tags: The tags of this DeviceUpdateInput.  # noqa: E501
        :type tags: list[str]
        """

        self._tags = tags

    @property
    def always_pxe(self):
        """Gets the always_pxe of this DeviceUpdateInput.  # noqa: E501


        :return: The always_pxe of this DeviceUpdateInput.  # noqa: E501
        :rtype: bool
        """
        return self._always_pxe

    @always_pxe.setter
    def always_pxe(self, always_pxe):
        """Sets the always_pxe of this DeviceUpdateInput.


        :param always_pxe: The always_pxe of this DeviceUpdateInput.  # noqa: E501
        :type always_pxe: bool
        """

        self._always_pxe = always_pxe

    @property
    def ipxe_script_url(self):
        """Gets the ipxe_script_url of this DeviceUpdateInput.  # noqa: E501


        :return: The ipxe_script_url of this DeviceUpdateInput.  # noqa: E501
        :rtype: str
        """
        return self._ipxe_script_url

    @ipxe_script_url.setter
    def ipxe_script_url(self, ipxe_script_url):
        """Sets the ipxe_script_url of this DeviceUpdateInput.


        :param ipxe_script_url: The ipxe_script_url of this DeviceUpdateInput.  # noqa: E501
        :type ipxe_script_url: str
        """

        self._ipxe_script_url = ipxe_script_url

    @property
    def spot_instance(self):
        """Gets the spot_instance of this DeviceUpdateInput.  # noqa: E501


        :return: The spot_instance of this DeviceUpdateInput.  # noqa: E501
        :rtype: bool
        """
        return self._spot_instance

    @spot_instance.setter
    def spot_instance(self, spot_instance):
        """Sets the spot_instance of this DeviceUpdateInput.


        :param spot_instance: The spot_instance of this DeviceUpdateInput.  # noqa: E501
        :type spot_instance: bool
        """

        self._spot_instance = spot_instance

    @property
    def customdata(self):
        """Gets the customdata of this DeviceUpdateInput.  # noqa: E501


        :return: The customdata of this DeviceUpdateInput.  # noqa: E501
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this DeviceUpdateInput.


        :param customdata: The customdata of this DeviceUpdateInput.  # noqa: E501
        :type customdata: object
        """

        self._customdata = customdata

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
        if not isinstance(other, DeviceUpdateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DeviceUpdateInput):
            return True

        return self.to_dict() != other.to_dict()