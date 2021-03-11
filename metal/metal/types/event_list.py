# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.event import Event
from metal.types.meta import Meta
from metal import util

from metal.types.event import Event  # noqa: E501
from metal.types.meta import Meta  # noqa: E501

class EventList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, events=None, meta=None):  # noqa: E501
        """EventList - a model defined in OpenAPI

        :param events: The events of this EventList.  # noqa: E501
        :type events: List[Event]
        :param meta: The meta of this EventList.  # noqa: E501
        :type meta: Meta
        """
        self.openapi_types = {
            'events': List[Event],
            'meta': Meta
        }

        self.attribute_map = {
            'events': 'events',
            'meta': 'meta'
        }

        self._events = events
        self._meta = meta

    @classmethod
    def from_dict(cls, dikt) -> 'EventList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The EventList of this EventList.  # noqa: E501
        :rtype: EventList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def events(self):
        """Gets the events of this EventList.


        :return: The events of this EventList.
        :rtype: List[Event]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this EventList.


        :param events: The events of this EventList.
        :type events: List[Event]
        """

        self._events = events

    @property
    def meta(self):
        """Gets the meta of this EventList.


        :return: The meta of this EventList.
        :rtype: Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this EventList.


        :param meta: The meta of this EventList.
        :type meta: Meta
        """

        self._meta = meta
