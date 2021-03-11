import connexion
import six

from metal.types.staff_hardware import StaffHardware  # noqa: E501
from metal.types.staff_hardware_create_input import StaffHardwareCreateInput  # noqa: E501
from metal.types.staff_hardware_list import StaffHardwareList  # noqa: E501
from metal.types.staff_hardware_update_input import StaffHardwareUpdateInput  # noqa: E501
from metal import util


def staff_create_server_rack_hardware(id, hardware):  # noqa: E501
    """Create hardware for server rack

    Creates hardware for server rack. # noqa: E501

    :param id: Server Rack UUID
    :type id: 
    :param hardware: Hardware to create
    :type hardware: dict | bytes

    :rtype: StaffHardware
    """
    if connexion.request.is_json:
        hardware = StaffHardwareCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def staff_delete_hardware_metadata(id):  # noqa: E501
    """Delete metadata for hardware

    Delete metadata for hardware. # noqa: E501

    :param id: Hardware UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def staff_find_hardware_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve hardware

    Returns hardware # noqa: E501

    :param id: Hardware UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: StaffHardware
    """
    return 'do some magic!'


def staff_find_server_rack_hardware(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all hardware for server rack

    Returns all hardware for a server rack. # noqa: E501

    :param id: Server Rack UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: StaffHardwareList
    """
    return 'do some magic!'


def staff_update_hardware(id, hardware):  # noqa: E501
    """Update hardware

    Updates hardware. # noqa: E501

    :param id: Hardware UUID
    :type id: 
    :param hardware: Hardware Information to be updated
    :type hardware: 

    :rtype: StaffHardware
    """
    return 'do some magic!'


def staff_update_hardware_provisioner(id):  # noqa: E501
    """Update provisioner for hardware

    Start a Job that will update the provisioner set on the hardware. # noqa: E501

    :param id: Hardware UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'
