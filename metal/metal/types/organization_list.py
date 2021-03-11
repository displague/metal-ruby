# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.meta import Meta
from metal.types.organization import Organization
from metal import util

from metal.types.meta import Meta  # noqa: E501
from metal.types.organization import Organization  # noqa: E501

class OrganizationList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, organizations=None, meta=None):  # noqa: E501
        """OrganizationList - a model defined in OpenAPI

        :param organizations: The organizations of this OrganizationList.  # noqa: E501
        :type organizations: List[Organization]
        :param meta: The meta of this OrganizationList.  # noqa: E501
        :type meta: Meta
        """
        self.openapi_types = {
            'organizations': List[Organization],
            'meta': Meta
        }

        self.attribute_map = {
            'organizations': 'organizations',
            'meta': 'meta'
        }

        self._organizations = organizations
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'OrganizationList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OrganizationList of this OrganizationList.  # noqa: E501
        :rtype: OrganizationList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def organizations(self):
        """Gets the organizations of this OrganizationList.


        :return: The organizations of this OrganizationList.
        :rtype: List[Organization]
        """
        return self._organizations

    @organizations.setter
    def organizations(self, organizations):
        """Sets the organizations of this OrganizationList.


        :param organizations: The organizations of this OrganizationList.
        :type organizations: List[Organization]
        """

        self._organizations = organizations

    @property
    def meta(self):
        """Gets the meta of this OrganizationList.


        :return: The meta of this OrganizationList.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this OrganizationList.


        :param meta: The meta of this OrganizationList.
        :type meta: Meta
        """

        self._meta = meta