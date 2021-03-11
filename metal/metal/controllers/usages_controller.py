import connexion
import six

from metal.types.device_usage_list import DeviceUsageList  # noqa: E501
from metal.types.project_usage_list import ProjectUsageList  # noqa: E501
from metal import util


def find_device_usages(id, created_after=None, created_before=None):  # noqa: E501
    """Retrieve all usages for device

    Returns all usages for a device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param created_after: Filter usages created after this date
    :type created_after: str
    :param created_before: Filter usages created before this date
    :type created_before: str

    :rtype: DeviceUsageList
    """
    return 'do some magic!'


def find_project_usage(id, created_after=None, created_before=None):  # noqa: E501
    """Retrieve all usages for project

    Returns all usages for a project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param created_after: Filter usages created after this date
    :type created_after: str
    :param created_before: Filter usages created before this date
    :type created_before: str

    :rtype: ProjectUsageList
    """
    return 'do some magic!'
