import connexion
import six

from metal.types.event import Event  # noqa: E501
from metal.types.interconnection import Interconnection  # noqa: E501
from metal.types.interconnection_create_input import InterconnectionCreateInput  # noqa: E501
from metal.types.interconnection_list import InterconnectionList  # noqa: E501
from metal.types.interconnection_port import InterconnectionPort  # noqa: E501
from metal.types.interconnection_port_list import InterconnectionPortList  # noqa: E501
from metal.types.interconnection_update_input import InterconnectionUpdateInput  # noqa: E501
from metal.types.virtual_circuit import VirtualCircuit  # noqa: E501
from metal.types.virtual_circuit_create_input import VirtualCircuitCreateInput  # noqa: E501
from metal.types.virtual_circuit_list import VirtualCircuitList  # noqa: E501
from metal.types.virtual_circuit_update_input import VirtualCircuitUpdateInput  # noqa: E501
from metal import util


def create_connection_port_virtual_circuit(connection_id, port_id, virtual_circuit):  # noqa: E501
    """Create a new Virtual Circuit

    Create a new Virtual Circuit on a dedicated connection using a Virtual Network record and an NNI VLAN value. # noqa: E501

    :param connection_id: UUID of the connection
    :type connection_id: 
    :param port_id: UUID of the connection port
    :type port_id: 
    :param virtual_circuit: Virtual Circuit details
    :type virtual_circuit: dict | bytes

    :rtype: VirtualCircuitList
    """
    if connexion.request.is_json:
        virtual_circuit = VirtualCircuitCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_organization_interconnection(organization_id, connection):  # noqa: E501
    """Request a new connection for the organization

    Creates a new connection request. A Project ID must be specified in the request body for connections on shared ports. # noqa: E501

    :param organization_id: UUID of the organization
    :type organization_id: 
    :param connection: Connection details
    :type connection: dict | bytes

    :rtype: Interconnection
    """
    if connexion.request.is_json:
        connection = InterconnectionCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_project_interconnection(project_id, connection):  # noqa: E501
    """Request a new connection for the project&#39;s organization

    Creates a new connection request # noqa: E501

    :param project_id: UUID of the project
    :type project_id: 
    :param connection: Connection details
    :type connection: dict | bytes

    :rtype: Interconnection
    """
    if connexion.request.is_json:
        connection = InterconnectionCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_interconnection(connection_id):  # noqa: E501
    """Delete connection

    Delete a connection, its associated ports and virtual circuits. # noqa: E501

    :param connection_id: Connection UUID
    :type connection_id: 

    :rtype: Interconnection
    """
    return 'do some magic!'


def delete_virtual_circuit(id):  # noqa: E501
    """Delete a virtual circuit

    Delete a virtual circuit from a dedicated port. # noqa: E501

    :param id: Virtual Circuit UUID
    :type id: 

    :rtype: VirtualCircuit
    """
    return 'do some magic!'


def find_connection_events(connection_id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve connection events

    Returns a list of the connection events # noqa: E501

    :param connection_id: Connection UUID
    :type connection_id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: Event
    """
    return 'do some magic!'


def find_connection_port_events(connection_id, id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve connection port events

    Returns a list of the connection port events # noqa: E501

    :param connection_id: Connection UUID
    :type connection_id: 
    :param id: Connection Port UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: Event
    """
    return 'do some magic!'


def find_virtual_circuit_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve connection events

    Returns a list of the virtual circuit events # noqa: E501

    :param id: Virtual Circuit UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: Event
    """
    return 'do some magic!'


def get_connection_port(connection_id, id):  # noqa: E501
    """Get a connection port

    Get the details of an connection port. # noqa: E501

    :param connection_id: UUID of the connection
    :type connection_id: 
    :param id: Port UUID
    :type id: 

    :rtype: InterconnectionPort
    """
    return 'do some magic!'


def get_interconnection(connection_id):  # noqa: E501
    """Get connection

    Get the details of a connection # noqa: E501

    :param connection_id: Connection UUID
    :type connection_id: 

    :rtype: Interconnection
    """
    return 'do some magic!'


def get_virtual_circuit(id):  # noqa: E501
    """Get a virtual circuit

    Get the details of a virtual circuit # noqa: E501

    :param id: Virtual Circuit UUID
    :type id: 

    :rtype: VirtualCircuit
    """
    return 'do some magic!'


def list_connection_port_virtual_circuits(connection_id, port_id):  # noqa: E501
    """List a connection port&#39;s virtual circuits

    List the virtual circuit record(s) associatiated with a particular connection port. # noqa: E501

    :param connection_id: UUID of the connection
    :type connection_id: 
    :param port_id: UUID of the connection port
    :type port_id: 

    :rtype: VirtualCircuitList
    """
    return 'do some magic!'


def list_connection_ports(connection_id):  # noqa: E501
    """List a connection&#39;s ports

    List the ports associated to an connection. # noqa: E501

    :param connection_id: UUID of the connection
    :type connection_id: 

    :rtype: InterconnectionPortList
    """
    return 'do some magic!'


def organization_list_interconnections(organization_id):  # noqa: E501
    """List organization connections

    List the connections belonging to the organization # noqa: E501

    :param organization_id: UUID of the organization
    :type organization_id: 

    :rtype: InterconnectionList
    """
    return 'do some magic!'


def project_list_interconnections(project_id):  # noqa: E501
    """List project connections

    List the connections belonging to the project # noqa: E501

    :param project_id: UUID of the project
    :type project_id: 

    :rtype: InterconnectionList
    """
    return 'do some magic!'


def update_interconnection(connection_id, connection):  # noqa: E501
    """Update connection

    Update the details of a connection # noqa: E501

    :param connection_id: Connection UUID
    :type connection_id: 
    :param connection: Updated connection details
    :type connection: dict | bytes

    :rtype: Interconnection
    """
    if connexion.request.is_json:
        connection = InterconnectionUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_virtual_circuit(id, virtual_circuit):  # noqa: E501
    """Update a virtual circuit

    Update the details of a virtual circuit. # noqa: E501

    :param id: Virtual Circuit UUID
    :type id: 
    :param virtual_circuit: Updated Virtual Circuit details
    :type virtual_circuit: dict | bytes

    :rtype: VirtualCircuit
    """
    if connexion.request.is_json:
        virtual_circuit = VirtualCircuitUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
