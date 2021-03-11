import connexion
import six

from metal.types.recovery_code_list import RecoveryCodeList  # noqa: E501
from metal import util


def find_ensure_otp(otp):  # noqa: E501
    """Verify user by providing an OTP

    It verifies the user once a valid OTP is provided. It gives back a session token, essentially logging in the user. # noqa: E501

    :param otp: OTP
    :type otp: str

    :rtype: None
    """
    return 'do some magic!'


def find_recovery_codes():  # noqa: E501
    """Retrieve my recovery codes

    Returns my recovery codes. # noqa: E501


    :rtype: RecoveryCodeList
    """
    return 'do some magic!'


def receive_codes():  # noqa: E501
    """Receive an OTP per sms

    Sends an OTP to the user&#39;s mobile phone. # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def regenerate_codes():  # noqa: E501
    """Generate new recovery codes

    Generate a new set of recovery codes. # noqa: E501


    :rtype: RecoveryCodeList
    """
    return 'do some magic!'
