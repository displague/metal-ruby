# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class OperatingSystem(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, slug=None, name=None, distro=None, version=None, provisionable_on=None):  # noqa: E501
        """OperatingSystem - a model defined in OpenAPI

        :param id: The id of this OperatingSystem.  # noqa: E501
        :type id: str
        :param slug: The slug of this OperatingSystem.  # noqa: E501
        :type slug: str
        :param name: The name of this OperatingSystem.  # noqa: E501
        :type name: str
        :param distro: The distro of this OperatingSystem.  # noqa: E501
        :type distro: str
        :param version: The version of this OperatingSystem.  # noqa: E501
        :type version: str
        :param provisionable_on: The provisionable_on of this OperatingSystem.  # noqa: E501
        :type provisionable_on: List[str]
        """
        self.openapi_types = {
            'id': str,
            'slug': str,
            'name': str,
            'distro': str,
            'version': str,
            'provisionable_on': List[str]
        }

        self.attribute_map = {
            'id': 'id',
            'slug': 'slug',
            'name': 'name',
            'distro': 'distro',
            'version': 'version',
            'provisionable_on': 'provisionable_on'
        }

        self._id = id
        self._slug = slug
        self._name = name
        self._distro = distro
        self._version = version
        self._provisionable_on = provisionable_on

    @classmethod
    def from_dict(cls, dikt) -> 'OperatingSystem':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The OperatingSystem of this OperatingSystem.  # noqa: E501
        :rtype: OperatingSystem
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this OperatingSystem.


        :return: The id of this OperatingSystem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OperatingSystem.


        :param id: The id of this OperatingSystem.
        :type id: str
        """

        self._id = id

    @property
    def slug(self):
        """Gets the slug of this OperatingSystem.


        :return: The slug of this OperatingSystem.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this OperatingSystem.


        :param slug: The slug of this OperatingSystem.
        :type slug: str
        """

        self._slug = slug

    @property
    def name(self):
        """Gets the name of this OperatingSystem.


        :return: The name of this OperatingSystem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OperatingSystem.


        :param name: The name of this OperatingSystem.
        :type name: str
        """

        self._name = name

    @property
    def distro(self):
        """Gets the distro of this OperatingSystem.


        :return: The distro of this OperatingSystem.
        :rtype: str
        """
        return self._distro

    @distro.setter
    def distro(self, distro):
        """Sets the distro of this OperatingSystem.


        :param distro: The distro of this OperatingSystem.
        :type distro: str
        """

        self._distro = distro

    @property
    def version(self):
        """Gets the version of this OperatingSystem.


        :return: The version of this OperatingSystem.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this OperatingSystem.


        :param version: The version of this OperatingSystem.
        :type version: str
        """

        self._version = version

    @property
    def provisionable_on(self):
        """Gets the provisionable_on of this OperatingSystem.


        :return: The provisionable_on of this OperatingSystem.
        :rtype: List[str]
        """
        return self._provisionable_on

    @provisionable_on.setter
    def provisionable_on(self, provisionable_on):
        """Sets the provisionable_on of this OperatingSystem.


        :param provisionable_on: The provisionable_on of this OperatingSystem.
        :type provisionable_on: List[str]
        """

        self._provisionable_on = provisionable_on