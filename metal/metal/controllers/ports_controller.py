import connexion
import six

from metal.types.port import Port  # noqa: E501
from metal.types.port_assign_input import PortAssignInput  # noqa: E501
from metal.types.port_convert_layer3_input import PortConvertLayer3Input  # noqa: E501
from metal import util


def assign_native_vlan(id, vnid):  # noqa: E501
    """Assign a native VLAN

    Assigns a virtual network to this port as a \&quot;native VLAN\&quot; # noqa: E501

    :param id: Port UUID
    :type id: 
    :param vnid: UUID or VNID of the virtual network to assign
    :type vnid: str

    :rtype: Port
    """
    return 'do some magic!'


def assign_port(id, vnid):  # noqa: E501
    """Assign a port to virtual network

    Assign a port for a hardware to virtual network. # noqa: E501

    :param id: Port UUID
    :type id: 
    :param vnid: Virtual Network ID
    :type vnid: dict | bytes

    :rtype: Port
    """
    if connexion.request.is_json:
        vnid = PortAssignInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def bond_port(id, bulk_enable=None):  # noqa: E501
    """Enabling bonding

    Enabling bonding for one or all ports # noqa: E501

    :param id: Port UUID
    :type id: 
    :param bulk_enable: enable both ports
    :type bulk_enable: bool

    :rtype: Port
    """
    return 'do some magic!'


def convert_layer2(id, vnid=None):  # noqa: E501
    """Convert to Layer 2

    Converts a bond port to Layer 2. IP assignments of the port will be removed. # noqa: E501

    :param id: Port UUID
    :type id: 
    :param vnid: Virtual Network ID
    :type vnid: dict | bytes

    :rtype: Port
    """
    if connexion.request.is_json:
        vnid = PortAssignInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def convert_layer3(id, request_ips=None):  # noqa: E501
    """Convert to Layer 3

    Converts a bond port to Layer 3. VLANs must first be unassigned. # noqa: E501

    :param id: Port UUID
    :type id: 
    :param request_ips: IPs to request
    :type request_ips: dict | bytes

    :rtype: Port
    """
    if connexion.request.is_json:
        request_ips = PortConvertLayer3Input.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_native_vlan(id):  # noqa: E501
    """Remove native VLAN

    Removes the native VLAN from this port # noqa: E501

    :param id: Port UUID
    :type id: 

    :rtype: Port
    """
    return 'do some magic!'


def disbond_port(id, bulk_disable=None):  # noqa: E501
    """Disabling bonding

    Disabling bonding for one or all ports # noqa: E501

    :param id: Port UUID
    :type id: 
    :param bulk_disable: disable both ports
    :type bulk_disable: bool

    :rtype: Port
    """
    return 'do some magic!'


def find_port_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a port

    Returns a port # noqa: E501

    :param id: Port UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Port
    """
    return 'do some magic!'


def unassign_port(id, vnid):  # noqa: E501
    """Unassign a port

    Unassign a port for a hardware. # noqa: E501

    :param id: Port UUID
    :type id: 
    :param vnid: Virtual Network ID
    :type vnid: dict | bytes

    :rtype: Port
    """
    if connexion.request.is_json:
        vnid = PortAssignInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
