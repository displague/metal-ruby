# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal import util


class VolumeAttachmentInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device_id=None):  # noqa: E501
        """VolumeAttachmentInput - a model defined in OpenAPI

        :param device_id: The device_id of this VolumeAttachmentInput.  # noqa: E501
        :type device_id: str
        """
        self.openapi_types = {
            'device_id': str
        }

        self.attribute_map = {
            'device_id': 'device_id'
        }

        self._device_id = device_id

    @classmethod
    def from_dict(cls, dikt) -> 'VolumeAttachmentInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VolumeAttachmentInput of this VolumeAttachmentInput.  # noqa: E501
        :rtype: VolumeAttachmentInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device_id(self):
        """Gets the device_id of this VolumeAttachmentInput.


        :return: The device_id of this VolumeAttachmentInput.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this VolumeAttachmentInput.


        :param device_id: The device_id of this VolumeAttachmentInput.
        :type device_id: str
        """
        if device_id is None:
            raise ValueError("Invalid value for `device_id`, must not be `None`")  # noqa: E501

        self._device_id = device_id