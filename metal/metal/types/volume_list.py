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


class VolumeList(object):
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
        'volumes': 'list[Volume]',
        'meta': 'Meta'
    }

    attribute_map = {
        'volumes': 'volumes',
        'meta': 'meta'
    }

    def __init__(self, volumes=None, meta=None, local_vars_configuration=None):  # noqa: E501
        """VolumeList - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._volumes = None
        self._meta = None
        self.discriminator = None

        if volumes is not None:
            self.volumes = volumes
        if meta is not None:
            self.meta = meta

    @property
    def volumes(self):
        """Gets the volumes of this VolumeList.  # noqa: E501


        :return: The volumes of this VolumeList.  # noqa: E501
        :rtype: list[Volume]
        """
        return self._volumes

    @volumes.setter
    def volumes(self, volumes):
        """Sets the volumes of this VolumeList.


        :param volumes: The volumes of this VolumeList.  # noqa: E501
        :type volumes: list[Volume]
        """

        self._volumes = volumes

    @property
    def meta(self):
        """Gets the meta of this VolumeList.  # noqa: E501


        :return: The meta of this VolumeList.  # noqa: E501
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this VolumeList.


        :param meta: The meta of this VolumeList.  # noqa: E501
        :type meta: Meta
        """

        self._meta = meta

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
        if not isinstance(other, VolumeList):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, VolumeList):
            return True

        return self.to_dict() != other.to_dict()
