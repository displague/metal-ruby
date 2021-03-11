import connexion
import six

from metal.types.license import License  # noqa: E501
from metal.types.license_create_input import LicenseCreateInput  # noqa: E501
from metal.types.license_list import LicenseList  # noqa: E501
from metal.types.license_update_input import LicenseUpdateInput  # noqa: E501
from metal import util


def create_license(id, license):  # noqa: E501
    """Create a License

    Creates a new license for the given project # noqa: E501

    :param id: Project UUID
    :type id: 
    :param license: License to create
    :type license: dict | bytes

    :rtype: License
    """
    if connexion.request.is_json:
        license = LicenseCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_license(id):  # noqa: E501
    """Delete the license

    Deletes a license. # noqa: E501

    :param id: License UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_license_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a license

    Returns a license # noqa: E501

    :param id: License UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: License
    """
    return 'do some magic!'


def find_project_licenses(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all licenses

    Provides a collection of licenses for a given project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: LicenseList
    """
    return 'do some magic!'


def update_license(id, license):  # noqa: E501
    """Update the license

    Updates the license. # noqa: E501

    :param id: License UUID
    :type id: 
    :param license: License to update
    :type license: dict | bytes

    :rtype: License
    """
    if connexion.request.is_json:
        license = LicenseUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
