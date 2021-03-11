import connexion
import six

from metal.types.facility_list import FacilityList  # noqa: E501
from metal import util


def find_facilities(include=None, exclude=None):  # noqa: E501
    """Retrieve all facilities

    Provides a listing of available datacenters where you can provision Packet devices. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: FacilityList
    """
    return 'do some magic!'


def find_facilities_by_organization(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all facilities visible by the organization

    Returns a listing of available datacenters for the given organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: FacilityList
    """
    return 'do some magic!'


def find_facilities_by_project(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all facilities visible by the project

    Returns a listing of available datacenters for the given project # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: FacilityList
    """
    return 'do some magic!'
