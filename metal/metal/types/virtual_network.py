# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.href import Href
from metal import util

from metal.types.href import Href  # noqa: E501

class VirtualNetwork(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, description=None, vxlan=None, facility=None, instances=None, assigned_to=None, href=None):  # noqa: E501
        """VirtualNetwork - a model defined in OpenAPI

        :param id: The id of this VirtualNetwork.  # noqa: E501
        :type id: str
        :param description: The description of this VirtualNetwork.  # noqa: E501
        :type description: str
        :param vxlan: The vxlan of this VirtualNetwork.  # noqa: E501
        :type vxlan: int
        :param facility: The facility of this VirtualNetwork.  # noqa: E501
        :type facility: Href
        :param instances: The instances of this VirtualNetwork.  # noqa: E501
        :type instances: List[Href]
        :param assigned_to: The assigned_to of this VirtualNetwork.  # noqa: E501
        :type assigned_to: Href
        :param href: The href of this VirtualNetwork.  # noqa: E501
        :type href: str
        """
        self.openapi_types = {
            'id': str,
            'description': str,
            'vxlan': int,
            'facility': Href,
            'instances': List[Href],
            'assigned_to': Href,
            'href': str
        }

        self.attribute_map = {
            'id': 'id',
            'description': 'description',
            'vxlan': 'vxlan',
            'facility': 'facility',
            'instances': 'instances',
            'assigned_to': 'assigned_to',
            'href': 'href'
        }

        self._id = id
        self._description = description
        self._vxlan = vxlan
        self._facility = facility
        self._instances = instances
        self._assigned_to = assigned_to
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'VirtualNetwork':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VirtualNetwork of this VirtualNetwork.  # noqa: E501
        :rtype: VirtualNetwork
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VirtualNetwork.


        :return: The id of this VirtualNetwork.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VirtualNetwork.


        :param id: The id of this VirtualNetwork.
        :type id: str
        """

        self._id = id

    @property
    def description(self):
        """Gets the description of this VirtualNetwork.


        :return: The description of this VirtualNetwork.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VirtualNetwork.


        :param description: The description of this VirtualNetwork.
        :type description: str
        """

        self._description = description

    @property
    def vxlan(self):
        """Gets the vxlan of this VirtualNetwork.


        :return: The vxlan of this VirtualNetwork.
        :rtype: int
        """
        return self._vxlan

    @vxlan.setter
    def vxlan(self, vxlan):
        """Sets the vxlan of this VirtualNetwork.


        :param vxlan: The vxlan of this VirtualNetwork.
        :type vxlan: int
        """

        self._vxlan = vxlan

    @property
    def facility(self):
        """Gets the facility of this VirtualNetwork.


        :return: The facility of this VirtualNetwork.
        :rtype: Href
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this VirtualNetwork.


        :param facility: The facility of this VirtualNetwork.
        :type facility: Href
        """

        self._facility = facility

    @property
    def instances(self):
        """Gets the instances of this VirtualNetwork.


        :return: The instances of this VirtualNetwork.
        :rtype: List[Href]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        """Sets the instances of this VirtualNetwork.


        :param instances: The instances of this VirtualNetwork.
        :type instances: List[Href]
        """

        self._instances = instances

    @property
    def assigned_to(self):
        """Gets the assigned_to of this VirtualNetwork.


        :return: The assigned_to of this VirtualNetwork.
        :rtype: Href
        """
        return self._assigned_to

    @assigned_to.setter
    def assigned_to(self, assigned_to):
        """Sets the assigned_to of this VirtualNetwork.


        :param assigned_to: The assigned_to of this VirtualNetwork.
        :type assigned_to: Href
        """

        self._assigned_to = assigned_to

    @property
    def href(self):
        """Gets the href of this VirtualNetwork.


        :return: The href of this VirtualNetwork.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this VirtualNetwork.


        :param href: The href of this VirtualNetwork.
        :type href: str
        """

        self._href = href