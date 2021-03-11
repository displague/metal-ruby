# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.transfer_request import TransferRequest
from metal import util

from metal.types.transfer_request import TransferRequest  # noqa: E501

class TransferRequestList(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, transfers=None):  # noqa: E501
        """TransferRequestList - a model defined in OpenAPI

        :param transfers: The transfers of this TransferRequestList.  # noqa: E501
        :type transfers: List[TransferRequest]
        """
        self.openapi_types = {
            'transfers': List[TransferRequest]
        }

        self.attribute_map = {
            'transfers': 'transfers'
        }

        self._transfers = transfers

    @classmethod
    def from_dict(cls, dikt) -> 'TransferRequestList':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The TransferRequestList of this TransferRequestList.  # noqa: E501
        :rtype: TransferRequestList
        """
        return util.deserialize_model(dikt, cls)

    @property
    def transfers(self):
        """Gets the transfers of this TransferRequestList.


        :return: The transfers of this TransferRequestList.
        :rtype: List[TransferRequest]
        """
        return self._transfers

    @transfers.setter
    def transfers(self, transfers):
        """Sets the transfers of this TransferRequestList.


        :param transfers: The transfers of this TransferRequestList.
        :type transfers: List[TransferRequest]
        """

        self._transfers = transfers
