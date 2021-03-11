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


class StaffPlanVersion(object):
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
        'slug': 'str',
        'specs': 'str',
        'active': 'bool',
        'priority': 'int',
        'storage': 'str',
        'preinstallable': 'bool',
        'plan': 'StaffPlan',
        'facility': 'StaffFacilityLittle'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'slug': 'slug',
        'specs': 'specs',
        'active': 'active',
        'priority': 'priority',
        'storage': 'storage',
        'preinstallable': 'preinstallable',
        'plan': 'plan',
        'facility': 'facility'
    }

    def __init__(self, id=None, name=None, slug=None, specs=None, active=None, priority=None, storage=None, preinstallable=None, plan=None, facility=None, local_vars_configuration=None):  # noqa: E501
        """StaffPlanVersion - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._id = None
        self._name = None
        self._slug = None
        self._specs = None
        self._active = None
        self._priority = None
        self._storage = None
        self._preinstallable = None
        self._plan = None
        self._facility = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if slug is not None:
            self.slug = slug
        if specs is not None:
            self.specs = specs
        if active is not None:
            self.active = active
        if priority is not None:
            self.priority = priority
        if storage is not None:
            self.storage = storage
        if preinstallable is not None:
            self.preinstallable = preinstallable
        if plan is not None:
            self.plan = plan
        if facility is not None:
            self.facility = facility

    @property
    def id(self):
        """Gets the id of this StaffPlanVersion.  # noqa: E501


        :return: The id of this StaffPlanVersion.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffPlanVersion.


        :param id: The id of this StaffPlanVersion.  # noqa: E501
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this StaffPlanVersion.  # noqa: E501


        :return: The name of this StaffPlanVersion.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffPlanVersion.


        :param name: The name of this StaffPlanVersion.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this StaffPlanVersion.  # noqa: E501


        :return: The slug of this StaffPlanVersion.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this StaffPlanVersion.


        :param slug: The slug of this StaffPlanVersion.  # noqa: E501
        :type slug: str
        """

        self._slug = slug

    @property
    def specs(self):
        """Gets the specs of this StaffPlanVersion.  # noqa: E501


        :return: The specs of this StaffPlanVersion.  # noqa: E501
        :rtype: str
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        """Sets the specs of this StaffPlanVersion.


        :param specs: The specs of this StaffPlanVersion.  # noqa: E501
        :type specs: str
        """

        self._specs = specs

    @property
    def active(self):
        """Gets the active of this StaffPlanVersion.  # noqa: E501


        :return: The active of this StaffPlanVersion.  # noqa: E501
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this StaffPlanVersion.


        :param active: The active of this StaffPlanVersion.  # noqa: E501
        :type active: bool
        """

        self._active = active

    @property
    def priority(self):
        """Gets the priority of this StaffPlanVersion.  # noqa: E501


        :return: The priority of this StaffPlanVersion.  # noqa: E501
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this StaffPlanVersion.


        :param priority: The priority of this StaffPlanVersion.  # noqa: E501
        :type priority: int
        """

        self._priority = priority

    @property
    def storage(self):
        """Gets the storage of this StaffPlanVersion.  # noqa: E501


        :return: The storage of this StaffPlanVersion.  # noqa: E501
        :rtype: str
        """
        return self._storage

    @storage.setter
    def storage(self, storage):
        """Sets the storage of this StaffPlanVersion.


        :param storage: The storage of this StaffPlanVersion.  # noqa: E501
        :type storage: str
        """

        self._storage = storage

    @property
    def preinstallable(self):
        """Gets the preinstallable of this StaffPlanVersion.  # noqa: E501


        :return: The preinstallable of this StaffPlanVersion.  # noqa: E501
        :rtype: bool
        """
        return self._preinstallable

    @preinstallable.setter
    def preinstallable(self, preinstallable):
        """Sets the preinstallable of this StaffPlanVersion.


        :param preinstallable: The preinstallable of this StaffPlanVersion.  # noqa: E501
        :type preinstallable: bool
        """

        self._preinstallable = preinstallable

    @property
    def plan(self):
        """Gets the plan of this StaffPlanVersion.  # noqa: E501


        :return: The plan of this StaffPlanVersion.  # noqa: E501
        :rtype: StaffPlan
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this StaffPlanVersion.


        :param plan: The plan of this StaffPlanVersion.  # noqa: E501
        :type plan: StaffPlan
        """

        self._plan = plan

    @property
    def facility(self):
        """Gets the facility of this StaffPlanVersion.  # noqa: E501


        :return: The facility of this StaffPlanVersion.  # noqa: E501
        :rtype: StaffFacilityLittle
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this StaffPlanVersion.


        :param facility: The facility of this StaffPlanVersion.  # noqa: E501
        :type facility: StaffFacilityLittle
        """

        self._facility = facility

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
        if not isinstance(other, StaffPlanVersion):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffPlanVersion):
            return True

        return self.to_dict() != other.to_dict()
