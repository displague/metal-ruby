import connexion
import six

from metal.types.internet_gateway import InternetGateway  # noqa: E501
from metal.types.port import Port  # noqa: E501
from metal.types.virtual_network import VirtualNetwork  # noqa: E501
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput  # noqa: E501
from metal.types.virtual_network_list import VirtualNetworkList  # noqa: E501
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


def create_internet_gateway(id, length):  # noqa: E501
    """Create an internet gateway

    Creates an internet gateway. # noqa: E501

    :param id: Virtual Network UUID
    :type id: 
    :param length: IP Reservation length
    :type length: str

    :rtype: InternetGateway
    """
    return 'do some magic!'


def create_virtual_network(id, virtual_network):  # noqa: E501
    """Create an virtual network

    Creates an virtual network. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param virtual_network: Virtual Network to create
    :type virtual_network: dict | bytes

    :rtype: VirtualNetwork
    """
    if connexion.request.is_json:
        virtual_network = VirtualNetworkCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_native_vlan(id):  # noqa: E501
    """Remove native VLAN

    Removes the native VLAN from this port # noqa: E501

    :param id: Port UUID
    :type id: 

    :rtype: Port
    """
    return 'do some magic!'


def delete_virtual_network(id):  # noqa: E501
    """Delete a virtual network

    Deletes a virtual network. # noqa: E501

    :param id: Virtual Network UUID
    :type id: 

    :rtype: VirtualNetwork
    """
    return 'do some magic!'


def find_virtual_networks(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all virtual networks

    Provides a list of virtual networks for a single project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: VirtualNetworkList
    """
    return 'do some magic!'


def get_virtual_network(id):  # noqa: E501
    """Get a virtual network

    Get a virtual network. # noqa: E501

    :param id: Virtual Network UUID
    :type id: 

    :rtype: VirtualNetwork
    """
    return 'do some magic!'
