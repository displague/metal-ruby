import connexion
import six

from metal.types.internet_gateway import InternetGateway  # noqa: E501
from metal import util


def create_internet_gateway(id, length):  # noqa: E501
    """Create an internet gateway

    Creates an internet gateway. # noqa: E501

    :param id: Virtual Network UUID
    :type id: 
    :param length: IP Reservation length
    :type length: str

    :rtype: InternetGateway
    """
    return 'do some magic!'
