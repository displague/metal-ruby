import connexion
import six

from metal.types.new_password import NewPassword  # noqa: E501
from metal import util


def create_password_reset_token(email):  # noqa: E501
    """Create a password reset token

    Creates a password reset token # noqa: E501

    :param email: Email of user to create password reset token
    :type email: str

    :rtype: None
    """
    return 'do some magic!'


def reset_password():  # noqa: E501
    """Reset current user password

    Resets current user password. # noqa: E501


    :rtype: NewPassword
    """
    return 'do some magic!'
