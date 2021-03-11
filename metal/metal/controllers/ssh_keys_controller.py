import connexion
import six

from metal.types.ssh_key import SSHKey  # noqa: E501
from metal.types.ssh_key_input import SSHKeyInput  # noqa: E501
from metal.types.ssh_key_list import SSHKeyList  # noqa: E501
from metal import util


def create_project_ssh_key(id, ssh_key):  # noqa: E501
    """Create a ssh key for the given project

    Creates a ssh key. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param ssh_key: ssh key to create
    :type ssh_key: dict | bytes

    :rtype: SSHKey
    """
    if connexion.request.is_json:
        ssh_key = SSHKeyInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_ssh_key(ssh_key):  # noqa: E501
    """Create a ssh key for the current user

    Creates a ssh key. # noqa: E501

    :param ssh_key: ssh key to create
    :type ssh_key: dict | bytes

    :rtype: SSHKey
    """
    if connexion.request.is_json:
        ssh_key = SSHKeyInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_ssh_key(id):  # noqa: E501
    """Delete the ssh key

    Deletes the ssh key. # noqa: E501

    :param id: ssh key UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_device_ssh_keys(id, search_string=None, include=None, exclude=None):  # noqa: E501
    """Retrieve a device&#39;s ssh keys

    Returns a collection of the device&#39;s ssh keys. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param search_string: Search by key, label, or fingerprint
    :type search_string: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: SSHKeyList
    """
    return 'do some magic!'


def find_project_ssh_keys(id, search_string=None, include=None, exclude=None):  # noqa: E501
    """Retrieve a project&#39;s ssh keys

    Returns a collection of the project&#39;s ssh keys. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param search_string: Search by key, label, or fingerprint
    :type search_string: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: SSHKeyList
    """
    return 'do some magic!'


def find_ssh_key_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a ssh key

    Returns a single ssh key if the user has access # noqa: E501

    :param id: SSH Key UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: SSHKey
    """
    return 'do some magic!'


def find_ssh_keys(search_string=None, include=None, exclude=None):  # noqa: E501
    """Retrieve all ssh keys

    Returns a collection of the user’s ssh keys. # noqa: E501

    :param search_string: Search by key, label, or fingerprint
    :type search_string: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: SSHKeyList
    """
    return 'do some magic!'


def update_ssh_key(id, ssh_key):  # noqa: E501
    """Update the ssh key

    Updates the ssh key. # noqa: E501

    :param id: SSH Key UUID
    :type id: 
    :param ssh_key: ssh key to update
    :type ssh_key: dict | bytes

    :rtype: SSHKey
    """
    if connexion.request.is_json:
        ssh_key = SSHKeyInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
