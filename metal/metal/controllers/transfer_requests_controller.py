import connexion
import six

from metal.types.transfer_request import TransferRequest  # noqa: E501
from metal.types.transfer_request_input import TransferRequestInput  # noqa: E501
from metal.types.transfer_request_list import TransferRequestList  # noqa: E501
from metal import util


def accept_transfer_request(id):  # noqa: E501
    """Accept a transfer request

    Accept a transfer request. # noqa: E501

    :param id: Transfer request UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def create_transfer_request(id, transfer_request):  # noqa: E501
    """Create a transfer request

    Organization owners can transfer their projects to other organizations. # noqa: E501

    :param id: UUID of the project to be transferred
    :type id: 
    :param transfer_request: Transfer Request to create
    :type transfer_request: dict | bytes

    :rtype: TransferRequest
    """
    if connexion.request.is_json:
        transfer_request = TransferRequestInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def decline_transfer_request(id):  # noqa: E501
    """Decline a transfer request

    Decline a transfer request. # noqa: E501

    :param id: Transfer request UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_organization_transfers(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all project transfer requests from or to an organization

    Provides a collection of project transfer requests from or to the organization. # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: TransferRequestList
    """
    return 'do some magic!'


def find_transfer_request_by_id(id, include=None, exclude=None):  # noqa: E501
    """View a transfer request

    Returns a single transfer request. # noqa: E501

    :param id: Transfer request UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: TransferRequest
    """
    return 'do some magic!'
