import connexion
import six

from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.user import User  # noqa: E501
from metal.types.user_list import UserList  # noqa: E501
from metal.types.user_update_input import UserUpdateInput  # noqa: E501
from metal import util


def find_current_user(include=None, exclude=None):  # noqa: E501
    """Retrieve the current user

    Returns the user object for the currently logged-in user. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: User
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


def find_user_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a user

    Returns a single user if the user has access # noqa: E501

    :param id: User UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: User
    """
    return 'do some magic!'


def find_user_customdata(id):  # noqa: E501
    """Retrieve the custom metadata of a user

    Provides the custom metadata stored for this user in json format # noqa: E501

    :param id: User UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_users(include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all users

    Returns a list of users that the are accessible to the current user (all users in the current user’s projects, essentially). # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: UserList
    """
    return 'do some magic!'


def update_current_user(user):  # noqa: E501
    """Update the current user

    Updates the currently logged-in user. # noqa: E501

    :param user: User to update
    :type user: dict | bytes

    :rtype: User
    """
    if connexion.request.is_json:
        user = UserUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
