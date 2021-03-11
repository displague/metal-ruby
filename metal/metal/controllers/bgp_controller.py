import connexion
import six

from metal.types.bgp_session_input import BGPSessionInput  # noqa: E501
from metal.types.bgp_config import BgpConfig  # noqa: E501
from metal.types.bgp_config_request_input import BgpConfigRequestInput  # noqa: E501
from metal.types.bgp_session import BgpSession  # noqa: E501
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.types.bgp_session_neighbors import BgpSessionNeighbors  # noqa: E501
from metal import util


def create_bgp_session(id, bgp_session):  # noqa: E501
    """Create a BGP session

    Creates a BGP session. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param bgp_session: BGP session to create
    :type bgp_session: dict | bytes

    :rtype: BgpSession
    """
    if connexion.request.is_json:
        bgp_session = BGPSessionInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_bgp_session(id):  # noqa: E501
    """Delete the BGP session

    Deletes the BGP session. # noqa: E501

    :param id: BGP session UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_bgp_config_by_project(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a bgp config

    Returns a bgp config # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: BgpConfig
    """
    return 'do some magic!'


def find_bgp_session_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a BGP session

    Returns a BGP session # noqa: E501

    :param id: BGP session UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: BgpSession
    """
    return 'do some magic!'


def find_bgp_sessions(id):  # noqa: E501
    """Retrieve all BGP sessions

    Provides a listing of available BGP sessions for the device. # noqa: E501

    :param id: Device UUID
    :type id: 

    :rtype: BgpSessionList
    """
    return 'do some magic!'


def find_project_bgp_sessions(id):  # noqa: E501
    """Retrieve all BGP sessions for project

    Provides a listing of available BGP sessions for the project. # noqa: E501

    :param id: Project UUID
    :type id: 

    :rtype: BgpSessionList
    """
    return 'do some magic!'


def get_bgp_neighbor_data(id):  # noqa: E501
    """Retrieve BGP neighbor data for this device

    Provides a summary of the BGP neighbor data associated to the BGP sessions for this device. # noqa: E501

    :param id: Device UUID
    :type id: 

    :rtype: BgpSessionNeighbors
    """
    return 'do some magic!'


def request_bgp_config(id, bgp_config_request):  # noqa: E501
    """Requesting bgp config

    Requests to enable bgp configuration for a project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param bgp_config_request: BGP config Request to create
    :type bgp_config_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bgp_config_request = BgpConfigRequestInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_bgp_session(id, default_route):  # noqa: E501
    """Update the BGP session

    Updates the BGP session by either enabling or disabling the default route functionality. # noqa: E501

    :param id: BGP session UUID
    :type id: 
    :param default_route: Default route
    :type default_route: bool

    :rtype: None
    """
    return 'do some magic!'
