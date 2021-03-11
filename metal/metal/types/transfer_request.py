# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.href import Href
from metal import util

from metal.types.href import Href  # noqa: E501

class TransferRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, created_at=None, updated_at=None, target_organization=None, project=None, href=None):  # noqa: E501
        """TransferRequest - a model defined in OpenAPI

        :param id: The id of this TransferRequest.  # noqa: E501
        :type id: str
        :param created_at: The created_at of this TransferRequest.  # noqa: E501
        :type created_at: datetime
        :param updated_at: The updated_at of this TransferRequest.  # noqa: E501
        :type updated_at: datetime
        :param target_organization: The target_organization of this TransferRequest.  # noqa: E501
        :type target_organization: Href
        :param project: The project of this TransferRequest.  # noqa: E501
        :type project: Href
        :param href: The href of this TransferRequest.  # noqa: E501
        :type href: str
        """
        self.openapi_types = {
            'id': str,
            'created_at': datetime,
            'updated_at': datetime,
            'target_organization': Href,
            'project': Href,
            'href': str
        }

        self.attribute_map = {
            'id': 'id',
            'created_at': 'created_at',
            'updated_at': 'updated_at',
            'target_organization': 'target_organization',
            'project': 'project',
            'href': 'href'
        }

        self._id = id
        self._created_at = created_at
        self._updated_at = updated_at
        self._target_organization = target_organization
        self._project = project
        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'TransferRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransferRequest of this TransferRequest.  # noqa: E501
        :rtype: TransferRequest
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this TransferRequest.


        :return: The id of this TransferRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransferRequest.


        :param id: The id of this TransferRequest.
        :type id: str
        """

        self._id = id

    @property
    def created_at(self):
        """Gets the created_at of this TransferRequest.


        :return: The created_at of this TransferRequest.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TransferRequest.


        :param created_at: The created_at of this TransferRequest.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TransferRequest.


        :return: The updated_at of this TransferRequest.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TransferRequest.


        :param updated_at: The updated_at of this TransferRequest.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def target_organization(self):
        """Gets the target_organization of this TransferRequest.


        :return: The target_organization of this TransferRequest.
        :rtype: Href
        """
        return self._target_organization

    @target_organization.setter
    def target_organization(self, target_organization):
        """Sets the target_organization of this TransferRequest.


        :param target_organization: The target_organization of this TransferRequest.
        :type target_organization: Href
        """

        self._target_organization = target_organization

    @property
    def project(self):
        """Gets the project of this TransferRequest.


        :return: The project of this TransferRequest.
        :rtype: Href
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this TransferRequest.


        :param project: The project of this TransferRequest.
        :type project: Href
        """

        self._project = project

    @property
    def href(self):
        """Gets the href of this TransferRequest.


        :return: The href of this TransferRequest.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this TransferRequest.


        :param href: The href of this TransferRequest.
        :type href: str
        """

        self._href = href
