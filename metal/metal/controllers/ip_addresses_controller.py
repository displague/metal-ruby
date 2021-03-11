import connexion
import six

from metal.types.ip_assignment import IPAssignment  # noqa: E501
from metal.types.ip_assignment_input import IPAssignmentInput  # noqa: E501
from metal.types.ip_assignment_list import IPAssignmentList  # noqa: E501
from metal.types.ip_availabilities_list import IPAvailabilitiesList  # noqa: E501
from metal.types.ip_reservation import IPReservation  # noqa: E501
from metal.types.ip_reservation_list import IPReservationList  # noqa: E501
from metal.types.ip_reservation_request_input import IPReservationRequestInput  # noqa: E501
from metal import util


def create_ip_assignment(id, ip_assignment):  # noqa: E501
    """Create a ip assignment

    Creates an ip assignment for a device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param ip_assignment: IPAssignment to create
    :type ip_assignment: dict | bytes

    :rtype: IPAssignment
    """
    if connexion.request.is_json:
        ip_assignment = IPAssignmentInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_ip_address(id):  # noqa: E501
    """Unassign an ip address

    Note! This call can be used to un-assign an IP assignment or delete an IP reservation. Un-assign an IP address record. Use the assignment UUID you get after attaching the IP. This will remove the relationship between an IP and the device and will make the IP address available to be assigned to another device. Delete and IP reservation. Use the reservation UUID you get after adding the IP to the project. This will permanently delete the IP block reservation from the project. # noqa: E501

    :param id: IP Address UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_ip_address_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve an ip address

    Returns a single ip address if the user has access. # noqa: E501

    :param id: IP Address UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: IPAssignment
    """
    return 'do some magic!'


def find_ip_address_customdata(id):  # noqa: E501
    """Retrieve the custom metadata of an IP Reservation or IP Assignment

    Provides the custom metadata stored for this IP Reservation or IP Assignment in json format # noqa: E501

    :param id: Ip Reservation UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_ip_assignments(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all ip assignments

    Returns all ip assignments for a device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: IPAssignmentList
    """
    return 'do some magic!'


def find_ip_availabilities(id, cidr):  # noqa: E501
    """Retrieve all available subnets of a particular reservation

    Provides a list of IP resevations for a single project. # noqa: E501

    :param id: IP Reservation UUID
    :type id: 
    :param cidr: Size of subnets in bits
    :type cidr: str

    :rtype: IPAvailabilitiesList
    """
    return 'do some magic!'


def find_ip_reservations(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all ip reservations

    Provides a list of IP resevations for a single project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: IPReservationList
    """
    return 'do some magic!'


def request_ip_reservation(id, ip_reservation_request):  # noqa: E501
    """Requesting IP reservations

    Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a &#x60;state&#x60; of &#x60;pending&#x60;. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the &#x60;fail_on_approval_required&#x60; parameter set to &#x60;true&#x60; in the request. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param ip_reservation_request: IP Reservation Request to create
    :type ip_reservation_request: dict | bytes

    :rtype: IPReservation
    """
    if connexion.request.is_json:
        ip_reservation_request = IPReservationRequestInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
