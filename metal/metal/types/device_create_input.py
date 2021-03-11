# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.device_create_input_ip_addresses import DeviceCreateInputIpAddresses
from metal import util

from metal.types.device_create_input_ip_addresses import DeviceCreateInputIpAddresses  # noqa: E501

class DeviceCreateInput(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, facility=None, plan=None, hostname=None, description=None, billing_cycle=None, operating_system=None, always_pxe=None, ipxe_script_url=None, userdata=None, locked=None, customdata=None, hardware_reservation_id=None, spot_instance=None, spot_price_max=None, termination_time=None, tags=None, project_ssh_keys=None, user_ssh_keys=None, features=None, public_ipv4_subnet_size=None, private_ipv4_subnet_size=None, ip_addresses=None):  # noqa: E501
        """DeviceCreateInput - a model defined in OpenAPI

        :param facility: The facility of this DeviceCreateInput.  # noqa: E501
        :type facility: str
        :param plan: The plan of this DeviceCreateInput.  # noqa: E501
        :type plan: str
        :param hostname: The hostname of this DeviceCreateInput.  # noqa: E501
        :type hostname: str
        :param description: The description of this DeviceCreateInput.  # noqa: E501
        :type description: str
        :param billing_cycle: The billing_cycle of this DeviceCreateInput.  # noqa: E501
        :type billing_cycle: str
        :param operating_system: The operating_system of this DeviceCreateInput.  # noqa: E501
        :type operating_system: str
        :param always_pxe: The always_pxe of this DeviceCreateInput.  # noqa: E501
        :type always_pxe: bool
        :param ipxe_script_url: The ipxe_script_url of this DeviceCreateInput.  # noqa: E501
        :type ipxe_script_url: str
        :param userdata: The userdata of this DeviceCreateInput.  # noqa: E501
        :type userdata: str
        :param locked: The locked of this DeviceCreateInput.  # noqa: E501
        :type locked: bool
        :param customdata: The customdata of this DeviceCreateInput.  # noqa: E501
        :type customdata: object
        :param hardware_reservation_id: The hardware_reservation_id of this DeviceCreateInput.  # noqa: E501
        :type hardware_reservation_id: str
        :param spot_instance: The spot_instance of this DeviceCreateInput.  # noqa: E501
        :type spot_instance: bool
        :param spot_price_max: The spot_price_max of this DeviceCreateInput.  # noqa: E501
        :type spot_price_max: float
        :param termination_time: The termination_time of this DeviceCreateInput.  # noqa: E501
        :type termination_time: datetime
        :param tags: The tags of this DeviceCreateInput.  # noqa: E501
        :type tags: List[str]
        :param project_ssh_keys: The project_ssh_keys of this DeviceCreateInput.  # noqa: E501
        :type project_ssh_keys: List[str]
        :param user_ssh_keys: The user_ssh_keys of this DeviceCreateInput.  # noqa: E501
        :type user_ssh_keys: List[str]
        :param features: The features of this DeviceCreateInput.  # noqa: E501
        :type features: List[str]
        :param public_ipv4_subnet_size: The public_ipv4_subnet_size of this DeviceCreateInput.  # noqa: E501
        :type public_ipv4_subnet_size: float
        :param private_ipv4_subnet_size: The private_ipv4_subnet_size of this DeviceCreateInput.  # noqa: E501
        :type private_ipv4_subnet_size: float
        :param ip_addresses: The ip_addresses of this DeviceCreateInput.  # noqa: E501
        :type ip_addresses: List[DeviceCreateInputIpAddresses]
        """
        self.openapi_types = {
            'facility': str,
            'plan': str,
            'hostname': str,
            'description': str,
            'billing_cycle': str,
            'operating_system': str,
            'always_pxe': bool,
            'ipxe_script_url': str,
            'userdata': str,
            'locked': bool,
            'customdata': object,
            'hardware_reservation_id': str,
            'spot_instance': bool,
            'spot_price_max': float,
            'termination_time': datetime,
            'tags': List[str],
            'project_ssh_keys': List[str],
            'user_ssh_keys': List[str],
            'features': List[str],
            'public_ipv4_subnet_size': float,
            'private_ipv4_subnet_size': float,
            'ip_addresses': List[DeviceCreateInputIpAddresses]
        }

        self.attribute_map = {
            'facility': 'facility',
            'plan': 'plan',
            'hostname': 'hostname',
            'description': 'description',
            'billing_cycle': 'billing_cycle',
            'operating_system': 'operating_system',
            'always_pxe': 'always_pxe',
            'ipxe_script_url': 'ipxe_script_url',
            'userdata': 'userdata',
            'locked': 'locked',
            'customdata': 'customdata',
            'hardware_reservation_id': 'hardware_reservation_id',
            'spot_instance': 'spot_instance',
            'spot_price_max': 'spot_price_max',
            'termination_time': 'termination_time',
            'tags': 'tags',
            'project_ssh_keys': 'project_ssh_keys',
            'user_ssh_keys': 'user_ssh_keys',
            'features': 'features',
            'public_ipv4_subnet_size': 'public_ipv4_subnet_size',
            'private_ipv4_subnet_size': 'private_ipv4_subnet_size',
            'ip_addresses': 'ip_addresses'
        }

        self._facility = facility
        self._plan = plan
        self._hostname = hostname
        self._description = description
        self._billing_cycle = billing_cycle
        self._operating_system = operating_system
        self._always_pxe = always_pxe
        self._ipxe_script_url = ipxe_script_url
        self._userdata = userdata
        self._locked = locked
        self._customdata = customdata
        self._hardware_reservation_id = hardware_reservation_id
        self._spot_instance = spot_instance
        self._spot_price_max = spot_price_max
        self._termination_time = termination_time
        self._tags = tags
        self._project_ssh_keys = project_ssh_keys
        self._user_ssh_keys = user_ssh_keys
        self._features = features
        self._public_ipv4_subnet_size = public_ipv4_subnet_size
        self._private_ipv4_subnet_size = private_ipv4_subnet_size
        self._ip_addresses = ip_addresses

    @classmethod
    def from_dict(cls, dikt) -> 'DeviceCreateInput':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DeviceCreateInput of this DeviceCreateInput.  # noqa: E501
        :rtype: DeviceCreateInput
        """
        return util.deserialize_model(dikt, cls)

    @property
    def facility(self):
        """Gets the facility of this DeviceCreateInput.


        :return: The facility of this DeviceCreateInput.
        :rtype: str
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this DeviceCreateInput.


        :param facility: The facility of this DeviceCreateInput.
        :type facility: str
        """
        if facility is None:
            raise ValueError("Invalid value for `facility`, must not be `None`")  # noqa: E501

        self._facility = facility

    @property
    def plan(self):
        """Gets the plan of this DeviceCreateInput.


        :return: The plan of this DeviceCreateInput.
        :rtype: str
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this DeviceCreateInput.


        :param plan: The plan of this DeviceCreateInput.
        :type plan: str
        """
        if plan is None:
            raise ValueError("Invalid value for `plan`, must not be `None`")  # noqa: E501

        self._plan = plan

    @property
    def hostname(self):
        """Gets the hostname of this DeviceCreateInput.


        :return: The hostname of this DeviceCreateInput.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """Sets the hostname of this DeviceCreateInput.


        :param hostname: The hostname of this DeviceCreateInput.
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def description(self):
        """Gets the description of this DeviceCreateInput.


        :return: The description of this DeviceCreateInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DeviceCreateInput.


        :param description: The description of this DeviceCreateInput.
        :type description: str
        """

        self._description = description

    @property
    def billing_cycle(self):
        """Gets the billing_cycle of this DeviceCreateInput.


        :return: The billing_cycle of this DeviceCreateInput.
        :rtype: str
        """
        return self._billing_cycle

    @billing_cycle.setter
    def billing_cycle(self, billing_cycle):
        """Sets the billing_cycle of this DeviceCreateInput.


        :param billing_cycle: The billing_cycle of this DeviceCreateInput.
        :type billing_cycle: str
        """

        self._billing_cycle = billing_cycle

    @property
    def operating_system(self):
        """Gets the operating_system of this DeviceCreateInput.


        :return: The operating_system of this DeviceCreateInput.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system):
        """Sets the operating_system of this DeviceCreateInput.


        :param operating_system: The operating_system of this DeviceCreateInput.
        :type operating_system: str
        """
        if operating_system is None:
            raise ValueError("Invalid value for `operating_system`, must not be `None`")  # noqa: E501

        self._operating_system = operating_system

    @property
    def always_pxe(self):
        """Gets the always_pxe of this DeviceCreateInput.


        :return: The always_pxe of this DeviceCreateInput.
        :rtype: bool
        """
        return self._always_pxe

    @always_pxe.setter
    def always_pxe(self, always_pxe):
        """Sets the always_pxe of this DeviceCreateInput.


        :param always_pxe: The always_pxe of this DeviceCreateInput.
        :type always_pxe: bool
        """

        self._always_pxe = always_pxe

    @property
    def ipxe_script_url(self):
        """Gets the ipxe_script_url of this DeviceCreateInput.


        :return: The ipxe_script_url of this DeviceCreateInput.
        :rtype: str
        """
        return self._ipxe_script_url

    @ipxe_script_url.setter
    def ipxe_script_url(self, ipxe_script_url):
        """Sets the ipxe_script_url of this DeviceCreateInput.


        :param ipxe_script_url: The ipxe_script_url of this DeviceCreateInput.
        :type ipxe_script_url: str
        """

        self._ipxe_script_url = ipxe_script_url

    @property
    def userdata(self):
        """Gets the userdata of this DeviceCreateInput.


        :return: The userdata of this DeviceCreateInput.
        :rtype: str
        """
        return self._userdata

    @userdata.setter
    def userdata(self, userdata):
        """Sets the userdata of this DeviceCreateInput.


        :param userdata: The userdata of this DeviceCreateInput.
        :type userdata: str
        """

        self._userdata = userdata

    @property
    def locked(self):
        """Gets the locked of this DeviceCreateInput.


        :return: The locked of this DeviceCreateInput.
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this DeviceCreateInput.


        :param locked: The locked of this DeviceCreateInput.
        :type locked: bool
        """

        self._locked = locked

    @property
    def customdata(self):
        """Gets the customdata of this DeviceCreateInput.


        :return: The customdata of this DeviceCreateInput.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this DeviceCreateInput.


        :param customdata: The customdata of this DeviceCreateInput.
        :type customdata: object
        """

        self._customdata = customdata

    @property
    def hardware_reservation_id(self):
        """Gets the hardware_reservation_id of this DeviceCreateInput.


        :return: The hardware_reservation_id of this DeviceCreateInput.
        :rtype: str
        """
        return self._hardware_reservation_id

    @hardware_reservation_id.setter
    def hardware_reservation_id(self, hardware_reservation_id):
        """Sets the hardware_reservation_id of this DeviceCreateInput.


        :param hardware_reservation_id: The hardware_reservation_id of this DeviceCreateInput.
        :type hardware_reservation_id: str
        """

        self._hardware_reservation_id = hardware_reservation_id

    @property
    def spot_instance(self):
        """Gets the spot_instance of this DeviceCreateInput.


        :return: The spot_instance of this DeviceCreateInput.
        :rtype: bool
        """
        return self._spot_instance

    @spot_instance.setter
    def spot_instance(self, spot_instance):
        """Sets the spot_instance of this DeviceCreateInput.


        :param spot_instance: The spot_instance of this DeviceCreateInput.
        :type spot_instance: bool
        """

        self._spot_instance = spot_instance

    @property
    def spot_price_max(self):
        """Gets the spot_price_max of this DeviceCreateInput.


        :return: The spot_price_max of this DeviceCreateInput.
        :rtype: float
        """
        return self._spot_price_max

    @spot_price_max.setter
    def spot_price_max(self, spot_price_max):
        """Sets the spot_price_max of this DeviceCreateInput.


        :param spot_price_max: The spot_price_max of this DeviceCreateInput.
        :type spot_price_max: float
        """

        self._spot_price_max = spot_price_max

    @property
    def termination_time(self):
        """Gets the termination_time of this DeviceCreateInput.


        :return: The termination_time of this DeviceCreateInput.
        :rtype: datetime
        """
        return self._termination_time

    @termination_time.setter
    def termination_time(self, termination_time):
        """Sets the termination_time of this DeviceCreateInput.


        :param termination_time: The termination_time of this DeviceCreateInput.
        :type termination_time: datetime
        """

        self._termination_time = termination_time

    @property
    def tags(self):
        """Gets the tags of this DeviceCreateInput.


        :return: The tags of this DeviceCreateInput.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this DeviceCreateInput.


        :param tags: The tags of this DeviceCreateInput.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def project_ssh_keys(self):
        """Gets the project_ssh_keys of this DeviceCreateInput.


        :return: The project_ssh_keys of this DeviceCreateInput.
        :rtype: List[str]
        """
        return self._project_ssh_keys

    @project_ssh_keys.setter
    def project_ssh_keys(self, project_ssh_keys):
        """Sets the project_ssh_keys of this DeviceCreateInput.


        :param project_ssh_keys: The project_ssh_keys of this DeviceCreateInput.
        :type project_ssh_keys: List[str]
        """

        self._project_ssh_keys = project_ssh_keys

    @property
    def user_ssh_keys(self):
        """Gets the user_ssh_keys of this DeviceCreateInput.

        The UUIDs of users whose SSH keys should be included on the provisioned device.  # noqa: E501

        :return: The user_ssh_keys of this DeviceCreateInput.
        :rtype: List[str]
        """
        return self._user_ssh_keys

    @user_ssh_keys.setter
    def user_ssh_keys(self, user_ssh_keys):
        """Sets the user_ssh_keys of this DeviceCreateInput.

        The UUIDs of users whose SSH keys should be included on the provisioned device.  # noqa: E501

        :param user_ssh_keys: The user_ssh_keys of this DeviceCreateInput.
        :type user_ssh_keys: List[str]
        """

        self._user_ssh_keys = user_ssh_keys

    @property
    def features(self):
        """Gets the features of this DeviceCreateInput.


        :return: The features of this DeviceCreateInput.
        :rtype: List[str]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this DeviceCreateInput.


        :param features: The features of this DeviceCreateInput.
        :type features: List[str]
        """

        self._features = features

    @property
    def public_ipv4_subnet_size(self):
        """Gets the public_ipv4_subnet_size of this DeviceCreateInput.

        Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request.  # noqa: E501

        :return: The public_ipv4_subnet_size of this DeviceCreateInput.
        :rtype: float
        """
        return self._public_ipv4_subnet_size

    @public_ipv4_subnet_size.setter
    def public_ipv4_subnet_size(self, public_ipv4_subnet_size):
        """Sets the public_ipv4_subnet_size of this DeviceCreateInput.

        Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device. Your project must have addresses available for a non-default request.  # noqa: E501

        :param public_ipv4_subnet_size: The public_ipv4_subnet_size of this DeviceCreateInput.
        :type public_ipv4_subnet_size: float
        """

        self._public_ipv4_subnet_size = public_ipv4_subnet_size

    @property
    def private_ipv4_subnet_size(self):
        """Gets the private_ipv4_subnet_size of this DeviceCreateInput.

        Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device.  # noqa: E501

        :return: The private_ipv4_subnet_size of this DeviceCreateInput.
        :rtype: float
        """
        return self._private_ipv4_subnet_size

    @private_ipv4_subnet_size.setter
    def private_ipv4_subnet_size(self, private_ipv4_subnet_size):
        """Sets the private_ipv4_subnet_size of this DeviceCreateInput.

        Deprecated. Use ip_addresses. Subnet range for addresses allocated to this device.  # noqa: E501

        :param private_ipv4_subnet_size: The private_ipv4_subnet_size of this DeviceCreateInput.
        :type private_ipv4_subnet_size: float
        """

        self._private_ipv4_subnet_size = private_ipv4_subnet_size

    @property
    def ip_addresses(self):
        """Gets the ip_addresses of this DeviceCreateInput.


        :return: The ip_addresses of this DeviceCreateInput.
        :rtype: List[DeviceCreateInputIpAddresses]
        """
        return self._ip_addresses

    @ip_addresses.setter
    def ip_addresses(self, ip_addresses):
        """Sets the ip_addresses of this DeviceCreateInput.


        :param ip_addresses: The ip_addresses of this DeviceCreateInput.
        :type ip_addresses: List[DeviceCreateInputIpAddresses]
        """

        self._ip_addresses = ip_addresses