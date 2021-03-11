import connexion
import six

from metal.types.device import Device  # noqa: E501
from metal.types.hardware_reservation import HardwareReservation  # noqa: E501
from metal.types.hardware_reservation_list import HardwareReservationList  # noqa: E501
from metal import util


def find_hardware_reservation_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a hardware reservation

    Returns a single hardware reservation # noqa: E501

    :param id: HardwareReservation UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Device
    """
    return 'do some magic!'


def find_project_hardware_reservations(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all hardware reservations for a given project

    Provides a collection of hardware reservations for a given project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: HardwareReservationList
    """
    return 'do some magic!'


def hardware_reservations_id_move_post(id, project_id):  # noqa: E501
    """Move a hardware reservation

    Move a hardware reservation to another project # noqa: E501

    :param id: Hardware Reservation UUID
    :type id: 
    :param project_id: Project UUID
    :type project_id: 
    :type project_id: 

    :rtype: HardwareReservation
    """
    return 'do some magic!'
