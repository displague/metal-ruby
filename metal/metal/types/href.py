# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class Href(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, href=None):  # noqa: E501
        """Href - a model defined in OpenAPI

        :param href: The href of this Href.  # noqa: E501
        :type href: str
        """
        self.openapi_types = {
            'href': str
        }

        self.attribute_map = {
            'href': 'href'
        }

        self._href = href

    @classmethod
    def from_dict(cls, dikt) -> 'Href':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Href of this Href.  # noqa: E501
        :rtype: Href
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self):
        """Gets the href of this Href.


        :return: The href of this Href.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this Href.


        :param href: The href of this Href.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href
