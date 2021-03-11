# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from metal.types.base_model_ import Model
from metal.types.staff_facility_little import StaffFacilityLittle
from metal.types.staff_metro_little import StaffMetroLittle
from metal.types.staff_port import StaffPort
from metal import util

from metal.types.staff_facility_little import StaffFacilityLittle  # noqa: E501
from metal.types.staff_metro_little import StaffMetroLittle  # noqa: E501
from metal.types.staff_port import StaffPort  # noqa: E501

class StaffIpAddress(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, network=None, address_family=None, netmask=None, created_at=None, details=None, public=None, management=None, manageable=None, enabled=None, created_by=None, global_ip=None, reservation=None, customdata=None, bill=None, tags=None, address=None, gateway=None, cidr=None, state=None, requested_quantity=None, facility=None, metro=None, interface=None):  # noqa: E501
        """StaffIpAddress - a model defined in OpenAPI

        :param id: The id of this StaffIpAddress.  # noqa: E501
        :type id: str
        :param network: The network of this StaffIpAddress.  # noqa: E501
        :type network: str
        :param address_family: The address_family of this StaffIpAddress.  # noqa: E501
        :type address_family: int
        :param netmask: The netmask of this StaffIpAddress.  # noqa: E501
        :type netmask: str
        :param created_at: The created_at of this StaffIpAddress.  # noqa: E501
        :type created_at: datetime
        :param details: The details of this StaffIpAddress.  # noqa: E501
        :type details: str
        :param public: The public of this StaffIpAddress.  # noqa: E501
        :type public: bool
        :param management: The management of this StaffIpAddress.  # noqa: E501
        :type management: bool
        :param manageable: The manageable of this StaffIpAddress.  # noqa: E501
        :type manageable: bool
        :param enabled: The enabled of this StaffIpAddress.  # noqa: E501
        :type enabled: bool
        :param created_by: The created_by of this StaffIpAddress.  # noqa: E501
        :type created_by: str
        :param global_ip: The global_ip of this StaffIpAddress.  # noqa: E501
        :type global_ip: bool
        :param reservation: The reservation of this StaffIpAddress.  # noqa: E501
        :type reservation: bool
        :param customdata: The customdata of this StaffIpAddress.  # noqa: E501
        :type customdata: object
        :param bill: The bill of this StaffIpAddress.  # noqa: E501
        :type bill: bool
        :param tags: The tags of this StaffIpAddress.  # noqa: E501
        :type tags: List[str]
        :param address: The address of this StaffIpAddress.  # noqa: E501
        :type address: str
        :param gateway: The gateway of this StaffIpAddress.  # noqa: E501
        :type gateway: str
        :param cidr: The cidr of this StaffIpAddress.  # noqa: E501
        :type cidr: int
        :param state: The state of this StaffIpAddress.  # noqa: E501
        :type state: str
        :param requested_quantity: The requested_quantity of this StaffIpAddress.  # noqa: E501
        :type requested_quantity: int
        :param facility: The facility of this StaffIpAddress.  # noqa: E501
        :type facility: StaffFacilityLittle
        :param metro: The metro of this StaffIpAddress.  # noqa: E501
        :type metro: StaffMetroLittle
        :param interface: The interface of this StaffIpAddress.  # noqa: E501
        :type interface: StaffPort
        """
        self.openapi_types = {
            'id': str,
            'network': str,
            'address_family': int,
            'netmask': str,
            'created_at': datetime,
            'details': str,
            'public': bool,
            'management': bool,
            'manageable': bool,
            'enabled': bool,
            'created_by': str,
            'global_ip': bool,
            'reservation': bool,
            'customdata': object,
            'bill': bool,
            'tags': List[str],
            'address': str,
            'gateway': str,
            'cidr': int,
            'state': str,
            'requested_quantity': int,
            'facility': StaffFacilityLittle,
            'metro': StaffMetroLittle,
            'interface': StaffPort
        }

        self.attribute_map = {
            'id': 'id',
            'network': 'network',
            'address_family': 'address_family',
            'netmask': 'netmask',
            'created_at': 'created_at',
            'details': 'details',
            'public': 'public',
            'management': 'management',
            'manageable': 'manageable',
            'enabled': 'enabled',
            'created_by': 'created_by',
            'global_ip': 'global_ip',
            'reservation': 'reservation',
            'customdata': 'customdata',
            'bill': 'bill',
            'tags': 'tags',
            'address': 'address',
            'gateway': 'gateway',
            'cidr': 'cidr',
            'state': 'state',
            'requested_quantity': 'requested_quantity',
            'facility': 'facility',
            'metro': 'metro',
            'interface': 'interface'
        }

        self._id = id
        self._network = network
        self._address_family = address_family
        self._netmask = netmask
        self._created_at = created_at
        self._details = details
        self._public = public
        self._management = management
        self._manageable = manageable
        self._enabled = enabled
        self._created_by = created_by
        self._global_ip = global_ip
        self._reservation = reservation
        self._customdata = customdata
        self._bill = bill
        self._tags = tags
        self._address = address
        self._gateway = gateway
        self._cidr = cidr
        self._state = state
        self._requested_quantity = requested_quantity
        self._facility = facility
        self._metro = metro
        self._interface = interface

    @classmethod
    def from_dict(cls, dikt) -> 'StaffIpAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Staff::IpAddress of this StaffIpAddress.  # noqa: E501
        :rtype: StaffIpAddress
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this StaffIpAddress.


        :return: The id of this StaffIpAddress.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this StaffIpAddress.


        :param id: The id of this StaffIpAddress.
        :type id: str
        """

        self._id = id

    @property
    def network(self):
        """Gets the network of this StaffIpAddress.


        :return: The network of this StaffIpAddress.
        :rtype: str
        """
        return self._network

    @network.setter
    def network(self, network):
        """Sets the network of this StaffIpAddress.


        :param network: The network of this StaffIpAddress.
        :type network: str
        """

        self._network = network

    @property
    def address_family(self):
        """Gets the address_family of this StaffIpAddress.


        :return: The address_family of this StaffIpAddress.
        :rtype: int
        """
        return self._address_family

    @address_family.setter
    def address_family(self, address_family):
        """Sets the address_family of this StaffIpAddress.


        :param address_family: The address_family of this StaffIpAddress.
        :type address_family: int
        """

        self._address_family = address_family

    @property
    def netmask(self):
        """Gets the netmask of this StaffIpAddress.


        :return: The netmask of this StaffIpAddress.
        :rtype: str
        """
        return self._netmask

    @netmask.setter
    def netmask(self, netmask):
        """Sets the netmask of this StaffIpAddress.


        :param netmask: The netmask of this StaffIpAddress.
        :type netmask: str
        """

        self._netmask = netmask

    @property
    def created_at(self):
        """Gets the created_at of this StaffIpAddress.


        :return: The created_at of this StaffIpAddress.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this StaffIpAddress.


        :param created_at: The created_at of this StaffIpAddress.
        :type created_at: datetime
        """

        self._created_at = created_at

    @property
    def details(self):
        """Gets the details of this StaffIpAddress.


        :return: The details of this StaffIpAddress.
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this StaffIpAddress.


        :param details: The details of this StaffIpAddress.
        :type details: str
        """

        self._details = details

    @property
    def public(self):
        """Gets the public of this StaffIpAddress.


        :return: The public of this StaffIpAddress.
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this StaffIpAddress.


        :param public: The public of this StaffIpAddress.
        :type public: bool
        """

        self._public = public

    @property
    def management(self):
        """Gets the management of this StaffIpAddress.


        :return: The management of this StaffIpAddress.
        :rtype: bool
        """
        return self._management

    @management.setter
    def management(self, management):
        """Sets the management of this StaffIpAddress.


        :param management: The management of this StaffIpAddress.
        :type management: bool
        """

        self._management = management

    @property
    def manageable(self):
        """Gets the manageable of this StaffIpAddress.


        :return: The manageable of this StaffIpAddress.
        :rtype: bool
        """
        return self._manageable

    @manageable.setter
    def manageable(self, manageable):
        """Sets the manageable of this StaffIpAddress.


        :param manageable: The manageable of this StaffIpAddress.
        :type manageable: bool
        """

        self._manageable = manageable

    @property
    def enabled(self):
        """Gets the enabled of this StaffIpAddress.


        :return: The enabled of this StaffIpAddress.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this StaffIpAddress.


        :param enabled: The enabled of this StaffIpAddress.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def created_by(self):
        """Gets the created_by of this StaffIpAddress.


        :return: The created_by of this StaffIpAddress.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this StaffIpAddress.


        :param created_by: The created_by of this StaffIpAddress.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def global_ip(self):
        """Gets the global_ip of this StaffIpAddress.


        :return: The global_ip of this StaffIpAddress.
        :rtype: bool
        """
        return self._global_ip

    @global_ip.setter
    def global_ip(self, global_ip):
        """Sets the global_ip of this StaffIpAddress.


        :param global_ip: The global_ip of this StaffIpAddress.
        :type global_ip: bool
        """

        self._global_ip = global_ip

    @property
    def reservation(self):
        """Gets the reservation of this StaffIpAddress.


        :return: The reservation of this StaffIpAddress.
        :rtype: bool
        """
        return self._reservation

    @reservation.setter
    def reservation(self, reservation):
        """Sets the reservation of this StaffIpAddress.


        :param reservation: The reservation of this StaffIpAddress.
        :type reservation: bool
        """

        self._reservation = reservation

    @property
    def customdata(self):
        """Gets the customdata of this StaffIpAddress.


        :return: The customdata of this StaffIpAddress.
        :rtype: object
        """
        return self._customdata

    @customdata.setter
    def customdata(self, customdata):
        """Sets the customdata of this StaffIpAddress.


        :param customdata: The customdata of this StaffIpAddress.
        :type customdata: object
        """

        self._customdata = customdata

    @property
    def bill(self):
        """Gets the bill of this StaffIpAddress.


        :return: The bill of this StaffIpAddress.
        :rtype: bool
        """
        return self._bill

    @bill.setter
    def bill(self, bill):
        """Sets the bill of this StaffIpAddress.


        :param bill: The bill of this StaffIpAddress.
        :type bill: bool
        """

        self._bill = bill

    @property
    def tags(self):
        """Gets the tags of this StaffIpAddress.


        :return: The tags of this StaffIpAddress.
        :rtype: List[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this StaffIpAddress.


        :param tags: The tags of this StaffIpAddress.
        :type tags: List[str]
        """

        self._tags = tags

    @property
    def address(self):
        """Gets the address of this StaffIpAddress.


        :return: The address of this StaffIpAddress.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this StaffIpAddress.


        :param address: The address of this StaffIpAddress.
        :type address: str
        """

        self._address = address

    @property
    def gateway(self):
        """Gets the gateway of this StaffIpAddress.


        :return: The gateway of this StaffIpAddress.
        :rtype: str
        """
        return self._gateway

    @gateway.setter
    def gateway(self, gateway):
        """Sets the gateway of this StaffIpAddress.


        :param gateway: The gateway of this StaffIpAddress.
        :type gateway: str
        """

        self._gateway = gateway

    @property
    def cidr(self):
        """Gets the cidr of this StaffIpAddress.


        :return: The cidr of this StaffIpAddress.
        :rtype: int
        """
        return self._cidr

    @cidr.setter
    def cidr(self, cidr):
        """Sets the cidr of this StaffIpAddress.


        :param cidr: The cidr of this StaffIpAddress.
        :type cidr: int
        """

        self._cidr = cidr

    @property
    def state(self):
        """Gets the state of this StaffIpAddress.


        :return: The state of this StaffIpAddress.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this StaffIpAddress.


        :param state: The state of this StaffIpAddress.
        :type state: str
        """

        self._state = state

    @property
    def requested_quantity(self):
        """Gets the requested_quantity of this StaffIpAddress.


        :return: The requested_quantity of this StaffIpAddress.
        :rtype: int
        """
        return self._requested_quantity

    @requested_quantity.setter
    def requested_quantity(self, requested_quantity):
        """Sets the requested_quantity of this StaffIpAddress.


        :param requested_quantity: The requested_quantity of this StaffIpAddress.
        :type requested_quantity: int
        """

        self._requested_quantity = requested_quantity

    @property
    def facility(self):
        """Gets the facility of this StaffIpAddress.


        :return: The facility of this StaffIpAddress.
        :rtype: StaffFacilityLittle
        """
        return self._facility

    @facility.setter
    def facility(self, facility):
        """Sets the facility of this StaffIpAddress.


        :param facility: The facility of this StaffIpAddress.
        :type facility: StaffFacilityLittle
        """

        self._facility = facility

    @property
    def metro(self):
        """Gets the metro of this StaffIpAddress.


        :return: The metro of this StaffIpAddress.
        :rtype: StaffMetroLittle
        """
        return self._metro

    @metro.setter
    def metro(self, metro):
        """Sets the metro of this StaffIpAddress.


        :param metro: The metro of this StaffIpAddress.
        :type metro: StaffMetroLittle
        """

        self._metro = metro

    @property
    def interface(self):
        """Gets the interface of this StaffIpAddress.


        :return: The interface of this StaffIpAddress.
        :rtype: StaffPort
        """
        return self._interface

    @interface.setter
    def interface(self, interface):
        """Sets the interface of this StaffIpAddress.


        :param interface: The interface of this StaffIpAddress.
        :type interface: StaffPort
        """

        self._interface = interface
