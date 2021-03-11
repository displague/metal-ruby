# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.event_type import EventType
from metal import util

from metal.types.event_type import EventType  # noqa: E501

class EventTypeList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, event_types=None):  # noqa: E501
        """EventTypeList - a model defined in OpenAPI

        :param event_types: The event_types of this EventTypeList.  # noqa: E501
        :type event_types: List[EventType]
        """
        self.openapi_types = {
            'event_types': List[EventType]
        }

        self.attribute_map = {
            'event_types': 'event_types'
        }

        self._event_types = event_types

    @classmethod
    def from_dict(cls, dikt) -> 'EventTypeList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventTypeList of this EventTypeList.  # noqa: E501
        :rtype: EventTypeList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def event_types(self):
        """Gets the event_types of this EventTypeList.


        :return: The event_types of this EventTypeList.
        :rtype: List[EventType]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this EventTypeList.


        :param event_types: The event_types of this EventTypeList.
        :type event_types: List[EventType]
        """

        self._event_types = event_types