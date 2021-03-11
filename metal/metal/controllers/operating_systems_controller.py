import connexion
import six

from metal.types.operating_system import OperatingSystem  # noqa: E501
from metal import util


def find_operating_systems():  # noqa: E501
    """Retrieve all operating systems

    Provides a listing of available operating systems to provision your new device with. # noqa: E501


    :rtype: List[OperatingSystem]
    """
    return 'do some magic!'


def find_operating_systems_by_organization(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all operating systems visible by the organization

    Returns a listing of available operating systems for the given organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: List[OperatingSystem]
    """
    return 'do some magic!'
