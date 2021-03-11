import connexion
import six

from metal.types.bgp_session_input import BGPSessionInput  # noqa: E501
from metal.types.batches_list import BatchesList  # noqa: E501
from metal.types.bgp_session import BgpSession  # noqa: E501
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.types.bgp_session_neighbors import BgpSessionNeighbors  # noqa: E501
from metal.types.device import Device  # noqa: E501
from metal.types.device_create_input import DeviceCreateInput  # noqa: E501
from metal.types.device_list import DeviceList  # noqa: E501
from metal.types.device_update_input import DeviceUpdateInput  # noqa: E501
from metal.types.device_usage_list import DeviceUsageList  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal.types.ip_assignment import IPAssignment  # noqa: E501
from metal.types.ip_assignment_input import IPAssignmentInput  # noqa: E501
from metal.types.ip_assignment_list import IPAssignmentList  # noqa: E501
from metal.types.instances_batch_create_input import InstancesBatchCreateInput  # noqa: E501
from metal.types.project_usage_list import ProjectUsageList  # noqa: E501
from metal.types.timeframe import Timeframe  # noqa: E501
from metal import util


def create_bgp_session(id, bgp_session):  # noqa: E501
    """Create a BGP session

    Creates a BGP session. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param bgp_session: BGP session to create
    :type bgp_session: dict | bytes

    :rtype: BgpSession
    """
    if connexion.request.is_json:
        bgp_session = BGPSessionInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_device(id, device):  # noqa: E501
    """Create a device

    Creates a new device and provisions it in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility &#x60;{ \&quot;facility\&quot;: \&quot;f1\&quot; }&#x60; , or you can instruct to create the device in the best available datacenter &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60;. Additionally it is possible to set a prioritized location selection.  For example &#x60;{ \&quot;facility\&quot;: [\&quot;f3\&quot;, \&quot;f2\&quot;, \&quot;any\&quot;] }&#x60; will try to assign to the facility f3, if there are no available f2, and so on. If \&quot;any\&quot; is not specified for \&quot;facility\&quot;, the request will fail unless it can assign in the selected locations.  The &#x60;ip_addresses attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: true }, { \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }, { \&quot;address_family\&quot;: 6, \&quot;public\&quot;: true }] }&#x60; was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }] }&#x60;.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, &#x60;{ \&quot;ip_addresses\&quot;: [..., {\&quot;address_family\&quot;: 4, \&quot;public\&quot;: true, \&quot;ip_reservations\&quot;: [\&quot;uuid1\&quot;, \&quot;uuid2\&quot;]}] }&#x60;  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy.  # noqa: E501

    :param id: Project UUID
    :type id: 
    :param device: Device to create
    :type device: dict | bytes

    :rtype: Device
    """
    if connexion.request.is_json:
        device = DeviceCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_device_batch(id, batch):  # noqa: E501
    """Create a devices batch

    Creates new devices in batch and provisions them in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility &#x60;{ \&quot;facility\&quot;: \&quot;f1\&quot; }&#x60; , or you can instruct to create the device in the best available datacenter &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60;. Additionally it is possible to set a prioritized location selection.  For example &#x60;{ \&quot;facility\&quot;: [\&quot;f3\&quot;, \&quot;f2\&quot;, \&quot;any\&quot;] }&#x60; will try to assign to the facility f3, if there are no available f2, and so on. If \&quot;any\&quot; is not specified for \&quot;facility\&quot;, the request will fail unless it can assign in the selected locations.  With &#x60;{ \&quot;facility\&quot;: \&quot;any\&quot; }&#x60; you have the option to diversify to indicate how many facilities you are willing to be spread across. For this purpose use parameter: &#x60;facility_diversity_level &#x3D; N&#x60;.  For example:  &#x60;{ \&quot;facilities\&quot;: [\&quot;sjc1\&quot;, \&quot;ewr1\&quot;, \&quot;any\&quot;] ,  \&quot;facility_diversity_level\&quot; &#x3D; 1, \&quot;quantity\&quot; &#x3D; 10 }&#x60; will assign 10 devices into the same facility, trying first in \&quot;sjc1\&quot;, and if there aren’t available, it will try in  \&quot;ewr1\&quot;, otherwise any other.  The &#x60;ip_addresses&#x60; attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: true }, { \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }, { \&quot;address_family\&quot;: 6, \&quot;public\&quot;: true }] }&#x60; was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send &#x60;{ \&quot;ip_addresses\&quot;: [{ \&quot;address_family\&quot;: 4, \&quot;public\&quot;: false }] }&#x60;.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, &#x60;{ \&quot;ip_addresses\&quot;: [..., {\&quot;address_family\&quot;: 4, \&quot;public\&quot;: true, \&quot;ip_reservations\&quot;: [\&quot;uuid1\&quot;, \&quot;uuid2\&quot;]}] }&#x60;  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param batch: Batches to create
    :type batch: dict | bytes

    :rtype: BatchesList
    """
    if connexion.request.is_json:
        batch = InstancesBatchCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_ip_assignment(id, ip_assignment):  # noqa: E501
    """Create a ip assignment

    Creates an ip assignment for a device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param ip_assignment: IPAssignment to create
    :type ip_assignment: dict | bytes

    :rtype: IPAssignment
    """
    if connexion.request.is_json:
        ip_assignment = IPAssignmentInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_device(id, force_delete=None):  # noqa: E501
    """Delete the device

    Deletes a device and deprovisions it in our datacenter. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param force_delete: Force the deletion of the device, by detaching any storage volume still active.
    :type force_delete: bool

    :rtype: None
    """
    return 'do some magic!'


