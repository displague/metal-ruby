import connexion
import six

from metal.types.regions_list import RegionsList  # noqa: E501
from metal import util


def find_regions(include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all regions

    Returns all regions. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: RegionsList
    """
    return 'do some magic!'
