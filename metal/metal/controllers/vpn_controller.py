import connexion
import six

from metal.types.vpn_config import VPNConfig  # noqa: E501
from metal import util


def find_current_user_vpn_config(code):  # noqa: E501
    """Retrieve the client vpn config for current user

    Returns the client vpn config for the currently logged-in user. # noqa: E501

    :param code: Facility code
    :type code: str

    :rtype: VPNConfig
    """
    return 'do some magic!'


def turn_off_current_user_vpn():  # noqa: E501
    """Turn off vpn for the current user

    Turns off vpn for the currently logged-in user. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def turn_on_current_user_vpn():  # noqa: E501
    """Turn on vpn for the current user

    Turns on vpn for the currently logged-in user. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
