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


class TransferRequest(object):
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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'target_organization': 'Href',
        'project': 'Href',
        'href': 'str'
    }

    attribute_map = {
        'id': 'id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'target_organization': 'target_organization',
        'project': 'project',
        'href': 'href'
    }

    def __init__(self, id=None, created_at=None, updated_at=None, target_organization=None, project=None, href=None, local_vars_configuration=None):  # noqa: E501
        """TransferRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._created_at = None
        self._updated_at = None
        self._target_organization = None
        self._project = None
        self._href = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if target_organization is not None:
            self.target_organization = target_organization
        if project is not None:
            self.project = project
        if href is not None:
            self.href = href

    @property
    def id(self):
        """Gets the id of this TransferRequest.  # noqa: E501


        :return: The id of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransferRequest.


        :param id: The id of this TransferRequest.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this TransferRequest.  # noqa: E501


        :return: The created_at of this TransferRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransferRequest.


        :param created_at: The created_at of this TransferRequest.  # noqa: E501
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TransferRequest.  # noqa: E501


        :return: The updated_at of this TransferRequest.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TransferRequest.


        :param updated_at: The updated_at of this TransferRequest.  # noqa: E501
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def target_organization(self):
        """Gets the target_organization of this TransferRequest.  # noqa: E501


        :return: The target_organization of this TransferRequest.  # noqa: E501
        :rtype: Href
        """
        return self._target_organization

    @target_organization.setter
    def target_organization(self, target_organization):
        """Sets the target_organization of this TransferRequest.


        :param target_organization: The target_organization of this TransferRequest.  # noqa: E501
        :type target_organization: Href
        """

        self._target_organization = target_organization

    @property
    def project(self):
        """Gets the project of this TransferRequest.  # noqa: E501


        :return: The project of this TransferRequest.  # noqa: E501
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TransferRequest.


        :param project: The project of this TransferRequest.  # noqa: E501
        :type project: Href
        """

        self._project = project

    @property
    def href(self):
        """Gets the href of this TransferRequest.  # noqa: E501


        :return: The href of this TransferRequest.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TransferRequest.


        :param href: The href of this TransferRequest.  # noqa: E501
        :type href: str
        """

        self._href = href

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
        if not isinstance(other, TransferRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, TransferRequest):
            return True

        return self.to_dict() != other.to_dict()
