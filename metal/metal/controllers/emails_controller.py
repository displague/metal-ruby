import connexion
import six

from metal.types.create_email_input import CreateEmailInput  # noqa: E501
from metal.types.email import Email  # noqa: E501
from metal.types.update_email_input import UpdateEmailInput  # noqa: E501
from metal import util


def create_email(email):  # noqa: E501
    """Create an email

    Add a new email address to the current user. # noqa: E501

    :param email: Email to create
    :type email: dict | bytes

    :rtype: Email
    """
    if connexion.request.is_json:
        email = CreateEmailInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_email(id):  # noqa: E501
    """Delete the email

    Deletes the email. # noqa: E501

    :param id: Email UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_email_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve an email

    Provides one of the user’s emails. # noqa: E501

    :param id: Email UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Email
    """
    return 'do some magic!'


def update_email(id, email):  # noqa: E501
    """Update the email

    Updates the email. # noqa: E501

    :param id: Email UUID
    :type id: 
    :param email: email to update
    :type email: dict | bytes

    :rtype: Email
    """
    if connexion.request.is_json:
        email = UpdateEmailInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