def find_bgp_sessions(id):  # noqa: E501
    """Retrieve all BGP sessions

    Provides a listing of available BGP sessions for the device. # noqa: E501

    :param id: Device UUID
    :type id: 

    :rtype: BgpSessionList
    """
    return 'do some magic!'


def find_device_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a device

    Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.                          State value can be one of: active inactive queued or provisioning # noqa: E501

    :param id: Device UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Device
    """
    return 'do some magic!'


def find_device_customdata(id):  # noqa: E501
    """Retrieve the custom metadata of an instance

    Provides the custom metadata stored for this instance in json format # noqa: E501

    :param id: Instance UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_device_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve device&#39;s events

    Returns a list of events pertaining to a specific device # noqa: E501

    :param id: Device UUID
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


def find_instance_bandwidth(id, _from, until):  # noqa: E501
    """Retrieve an instance bandwidth

    Retrieve an instance bandwidth for a given period of time. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param _from: Timestamp from range
    :type _from: str
    :param until: Timestamp to range
    :type until: str

    :rtype: None
    """
    return 'do some magic!'


def find_ip_assignment_customdata(instance_id, id):  # noqa: E501
    """Retrieve the custom metadata of an IP Assignment

    Provides the custom metadata stored for this IP Assignment in json format # noqa: E501

    :param instance_id: Instance UUID
    :type instance_id: 
    :param id: Ip Assignment UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_ip_assignments(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all ip assignments

    Returns all ip assignments for a device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: IPAssignmentList
    """
    return 'do some magic!'


def find_organization_devices(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all devices of an organization

    Provides a collection of devices for a given organization. # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: DeviceList
    """
    return 'do some magic!'


def find_project_devices(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all devices of a project

    Provides a collection of devices for a given project. # noqa: E501

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

    :rtype: DeviceList
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


def find_traffic(id, direction, timeframe, interval=None, bucket=None):  # noqa: E501
    """Retrieve device traffic

    Returns traffic for a specific device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param direction: Traffic direction
    :type direction: str
    :param timeframe: Traffic timeframe
    :type timeframe: dict | bytes
    :param interval: Traffic interval
    :type interval: str
    :param bucket: Traffic bucket
    :type bucket: str

    :rtype: None
    """
    if connexion.request.is_json:
        timeframe = Timeframe.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def get_bgp_neighbor_data(id):  # noqa: E501
    """Retrieve BGP neighbor data for this device

    Provides a summary of the BGP neighbor data associated to the BGP sessions for this device. # noqa: E501

    :param id: Device UUID
    :type id: 

    :rtype: BgpSessionNeighbors
    """
    return 'do some magic!'


def perform_action(id, type):  # noqa: E501
    """Perform an action

    Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.) # noqa: E501

    :param id: Device UUID
    :type id: 
    :param type: Action to perform
    :type type: str

    :rtype: None
    """
    return 'do some magic!'


def update_device(id, device):  # noqa: E501
    """Update the device

    Updates the device. # noqa: E501

    :param id: Device UUID
    :type id: 
    :param device: Facility to update
    :type device: dict | bytes

    :rtype: Device
    """
    if connexion.request.is_json:
        device = DeviceUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
