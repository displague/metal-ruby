# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class SubscribableEvent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, event_type=None, event_name=None, event_slug=None):  # noqa: E501
        """SubscribableEvent - a model defined in OpenAPI

        :param id: The id of this SubscribableEvent.  # noqa: E501
        :type id: str
        :param event_type: The event_type of this SubscribableEvent.  # noqa: E501
        :type event_type: str
        :param event_name: The event_name of this SubscribableEvent.  # noqa: E501
        :type event_name: str
        :param event_slug: The event_slug of this SubscribableEvent.  # noqa: E501
        :type event_slug: str
        """
        self.openapi_types = {
            'id': str,
            'event_type': str,
            'event_name': str,
            'event_slug': str
        }

        self.attribute_map = {
            'id': 'id',
            'event_type': 'event_type',
            'event_name': 'event_name',
            'event_slug': 'event_slug'
        }

        self._id = id
        self._event_type = event_type
        self._event_name = event_name
        self._event_slug = event_slug

    @classmethod
    def from_dict(cls, dikt) -> 'SubscribableEvent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The SubscribableEvent of this SubscribableEvent.  # noqa: E501
        :rtype: SubscribableEvent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this SubscribableEvent.


        :return: The id of this SubscribableEvent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscribableEvent.


        :param id: The id of this SubscribableEvent.
        :type id: str
        """

        self._id = id

    @property
    def event_type(self):
        """Gets the event_type of this SubscribableEvent.


        :return: The event_type of this SubscribableEvent.
        :rtype: str
        """
        return self._event_type

    @event_type.setter
    def event_type(self, event_type):
        """Sets the event_type of this SubscribableEvent.


        :param event_type: The event_type of this SubscribableEvent.
        :type event_type: str
        """

        self._event_type = event_type

    @property
    def event_name(self):
        """Gets the event_name of this SubscribableEvent.


        :return: The event_name of this SubscribableEvent.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this SubscribableEvent.


        :param event_name: The event_name of this SubscribableEvent.
        :type event_name: str
        """

        self._event_name = event_name

    @property
    def event_slug(self):
        """Gets the event_slug of this SubscribableEvent.


        :return: The event_slug of this SubscribableEvent.
        :rtype: str
        """
        return self._event_slug

    @event_slug.setter
    def event_slug(self, event_slug):
        """Sets the event_slug of this SubscribableEvent.


        :param event_slug: The event_slug of this SubscribableEvent.
        :type event_slug: str
        """

        self._event_slug = event_slug
