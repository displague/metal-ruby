import connexion
import six

from metal.types.plan_list import PlanList  # noqa: E501
from metal import util


def find_plans(include=None, exclude=None):  # noqa: E501
    """Retrieve all plans

    Provides a listing of available plans to provision your device on. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: PlanList
    """
    return 'do some magic!'


def find_plans_by_organization(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all plans visible by the organization

    Returns a listing of available plans for the given organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: PlanList
    """
    return 'do some magic!'


def find_plans_by_project(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all plans visible by the project

    Returns a listing of available plans for the given project # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: PlanList
    """
    return 'do some magic!'
