# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class ProjectCreateFromRootInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, organization_id=None, payment_method_id=None, customdata=None):  # noqa: E501
        """ProjectCreateFromRootInput - a model defined in OpenAPI

        :param name: The name of this ProjectCreateFromRootInput.  # noqa: E501
        :type name: str
        :param organization_id: The organization_id of this ProjectCreateFromRootInput.  # noqa: E501
        :type organization_id: str
        :param payment_method_id: The payment_method_id of this ProjectCreateFromRootInput.  # noqa: E501
        :type payment_method_id: str
        :param customdata: The customdata of this ProjectCreateFromRootInput.  # noqa: E501
        :type customdata: object
        """
        self.openapi_types = {
            'name': str,
            'organization_id': str,
            'payment_method_id': str,
            'customdata': object
        }

        self.attribute_map = {
            'name': 'name',
            'organization_id': 'organization_id',
            'payment_method_id': 'payment_method_id',
            'customdata': 'customdata'
        }

        self._name = name
        self._organization_id = organization_id
        self._payment_method_id = payment_method_id
        self._customdata = customdata

    @classmethod
    def from_dict(cls, dikt) -> 'ProjectCreateFromRootInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProjectCreateFromRootInput of this ProjectCreateFromRootInput.  # noqa: E501
        :rtype: ProjectCreateFromRootInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ProjectCreateFromRootInput.


        :return: The name of this ProjectCreateFromRootInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreateFromRootInput.


        :param name: The name of this ProjectCreateFromRootInput.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def organization_id(self):
        """Gets the organization_id of this ProjectCreateFromRootInput.


        :return: The organization_id of this ProjectCreateFromRootInput.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ProjectCreateFromRootInput.


        :param organization_id: The organization_id of this ProjectCreateFromRootInput.
        :type organization_id: str
        """

        self._organization_id = organization_id

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ProjectCreateFromRootInput.


        :return: The payment_method_id of this ProjectCreateFromRootInput.
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ProjectCreateFromRootInput.


        :param payment_method_id: The payment_method_id of this ProjectCreateFromRootInput.
        :type payment_method_id: str
        """

        self._payment_method_id = payment_method_id

    @property
    def customdata(self):
        """Gets the customdata of this ProjectCreateFromRootInput.


        :return: The customdata of this ProjectCreateFromRootInput.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this ProjectCreateFromRootInput.


        :param customdata: The customdata of this ProjectCreateFromRootInput.
        :type customdata: object
        """

        self._customdata = customdata
