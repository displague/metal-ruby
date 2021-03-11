# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class LicenseCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, size=None, licensee_product_id=None):  # noqa: E501
        """LicenseCreateInput - a model defined in OpenAPI

        :param description: The description of this LicenseCreateInput.  # noqa: E501
        :type description: str
        :param size: The size of this LicenseCreateInput.  # noqa: E501
        :type size: float
        :param licensee_product_id: The licensee_product_id of this LicenseCreateInput.  # noqa: E501
        :type licensee_product_id: str
        """
        self.openapi_types = {
            'description': str,
            'size': float,
            'licensee_product_id': str
        }

        self.attribute_map = {
            'description': 'description',
            'size': 'size',
            'licensee_product_id': 'licensee_product_id'
        }

        self._description = description
        self._size = size
        self._licensee_product_id = licensee_product_id

    @classmethod
    def from_dict(cls, dikt) -> 'LicenseCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The LicenseCreateInput of this LicenseCreateInput.  # noqa: E501
        :rtype: LicenseCreateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this LicenseCreateInput.


        :return: The description of this LicenseCreateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LicenseCreateInput.


        :param description: The description of this LicenseCreateInput.
        :type description: str
        """

        self._description = description

    @property
    def size(self):
        """Gets the size of this LicenseCreateInput.


        :return: The size of this LicenseCreateInput.
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this LicenseCreateInput.


        :param size: The size of this LicenseCreateInput.
        :type size: float
        """

        self._size = size

    @property
    def licensee_product_id(self):
        """Gets the licensee_product_id of this LicenseCreateInput.


        :return: The licensee_product_id of this LicenseCreateInput.
        :rtype: str
        """
        return self._licensee_product_id

    @licensee_product_id.setter
    def licensee_product_id(self, licensee_product_id):
        """Sets the licensee_product_id of this LicenseCreateInput.


        :param licensee_product_id: The licensee_product_id of this LicenseCreateInput.
        :type licensee_product_id: str
        """

        self._licensee_product_id = licensee_product_id
