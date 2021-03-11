# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.snapshot_policy_input import SnapshotPolicyInput
from metal import util

from metal.types.snapshot_policy_input import SnapshotPolicyInput  # noqa: E501

class VolumeCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description=None, facility=None, plan=None, size=None, locked=None, billing_cycle=None, snapshot_policies=None, customdata=None):  # noqa: E501
        """VolumeCreateInput - a model defined in OpenAPI

        :param description: The description of this VolumeCreateInput.  # noqa: E501
        :type description: str
        :param facility: The facility of this VolumeCreateInput.  # noqa: E501
        :type facility: str
        :param plan: The plan of this VolumeCreateInput.  # noqa: E501
        :type plan: str
        :param size: The size of this VolumeCreateInput.  # noqa: E501
        :type size: int
        :param locked: The locked of this VolumeCreateInput.  # noqa: E501
        :type locked: bool
        :param billing_cycle: The billing_cycle of this VolumeCreateInput.  # noqa: E501
        :type billing_cycle: str
        :param snapshot_policies: The snapshot_policies of this VolumeCreateInput.  # noqa: E501
        :type snapshot_policies: SnapshotPolicyInput
        :param customdata: The customdata of this VolumeCreateInput.  # noqa: E501
        :type customdata: object
        """
        self.openapi_types = {
            'description': str,
            'facility': str,
            'plan': str,
            'size': int,
            'locked': bool,
            'billing_cycle': str,
            'snapshot_policies': SnapshotPolicyInput,
            'customdata': object
        }

        self.attribute_map = {
            'description': 'description',
            'facility': 'facility',
            'plan': 'plan',
            'size': 'size',
            'locked': 'locked',
            'billing_cycle': 'billing_cycle',
            'snapshot_policies': 'snapshot_policies',
            'customdata': 'customdata'
        }

        self._description = description
        self._facility = facility
        self._plan = plan
        self._size = size
        self._locked = locked
        self._billing_cycle = billing_cycle
        self._snapshot_policies = snapshot_policies
        self._customdata = customdata

    @classmethod
    def from_dict(cls, dikt) -> 'VolumeCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VolumeCreateInput of this VolumeCreateInput.  # noqa: E501
        :rtype: VolumeCreateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this VolumeCreateInput.


        :return: The description of this VolumeCreateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VolumeCreateInput.


        :param description: The description of this VolumeCreateInput.
        :type description: str
        """

        self._description = description

    @property
    def facility(self):
        """Gets the facility of this VolumeCreateInput.

        ams1, ewr1, nrt1, sjc1  # noqa: E501

        :return: The facility of this VolumeCreateInput.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this VolumeCreateInput.

        ams1, ewr1, nrt1, sjc1  # noqa: E501

        :param facility: The facility of this VolumeCreateInput.
        :type facility: str
        """
        if facility is None:
            raise ValueError("Invalid value for `facility`, must not be `None`")  # noqa: E501

        self._facility = facility

    @property
    def plan(self):
        """Gets the plan of this VolumeCreateInput.

        storage_1, storage_2  # noqa: E501

        :return: The plan of this VolumeCreateInput.
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this VolumeCreateInput.

        storage_1, storage_2  # noqa: E501

        :param plan: The plan of this VolumeCreateInput.
        :type plan: str
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")  # noqa: E501

        self._plan = plan

    @property
    def size(self):
        """Gets the size of this VolumeCreateInput.


        :return: The size of this VolumeCreateInput.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this VolumeCreateInput.


        :param size: The size of this VolumeCreateInput.
        :type size: int
        """
        if size is None:
            raise ValueError("Invalid value for `size`, must not be `None`")  # noqa: E501

        self._size = size

    @property
    def locked(self):
        """Gets the locked of this VolumeCreateInput.


        :return: The locked of this VolumeCreateInput.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this VolumeCreateInput.


        :param locked: The locked of this VolumeCreateInput.
        :type locked: bool
        """

        self._locked = locked

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this VolumeCreateInput.

        hourly  # noqa: E501

        :return: The billing_cycle of this VolumeCreateInput.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this VolumeCreateInput.

        hourly  # noqa: E501

        :param billing_cycle: The billing_cycle of this VolumeCreateInput.
        :type billing_cycle: str
        """

        self._billing_cycle = billing_cycle

    @property
    def snapshot_policies(self):
        """Gets the snapshot_policies of this VolumeCreateInput.


        :return: The snapshot_policies of this VolumeCreateInput.
        :rtype: SnapshotPolicyInput
        """
        return self._snapshot_policies

    @snapshot_policies.setter
    def snapshot_policies(self, snapshot_policies):
        """Sets the snapshot_policies of this VolumeCreateInput.


        :param snapshot_policies: The snapshot_policies of this VolumeCreateInput.
        :type snapshot_policies: SnapshotPolicyInput
        """

        self._snapshot_policies = snapshot_policies

    @property
    def customdata(self):
        """Gets the customdata of this VolumeCreateInput.


        :return: The customdata of this VolumeCreateInput.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this VolumeCreateInput.


        :param customdata: The customdata of this VolumeCreateInput.
        :type customdata: object
        """

        self._customdata = customdata