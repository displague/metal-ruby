import connexion
import six

from metal import util


def consume_verification_request(token):  # noqa: E501
    """Verify a user using an email verification token

    Consumes an email verification token and verifies the user associated with it. # noqa: E501

    :param token: User verification token
    :type token: str

    :rtype: None
    """
    return 'do some magic!'


def create_validation_request(login):  # noqa: E501
    """Create an email verification request

    Creates an email verification request # noqa: E501

    :param login: Email for verification request
    :type login: str

    :rtype: None
    """
    return 'do some magic!'
