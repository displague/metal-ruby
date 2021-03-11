# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


import inspect
import pprint
import re  # noqa: F401
import six

from metal.configuration import Configuration


class StaffHardwareCreateInput(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'state': 'str',
        'u_spaces': 'int',
        'model_number': 'str',
        'serial_number': 'str',
        'server_rack_id': 'str',
        'leased': 'bool',
        'lease_number': 'str',
        'lease_expires_at': 'datetime',
        'arch': 'str',
        'dhcp_group': 'str',
        'efi_boot': 'bool',
        'bios_password': 'str',
        'maintenance_state': 'str',
        'name': 'str',
        'static_name': 'str',
        'uefi_supports_rfc3021': 'bool',
        'link_aggregation': 'str',
        'provisioner': 'str',
        'supported_networking': 'list[str]',
        'services': 'object',
        'management': 'object',
        'data': 'object',
        'role': 'str',
        'vlan_id': 'int',
        'tpm': 'bool',
        'switch_short_id': 'str',
        'is_primary': 'bool',
        'loopback_ip': 'str',
        'vrf': 'str',
        'exclude_from_narwhal': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'state': 'state',
        'u_spaces': 'u_spaces',
        'model_number': 'model_number',
        'serial_number': 'serial_number',
        'server_rack_id': 'server_rack_id',
        'leased': 'leased',
        'lease_number': 'lease_number',
        'lease_expires_at': 'lease_expires_at',
        'arch': 'arch',
        'dhcp_group': 'dhcp_group',
        'efi_boot': 'efi_boot',
        'bios_password': 'bios_password',
        'maintenance_state': 'maintenance_state',
        'name': 'name',
        'static_name': 'static_name',
        'uefi_supports_rfc3021': 'uefi_supports_rfc3021',
        'link_aggregation': 'link_aggregation',
        'provisioner': 'provisioner',
        'supported_networking': 'supported_networking',
        'services': 'services',
        'management': 'management',
        'data': 'data',
        'role': 'role',
        'vlan_id': 'vlan_id',
        'tpm': 'tpm',
        'switch_short_id': 'switch_short_id',
        'is_primary': 'is_primary',
        'loopback_ip': 'loopback_ip',
        'vrf': 'vrf',
        'exclude_from_narwhal': 'exclude_from_narwhal'
    }

    def __init__(self, type=None, state=None, u_spaces=None, model_number=None, serial_number=None, server_rack_id=None, leased=None, lease_number=None, lease_expires_at=None, arch=None, dhcp_group=None, efi_boot=None, bios_password=None, maintenance_state=None, name=None, static_name=None, uefi_supports_rfc3021=None, link_aggregation=None, provisioner=None, supported_networking=None, services=None, management=None, data=None, role=None, vlan_id=None, tpm=None, switch_short_id=None, is_primary=None, loopback_ip=None, vrf=None, exclude_from_narwhal=None, local_vars_configuration=None):  # noqa: E501
        """StaffHardwareCreateInput - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._state = None
        self._u_spaces = None
        self._model_number = None
        self._serial_number = None
        self._server_rack_id = None
        self._leased = None
        self._lease_number = None
        self._lease_expires_at = None
        self._arch = None
        self._dhcp_group = None
        self._efi_boot = None
        self._bios_password = None
        self._maintenance_state = None
        self._name = None
        self._static_name = None
        self._uefi_supports_rfc3021 = None
        self._link_aggregation = None
        self._provisioner = None
        self._supported_networking = None
        self._services = None
        self._management = None
        self._data = None
        self._role = None
        self._vlan_id = None
        self._tpm = None
        self._switch_short_id = None
        self._is_primary = None
        self._loopback_ip = None
        self._vrf = None
        self._exclude_from_narwhal = None
        self.discriminator = None

        self.type = type
        if state is not None:
            self.state = state
        if u_spaces is not None:
            self.u_spaces = u_spaces
        self.model_number = model_number
        if serial_number is not None:
            self.serial_number = serial_number
        if server_rack_id is not None:
            self.server_rack_id = server_rack_id
        if leased is not None:
            self.leased = leased
        if lease_number is not None:
            self.lease_number = lease_number
        if lease_expires_at is not None:
            self.lease_expires_at = lease_expires_at
        if arch is not None:
            self.arch = arch
        if dhcp_group is not None:
            self.dhcp_group = dhcp_group
        if efi_boot is not None:
            self.efi_boot = efi_boot
        if bios_password is not None:
            self.bios_password = bios_password
        if maintenance_state is not None:
            self.maintenance_state = maintenance_state
        if name is not None:
            self.name = name
        if static_name is not None:
            self.static_name = static_name
        if uefi_supports_rfc3021 is not None:
            self.uefi_supports_rfc3021 = uefi_supports_rfc3021
        if link_aggregation is not None:
            self.link_aggregation = link_aggregation
        if provisioner is not None:
            self.provisioner = provisioner
        if supported_networking is not None:
            self.supported_networking = supported_networking
        if services is not None:
            self.services = services
        if management is not None:
            self.management = management
        if data is not None:
            self.data = data
        if role is not None:
            self.role = role
        if vlan_id is not None:
            self.vlan_id = vlan_id
        if tpm is not None:
            self.tpm = tpm
        if switch_short_id is not None:
            self.switch_short_id = switch_short_id
        if is_primary is not None:
            self.is_primary = is_primary
        if loopback_ip is not None:
            self.loopback_ip = loopback_ip
        if vrf is not None:
            self.vrf = vrf
        if exclude_from_narwhal is not None:
            self.exclude_from_narwhal = exclude_from_narwhal

    @property
    def type(self):
        """Gets the type of this StaffHardwareCreateInput.  # noqa: E501


        :return: The type of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StaffHardwareCreateInput.


        :param type: The type of this StaffHardwareCreateInput.  # noqa: E501
        :type type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def state(self):
        """Gets the state of this StaffHardwareCreateInput.  # noqa: E501


        :return: The state of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StaffHardwareCreateInput.


        :param state: The state of this StaffHardwareCreateInput.  # noqa: E501
        :type state: str
        """

        self._state = state

    @property
    def u_spaces(self):
        """Gets the u_spaces of this StaffHardwareCreateInput.  # noqa: E501


        :return: The u_spaces of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: int
        """
        return self._u_spaces

    @u_spaces.setter
    def u_spaces(self, u_spaces):
        """Sets the u_spaces of this StaffHardwareCreateInput.


        :param u_spaces: The u_spaces of this StaffHardwareCreateInput.  # noqa: E501
        :type u_spaces: int
        """

        self._u_spaces = u_spaces

    @property
    def model_number(self):
        """Gets the model_number of this StaffHardwareCreateInput.  # noqa: E501


        :return: The model_number of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._model_number

    @model_number.setter
    def model_number(self, model_number):
        """Sets the model_number of this StaffHardwareCreateInput.


        :param model_number: The model_number of this StaffHardwareCreateInput.  # noqa: E501
        :type model_number: str
        """
        if self.local_vars_configuration.client_side_validation and model_number is None:  # noqa: E501
            raise ValueError("Invalid value for `model_number`, must not be `None`")  # noqa: E501

        self._model_number = model_number

    @property
    def serial_number(self):
        """Gets the serial_number of this StaffHardwareCreateInput.  # noqa: E501


        :return: The serial_number of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        """Sets the serial_number of this StaffHardwareCreateInput.


        :param serial_number: The serial_number of this StaffHardwareCreateInput.  # noqa: E501
        :type serial_number: str
        """

        self._serial_number = serial_number

    @property
    def server_rack_id(self):
        """Gets the server_rack_id of this StaffHardwareCreateInput.  # noqa: E501


        :return: The server_rack_id of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._server_rack_id

    @server_rack_id.setter
    def server_rack_id(self, server_rack_id):
        """Sets the server_rack_id of this StaffHardwareCreateInput.


        :param server_rack_id: The server_rack_id of this StaffHardwareCreateInput.  # noqa: E501
        :type server_rack_id: str
        """

        self._server_rack_id = server_rack_id

    @property
    def leased(self):
        """Gets the leased of this StaffHardwareCreateInput.  # noqa: E501


        :return: The leased of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: bool
        """
        return self._leased

    @leased.setter
    def leased(self, leased):
        """Sets the leased of this StaffHardwareCreateInput.


        :param leased: The leased of this StaffHardwareCreateInput.  # noqa: E501
        :type leased: bool
        """

        self._leased = leased

    @property
    def lease_number(self):
        """Gets the lease_number of this StaffHardwareCreateInput.  # noqa: E501


        :return: The lease_number of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._lease_number

    @lease_number.setter
    def lease_number(self, lease_number):
        """Sets the lease_number of this StaffHardwareCreateInput.


        :param lease_number: The lease_number of this StaffHardwareCreateInput.  # noqa: E501
        :type lease_number: str
        """

        self._lease_number = lease_number

    @property
    def lease_expires_at(self):
        """Gets the lease_expires_at of this StaffHardwareCreateInput.  # noqa: E501


        :return: The lease_expires_at of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: datetime
        """
        return self._lease_expires_at

    @lease_expires_at.setter
    def lease_expires_at(self, lease_expires_at):
        """Sets the lease_expires_at of this StaffHardwareCreateInput.


        :param lease_expires_at: The lease_expires_at of this StaffHardwareCreateInput.  # noqa: E501
        :type lease_expires_at: datetime
        """

        self._lease_expires_at = lease_expires_at

    @property
    def arch(self):
        """Gets the arch of this StaffHardwareCreateInput.  # noqa: E501


        :return: The arch of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this StaffHardwareCreateInput.


        :param arch: The arch of this StaffHardwareCreateInput.  # noqa: E501
        :type arch: str
        """

        self._arch = arch

    @property
    def dhcp_group(self):
        """Gets the dhcp_group of this StaffHardwareCreateInput.  # noqa: E501


        :return: The dhcp_group of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._dhcp_group

    @dhcp_group.setter
    def dhcp_group(self, dhcp_group):
        """Sets the dhcp_group of this StaffHardwareCreateInput.


        :param dhcp_group: The dhcp_group of this StaffHardwareCreateInput.  # noqa: E501
        :type dhcp_group: str
        """

        self._dhcp_group = dhcp_group

    @property
    def efi_boot(self):
        """Gets the efi_boot of this StaffHardwareCreateInput.  # noqa: E501


        :return: The efi_boot of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: bool
        """
        return self._efi_boot

    @efi_boot.setter
    def efi_boot(self, efi_boot):
        """Sets the efi_boot of this StaffHardwareCreateInput.


        :param efi_boot: The efi_boot of this StaffHardwareCreateInput.  # noqa: E501
        :type efi_boot: bool
        """

        self._efi_boot = efi_boot

    @property
    def bios_password(self):
        """Gets the bios_password of this StaffHardwareCreateInput.  # noqa: E501


        :return: The bios_password of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._bios_password

    @bios_password.setter
    def bios_password(self, bios_password):
        """Sets the bios_password of this StaffHardwareCreateInput.


        :param bios_password: The bios_password of this StaffHardwareCreateInput.  # noqa: E501
        :type bios_password: str
        """

        self._bios_password = bios_password

    @property
    def maintenance_state(self):
        """Gets the maintenance_state of this StaffHardwareCreateInput.  # noqa: E501


        :return: The maintenance_state of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._maintenance_state

    @maintenance_state.setter
    def maintenance_state(self, maintenance_state):
        """Sets the maintenance_state of this StaffHardwareCreateInput.


        :param maintenance_state: The maintenance_state of this StaffHardwareCreateInput.  # noqa: E501
        :type maintenance_state: str
        """

        self._maintenance_state = maintenance_state

    @property
    def name(self):
        """Gets the name of this StaffHardwareCreateInput.  # noqa: E501


        :return: The name of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StaffHardwareCreateInput.


        :param name: The name of this StaffHardwareCreateInput.  # noqa: E501
        :type name: str
        """

        self._name = name

    @property
    def static_name(self):
        """Gets the static_name of this StaffHardwareCreateInput.  # noqa: E501


        :return: The static_name of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._static_name

    @static_name.setter
    def static_name(self, static_name):
        """Sets the static_name of this StaffHardwareCreateInput.


        :param static_name: The static_name of this StaffHardwareCreateInput.  # noqa: E501
        :type static_name: str
        """

        self._static_name = static_name

    @property
    def uefi_supports_rfc3021(self):
        """Gets the uefi_supports_rfc3021 of this StaffHardwareCreateInput.  # noqa: E501


        :return: The uefi_supports_rfc3021 of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: bool
        """
        return self._uefi_supports_rfc3021

    @uefi_supports_rfc3021.setter
    def uefi_supports_rfc3021(self, uefi_supports_rfc3021):
        """Sets the uefi_supports_rfc3021 of this StaffHardwareCreateInput.


        :param uefi_supports_rfc3021: The uefi_supports_rfc3021 of this StaffHardwareCreateInput.  # noqa: E501
        :type uefi_supports_rfc3021: bool
        """

        self._uefi_supports_rfc3021 = uefi_supports_rfc3021

    @property
    def link_aggregation(self):
        """Gets the link_aggregation of this StaffHardwareCreateInput.  # noqa: E501


        :return: The link_aggregation of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._link_aggregation

    @link_aggregation.setter
    def link_aggregation(self, link_aggregation):
        """Sets the link_aggregation of this StaffHardwareCreateInput.


        :param link_aggregation: The link_aggregation of this StaffHardwareCreateInput.  # noqa: E501
        :type link_aggregation: str
        """

        self._link_aggregation = link_aggregation

    @property
    def provisioner(self):
        """Gets the provisioner of this StaffHardwareCreateInput.  # noqa: E501


        :return: The provisioner of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._provisioner

    @provisioner.setter
    def provisioner(self, provisioner):
        """Sets the provisioner of this StaffHardwareCreateInput.


        :param provisioner: The provisioner of this StaffHardwareCreateInput.  # noqa: E501
        :type provisioner: str
        """

        self._provisioner = provisioner

    @property
    def supported_networking(self):
        """Gets the supported_networking of this StaffHardwareCreateInput.  # noqa: E501


        :return: The supported_networking of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: list[str]
        """
        return self._supported_networking

    @supported_networking.setter
    def supported_networking(self, supported_networking):
        """Sets the supported_networking of this StaffHardwareCreateInput.


        :param supported_networking: The supported_networking of this StaffHardwareCreateInput.  # noqa: E501
        :type supported_networking: list[str]
        """

        self._supported_networking = supported_networking

    @property
    def services(self):
        """Gets the services of this StaffHardwareCreateInput.  # noqa: E501


        :return: The services of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: object
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this StaffHardwareCreateInput.


        :param services: The services of this StaffHardwareCreateInput.  # noqa: E501
        :type services: object
        """

        self._services = services

    @property
    def management(self):
        """Gets the management of this StaffHardwareCreateInput.  # noqa: E501


        :return: The management of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: object
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this StaffHardwareCreateInput.


        :param management: The management of this StaffHardwareCreateInput.  # noqa: E501
        :type management: object
        """

        self._management = management

    @property
    def data(self):
        """Gets the data of this StaffHardwareCreateInput.  # noqa: E501

        Holds custom data depending on the hardware type. Any attribute set here can also be set as part of the hardware object  # noqa: E501

        :return: The data of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this StaffHardwareCreateInput.

        Holds custom data depending on the hardware type. Any attribute set here can also be set as part of the hardware object  # noqa: E501

        :param data: The data of this StaffHardwareCreateInput.  # noqa: E501
        :type data: object
        """

        self._data = data

    @property
    def role(self):
        """Gets the role of this StaffHardwareCreateInput.  # noqa: E501

        Role of the hardware. Will affect how the hardware will be named. Its required for certain hardware types.  # noqa: E501

        :return: The role of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this StaffHardwareCreateInput.

        Role of the hardware. Will affect how the hardware will be named. Its required for certain hardware types.  # noqa: E501

        :param role: The role of this StaffHardwareCreateInput.  # noqa: E501
        :type role: str
        """

        self._role = role

    @property
    def vlan_id(self):
        """Gets the vlan_id of this StaffHardwareCreateInput.  # noqa: E501

        On certain server nodes/sleds (t1.small.x86 and x1.small.x86), it describes the internal VLAN used to route traffic inside the BladeSwitch.  # noqa: E501

        :return: The vlan_id of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: int
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this StaffHardwareCreateInput.

        On certain server nodes/sleds (t1.small.x86 and x1.small.x86), it describes the internal VLAN used to route traffic inside the BladeSwitch.  # noqa: E501

        :param vlan_id: The vlan_id of this StaffHardwareCreateInput.  # noqa: E501
        :type vlan_id: int
        """

        self._vlan_id = vlan_id

    @property
    def tpm(self):
        """Gets the tpm of this StaffHardwareCreateInput.  # noqa: E501

        On servers, describe if the server has a TPM card.  # noqa: E501

        :return: The tpm of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: bool
        """
        return self._tpm

    @tpm.setter
    def tpm(self, tpm):
        """Sets the tpm of this StaffHardwareCreateInput.

        On servers, describe if the server has a TPM card.  # noqa: E501

        :param tpm: The tpm of this StaffHardwareCreateInput.  # noqa: E501
        :type tpm: bool
        """

        self._tpm = tpm

    @property
    def switch_short_id(self):
        """Gets the switch_short_id of this StaffHardwareCreateInput.  # noqa: E501

        On servers, describe the switch the server is connected too. If left empty, the value will be auto set on creation.  # noqa: E501

        :return: The switch_short_id of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._switch_short_id

    @switch_short_id.setter
    def switch_short_id(self, switch_short_id):
        """Sets the switch_short_id of this StaffHardwareCreateInput.

        On servers, describe the switch the server is connected too. If left empty, the value will be auto set on creation.  # noqa: E501

        :param switch_short_id: The switch_short_id of this StaffHardwareCreateInput.  # noqa: E501
        :type switch_short_id: str
        """

        self._switch_short_id = switch_short_id

    @property
    def is_primary(self):
        """Gets the is_primary of this StaffHardwareCreateInput.  # noqa: E501

        Switch attribute. On Arista switches, indicates which of the 2 Arista switches in mlag mode is the primary. Its used to properly configure the switch through Narhwal.  # noqa: E501

        :return: The is_primary of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: bool
        """
        return self._is_primary

    @is_primary.setter
    def is_primary(self, is_primary):
        """Sets the is_primary of this StaffHardwareCreateInput.

        Switch attribute. On Arista switches, indicates which of the 2 Arista switches in mlag mode is the primary. Its used to properly configure the switch through Narhwal.  # noqa: E501

        :param is_primary: The is_primary of this StaffHardwareCreateInput.  # noqa: E501
        :type is_primary: bool
        """

        self._is_primary = is_primary

    @property
    def loopback_ip(self):
        """Gets the loopback_ip of this StaffHardwareCreateInput.  # noqa: E501

        Switch attribute. Specify the loopback_ip of the switch. Currently is not used in our automation.  # noqa: E501

        :return: The loopback_ip of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._loopback_ip

    @loopback_ip.setter
    def loopback_ip(self, loopback_ip):
        """Sets the loopback_ip of this StaffHardwareCreateInput.

        Switch attribute. Specify the loopback_ip of the switch. Currently is not used in our automation.  # noqa: E501

        :param loopback_ip: The loopback_ip of this StaffHardwareCreateInput.  # noqa: E501
        :type loopback_ip: str
        """

        self._loopback_ip = loopback_ip

    @property
    def vrf(self):
        """Gets the vrf of this StaffHardwareCreateInput.  # noqa: E501

        Switch attribute. Specify the Virtual Routing and Forwarding tag used on the configuration.  # noqa: E501

        :return: The vrf of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: str
        """
        return self._vrf

    @vrf.setter
    def vrf(self, vrf):
        """Sets the vrf of this StaffHardwareCreateInput.

        Switch attribute. Specify the Virtual Routing and Forwarding tag used on the configuration.  # noqa: E501

        :param vrf: The vrf of this StaffHardwareCreateInput.  # noqa: E501
        :type vrf: str
        """

        self._vrf = vrf

    @property
    def exclude_from_narwhal(self):
        """Gets the exclude_from_narwhal of this StaffHardwareCreateInput.  # noqa: E501

        Switch attribute. If set to true, any switch configuration task created by our automation will be skipped for this switch  # noqa: E501

        :return: The exclude_from_narwhal of this StaffHardwareCreateInput.  # noqa: E501
        :rtype: bool
        """
        return self._exclude_from_narwhal

    @exclude_from_narwhal.setter
    def exclude_from_narwhal(self, exclude_from_narwhal):
        """Sets the exclude_from_narwhal of this StaffHardwareCreateInput.

        Switch attribute. If set to true, any switch configuration task created by our automation will be skipped for this switch  # noqa: E501

        :param exclude_from_narwhal: The exclude_from_narwhal of this StaffHardwareCreateInput.  # noqa: E501
        :type exclude_from_narwhal: bool
        """

        self._exclude_from_narwhal = exclude_from_narwhal

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = inspect.getargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, StaffHardwareCreateInput):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StaffHardwareCreateInput):
            return True

        return self.to_dict() != other.to_dict()
