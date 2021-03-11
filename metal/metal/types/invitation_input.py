# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class InvitationInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, invitee=None, message=None, roles=None, projects_ids=None):  # noqa: E501
        """InvitationInput - a model defined in OpenAPI

        :param invitee: The invitee of this InvitationInput.  # noqa: E501
        :type invitee: str
        :param message: The message of this InvitationInput.  # noqa: E501
        :type message: str
        :param roles: The roles of this InvitationInput.  # noqa: E501
        :type roles: List[str]
        :param projects_ids: The projects_ids of this InvitationInput.  # noqa: E501
        :type projects_ids: List[str]
        """
        self.openapi_types = {
            'invitee': str,
            'message': str,
            'roles': List[str],
            'projects_ids': List[str]
        }

        self.attribute_map = {
            'invitee': 'invitee',
            'message': 'message',
            'roles': 'roles',
            'projects_ids': 'projects_ids'
        }

        self._invitee = invitee
        self._message = message
        self._roles = roles
        self._projects_ids = projects_ids

    @classmethod
    def from_dict(cls, dikt) -> 'InvitationInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvitationInput of this InvitationInput.  # noqa: E501
        :rtype: InvitationInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def invitee(self):
        """Gets the invitee of this InvitationInput.


        :return: The invitee of this InvitationInput.
        :rtype: str
        """
        return self._invitee

    @invitee.setter
    def invitee(self, invitee):
        """Sets the invitee of this InvitationInput.


        :param invitee: The invitee of this InvitationInput.
        :type invitee: str
        """
        if invitee is None:
            raise ValueError("Invalid value for `invitee`, must not be `None`")  # noqa: E501

        self._invitee = invitee

    @property
    def message(self):
        """Gets the message of this InvitationInput.


        :return: The message of this InvitationInput.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this InvitationInput.


        :param message: The message of this InvitationInput.
        :type message: str
        """

        self._message = message

    @property
    def roles(self):
        """Gets the roles of this InvitationInput.


        :return: The roles of this InvitationInput.
        :rtype: List[str]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        """Sets the roles of this InvitationInput.


        :param roles: The roles of this InvitationInput.
        :type roles: List[str]
        """

        self._roles = roles

    @property
    def projects_ids(self):
        """Gets the projects_ids of this InvitationInput.


        :return: The projects_ids of this InvitationInput.
        :rtype: List[str]
        """
        return self._projects_ids

    @projects_ids.setter
    def projects_ids(self, projects_ids):
        """Sets the projects_ids of this InvitationInput.


        :param projects_ids: The projects_ids of this InvitationInput.
        :type projects_ids: List[str]
        """

        self._projects_ids = projects_ids
