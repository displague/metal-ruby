# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class ProjectCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, payment_method_id=None, customdata=None):  # noqa: E501
        """ProjectCreateInput - a model defined in OpenAPI

        :param name: The name of this ProjectCreateInput.  # noqa: E501
        :type name: str
        :param payment_method_id: The payment_method_id of this ProjectCreateInput.  # noqa: E501
        :type payment_method_id: str
        :param customdata: The customdata of this ProjectCreateInput.  # noqa: E501
        :type customdata: object
        """
        self.openapi_types = {
            'name': str,
            'payment_method_id': str,
            'customdata': object
        }

        self.attribute_map = {
            'name': 'name',
            'payment_method_id': 'payment_method_id',
            'customdata': 'customdata'
        }

        self._name = name
        self._payment_method_id = payment_method_id
        self._customdata = customdata

    @classmethod
    def from_dict(cls, dikt) -> 'ProjectCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The ProjectCreateInput of this ProjectCreateInput.  # noqa: E501
        :rtype: ProjectCreateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ProjectCreateInput.


        :return: The name of this ProjectCreateInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectCreateInput.


        :param name: The name of this ProjectCreateInput.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def payment_method_id(self):
        """Gets the payment_method_id of this ProjectCreateInput.


        :return: The payment_method_id of this ProjectCreateInput.
        :rtype: str
        """
        return self._payment_method_id

    @payment_method_id.setter
    def payment_method_id(self, payment_method_id):
        """Sets the payment_method_id of this ProjectCreateInput.


        :param payment_method_id: The payment_method_id of this ProjectCreateInput.
        :type payment_method_id: str
        """

        self._payment_method_id = payment_method_id

    @property
    def customdata(self):
        """Gets the customdata of this ProjectCreateInput.


        :return: The customdata of this ProjectCreateInput.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this ProjectCreateInput.


        :param customdata: The customdata of this ProjectCreateInput.
        :type customdata: object
        """

        self._customdata = customdata
