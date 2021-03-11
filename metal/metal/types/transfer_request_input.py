# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class TransferRequestInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, target_organization_id=None):  # noqa: E501
        """TransferRequestInput - a model defined in OpenAPI

        :param target_organization_id: The target_organization_id of this TransferRequestInput.  # noqa: E501
        :type target_organization_id: str
        """
        self.openapi_types = {
            'target_organization_id': str
        }

        self.attribute_map = {
            'target_organization_id': 'target_organization_id'
        }

        self._target_organization_id = target_organization_id

    @classmethod
    def from_dict(cls, dikt) -> 'TransferRequestInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransferRequestInput of this TransferRequestInput.  # noqa: E501
        :rtype: TransferRequestInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def target_organization_id(self):
        """Gets the target_organization_id of this TransferRequestInput.


        :return: The target_organization_id of this TransferRequestInput.
        :rtype: str
        """
        return self._target_organization_id

    @target_organization_id.setter
    def target_organization_id(self, target_organization_id):
        """Sets the target_organization_id of this TransferRequestInput.


        :param target_organization_id: The target_organization_id of this TransferRequestInput.
        :type target_organization_id: str
        """

        self._target_organization_id = target_organization_id
