# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.meta import Meta
from metal.types.project import Project
from metal import util

from metal.types.meta import Meta  # noqa: E501
from metal.types.project import Project  # noqa: E501

class ProjectList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, projects=None, meta=None):  # noqa: E501
        """ProjectList - a model defined in OpenAPI

        :param projects: The projects of this ProjectList.  # noqa: E501
        :type projects: List[Project]
        :param meta: The meta of this ProjectList.  # noqa: E501
        :type meta: Meta
        """
        self.openapi_types = {
            'projects': List[Project],
            'meta': Meta
        }

        self.attribute_map = {
            'projects': 'projects',
            'meta': 'meta'
        }

        self._projects = projects
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'ProjectList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProjectList of this ProjectList.  # noqa: E501
        :rtype: ProjectList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def projects(self):
        """Gets the projects of this ProjectList.


        :return: The projects of this ProjectList.
        :rtype: List[Project]
        """
        return self._projects

    @projects.setter
    def projects(self, projects):
        """Sets the projects of this ProjectList.


        :param projects: The projects of this ProjectList.
        :type projects: List[Project]
        """

        self._projects = projects

    @property
    def meta(self):
        """Gets the meta of this ProjectList.


        :return: The meta of this ProjectList.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this ProjectList.


        :param meta: The meta of this ProjectList.
        :type meta: Meta
        """

        self._meta = meta