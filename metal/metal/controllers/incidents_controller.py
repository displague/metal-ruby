import connexion
import six

from metal import util


def incidents_get(include=None, exclude=None):  # noqa: E501
    """Retrieve the number of incidents

    Retrieve the number of incidents. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: None
    """
    return 'do some magic!'
