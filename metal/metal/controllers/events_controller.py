import connexion
import six

from metal.types.event import Event  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal import util


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


def find_device_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve device&#39;s events

    Returns a list of events pertaining to a specific device # noqa: E501

    :param id: Device UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: EventList
    """
    return 'do some magic!'


def find_event_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve an event

    Returns a single event if the user has access # noqa: E501

    :param id: Event UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Event
    """
    return 'do some magic!'


def find_events(include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve current user&#39;s events

    Returns a list of the current user’s events # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: EventList
    """
    return 'do some magic!'


def find_organization_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve organization&#39;s events

    Returns a list of events for a single organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: EventList
    """
    return 'do some magic!'


def find_project_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve project&#39;s events

    Returns a list of events for a single project # noqa: E501

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

    :rtype: EventList
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


def find_volume_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve volume&#39;s events

    Returns a list of the current volume’s events # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: EventList
    """
    return 'do some magic!'
