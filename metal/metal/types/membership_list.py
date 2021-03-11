# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.membership import Membership
from metal import util

from metal.types.membership import Membership  # noqa: E501

class MembershipList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, memberships=None):  # noqa: E501
        """MembershipList - a model defined in OpenAPI

        :param memberships: The memberships of this MembershipList.  # noqa: E501
        :type memberships: List[Membership]
        """
        self.openapi_types = {
            'memberships': List[Membership]
        }

        self.attribute_map = {
            'memberships': 'memberships'
        }

        self._memberships = memberships

    @classmethod
    def from_dict(cls, dikt) -> 'MembershipList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The MembershipList of this MembershipList.  # noqa: E501
        :rtype: MembershipList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def memberships(self):
        """Gets the memberships of this MembershipList.


        :return: The memberships of this MembershipList.
        :rtype: List[Membership]
        """
        return self._memberships

    @memberships.setter
    def memberships(self, memberships):
        """Sets the memberships of this MembershipList.


        :param memberships: The memberships of this MembershipList.
        :type memberships: List[Membership]
        """

        self._memberships = memberships
