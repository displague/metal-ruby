import connexion
import six

from metal.types.event_list import EventList  # noqa: E501
from metal.types.snapshot_policy import SnapshotPolicy  # noqa: E501
from metal.types.volume import Volume  # noqa: E501
from metal.types.volume_attachment import VolumeAttachment  # noqa: E501
from metal.types.volume_attachment_input import VolumeAttachmentInput  # noqa: E501
from metal.types.volume_attachment_list import VolumeAttachmentList  # noqa: E501
from metal.types.volume_create_input import VolumeCreateInput  # noqa: E501
from metal.types.volume_list import VolumeList  # noqa: E501
from metal.types.volume_snapshot_list import VolumeSnapshotList  # noqa: E501
from metal.types.volume_update_input import VolumeUpdateInput  # noqa: E501
from metal import util


def clone_volume(id, snapshot_timestamp=None):  # noqa: E501
    """Clone volume/snapshot

    Clone your volume or snapshot into a new volume. To clone the volume, send an empty body. To promote a volume snapshot into a new volume, include the snapshot_timestamp attribute in the request body. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param snapshot_timestamp: snapshot timestamp
    :type snapshot_timestamp: str

    :rtype: Volume
    """
    return 'do some magic!'


def create_volume(id, volume):  # noqa: E501
    """Create a volume

    Creates a new volume in our datacenter. The valid attribute values for &#x60;plan&#x60; and &#x60;facility&#x60; are:           \&quot;facility\&quot;: \&quot;ams1\&quot;, \&quot;ewr1\&quot;, \&quot;nrt1\&quot;, \&quot;sjc1\&quot;          \&quot;plan\&quot;: \&quot;storage_1\&quot; (Standard), \&quot;storage_2\&quot; (Performance) # noqa: E501

    :param id: Project UUID
    :type id: 
    :param volume: Volume to create
    :type volume: dict | bytes

    :rtype: Volume
    """
    if connexion.request.is_json:
        volume = VolumeCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_volume_attachment(id, attachment):  # noqa: E501
    """Attach your volume

    Attach your volume to a device. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param attachment: Device to attach
    :type attachment: dict | bytes

    :rtype: VolumeAttachment
    """
    if connexion.request.is_json:
        attachment = VolumeAttachmentInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_volume_snapshot_policy(id, snapshot_frequency, snapshot_count=None):  # noqa: E501
    """Create a volume snapshot policy

    Creates a new snapshot policy of your volume. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param snapshot_frequency: Snapshot frequency
    :type snapshot_frequency: str
    :param snapshot_count: Snapshot count
    :type snapshot_count: int

    :rtype: SnapshotPolicy
    """
    return 'do some magic!'


def delete_volume(id):  # noqa: E501
    """Delete the volume

    Deletes the volume. # noqa: E501

    :param id: Volume UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def delete_volume_attachment(id):  # noqa: E501
    """Detach volume

    Detach volume. # noqa: E501

    :param id: Attachment UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def delete_volume_snapshot(volume_id, id):  # noqa: E501
    """Delete volume snapshot

    Delete volume snapshot. # noqa: E501

    :param volume_id: Volume UUID
    :type volume_id: 
    :param id: Snapshot UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def delete_volume_snapshot_policy(id):  # noqa: E501
    """Delete the volume snapshot policy

    Deletes the volume snapshot policy. # noqa: E501

    :param id: Snapshot Policy UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_volume_attachment_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve an attachment

    Returns a single attachment if the user has access # noqa: E501

    :param id: Attachment UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: VolumeAttachment
    """
    return 'do some magic!'


def find_volume_attachments(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all volume attachment

    Returns a list of the current volume’s attachments. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: VolumeAttachmentList
    """
    return 'do some magic!'


def find_volume_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a volume

    Returns a single volume if the user has access # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Volume
    """
    return 'do some magic!'


def find_volume_customdata(id):  # noqa: E501
    """Retrieve the custom metadata of a storage volume

    Provides the custom metadata stored for this storage volume in json format # noqa: E501

    :param id: Storage Volume UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_volume_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve volume&#39;s events

    Returns a list of the current volume’s events # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: EventList
    """
    return 'do some magic!'


def find_volume_snapshots(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all volume snapshot

    Returns a list of the current volume’s snapshots. To create Volume Snapshots, please check the Volume Snapshot Policies feature. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: VolumeSnapshotList
    """
    return 'do some magic!'


def find_volumes(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all volumes

    Returns a list of the current projects’s volumes. # noqa: E501

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

    :rtype: VolumeList
    """
    return 'do some magic!'


def restore_volume(id, restore_point):  # noqa: E501
    """Restore volume

    Restore the volume to the given snapshot. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param restore_point: restore point
    :type restore_point: str

    :rtype: Volume
    """
    return 'do some magic!'


def update_volume(id, volume):  # noqa: E501
    """Update the volume

    Updates the volume. # noqa: E501

    :param id: Volume UUID
    :type id: 
    :param volume: Volume to update
    :type volume: dict | bytes

    :rtype: Volume
    """
    if connexion.request.is_json:
        volume = VolumeUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_volume_snapshot_policy(id, snapshot_frequency, snapshot_count=None):  # noqa: E501
    """Update the volume snapshot policy

    Updates the volume snapshot policy. # noqa: E501

    :param id: Snapshot Policy UUID
    :type id: 
    :param snapshot_frequency: Snapshot frequency
    :type snapshot_frequency: str
    :param snapshot_count: Snapshot count
    :type snapshot_count: int

    :rtype: SnapshotPolicy
    """
    return 'do some magic!'
