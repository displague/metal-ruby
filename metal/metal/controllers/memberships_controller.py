import connexion
import six

from metal.types.membership import Membership  # noqa: E501
from metal.types.membership_input import MembershipInput  # noqa: E501
from metal.types.membership_list import MembershipList  # noqa: E501
from metal import util


def delete_membership(id):  # noqa: E501
    """Delete the membership

    Deletes the membership. # noqa: E501

    :param id: Membership UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_membership_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a membership

    Returns a single membership. # noqa: E501

    :param id: Membership UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Membership
    """
    return 'do some magic!'


def find_project_memberships(project_id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve project memberships

    Returns all memberships in a project. # noqa: E501

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

    :rtype: MembershipList
    """
    return 'do some magic!'


def update_membership(id, membership):  # noqa: E501
    """Update the membership

    Updates the membership. # noqa: E501

    :param id: Membership UUID
    :type id: 
    :param membership: Membership to update
    :type membership: dict | bytes

    :rtype: Membership
    """
    if connexion.request.is_json:
        membership = MembershipInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
