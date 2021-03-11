import connexion
import six

from metal.types.capacity_check_per_facility_list import CapacityCheckPerFacilityList  # noqa: E501
from metal.types.capacity_input import CapacityInput  # noqa: E501
from metal.types.capacity_list import CapacityList  # noqa: E501
from metal import util


def check_capacity_for_facility(facility):  # noqa: E501
    """Check capacity

    Validates if a deploy can be fulfilled. # noqa: E501

    :param facility: Facility to check capacity in
    :type facility: dict | bytes

    :rtype: CapacityCheckPerFacilityList
    """
    if connexion.request.is_json:
        facility = CapacityInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def find_capacity_for_facility():  # noqa: E501
    """View capacity

    Returns a list of facilities and plans with their current capacity. # noqa: E501


    :rtype: CapacityList
    """
    return 'do some magic!'
