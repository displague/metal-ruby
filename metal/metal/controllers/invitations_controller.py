import connexion
import six

from metal.types.invitation import Invitation  # noqa: E501
from metal.types.invitation_input import InvitationInput  # noqa: E501
from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.membership import Membership  # noqa: E501
from metal import util


def accept_invitation(id):  # noqa: E501
    """Accept an invitation

    Accept an invitation. # noqa: E501

    :param id: Invitation UUID
    :type id: 

    :rtype: Membership
    """
    return 'do some magic!'


def create_organization_invitation(id, invitation):  # noqa: E501
    """Create an invitation for an organization

    In order to add a user to an organization, they must first be invited. To invite to several projects the parameter &#x60;projects_ids:[a,b,c]&#x60; can be used # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param invitation: Invitation to create
    :type invitation: dict | bytes

    :rtype: Invitation
    """
    if connexion.request.is_json:
        invitation = InvitationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_project_invitation(project_id, invitation):  # noqa: E501
    """Create an invitation for a project

    In order to add a user to a project, they must first be invited. # noqa: E501

    :param project_id: Project UUID
    :type project_id: 
    :param invitation: Invitation to create
    :type invitation: dict | bytes

    :rtype: Invitation
    """
    if connexion.request.is_json:
        invitation = InvitationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def decline_invitation(id):  # noqa: E501
    """Decline an invitation

    Decline an invitation. # noqa: E501

    :param id: Invitation UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_invitation_by_id(id, include=None, exclude=None):  # noqa: E501
    """View an invitation

    Returns a single invitation. (It include the &#x60;invitable&#x60; to maintain backward compatibility but will be removed soon) # noqa: E501

    :param id: Invitation UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Invitation
    """
    return 'do some magic!'


def find_invitations(include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve current user invitations

    Returns all invitations in current user. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: InvitationList
    """
    return 'do some magic!'


def find_organization_invitations(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve organization invitations

    Returns all invitations in an organization. # noqa: E501

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

    :rtype: InvitationList
    """
    return 'do some magic!'


def find_project_invitations(project_id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve project invitations

    Returns all invitations in a project. # noqa: E501

    :param project_id: Project UUID
    :type project_id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: InvitationList
    """
    return 'do some magic!'
