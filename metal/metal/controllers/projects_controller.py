import connexion
import six

from metal.types.batches_list import BatchesList  # noqa: E501
from metal.types.bgp_config import BgpConfig  # noqa: E501
from metal.types.bgp_config_request_input import BgpConfigRequestInput  # noqa: E501
from metal.types.bgp_session_list import BgpSessionList  # noqa: E501
from metal.types.device import Device  # noqa: E501
from metal.types.device_create_input import DeviceCreateInput  # noqa: E501
from metal.types.device_list import DeviceList  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal.types.facility_list import FacilityList  # noqa: E501
from metal.types.hardware_reservation_list import HardwareReservationList  # noqa: E501
from metal.types.ip_reservation import IPReservation  # noqa: E501
from metal.types.ip_reservation_list import IPReservationList  # noqa: E501
from metal.types.ip_reservation_request_input import IPReservationRequestInput  # noqa: E501
from metal.types.invitation import Invitation  # noqa: E501
from metal.types.invitation_input import InvitationInput  # noqa: E501
from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.license import License  # noqa: E501
from metal.types.license_create_input import LicenseCreateInput  # noqa: E501
from metal.types.license_list import LicenseList  # noqa: E501
from metal.types.membership_list import MembershipList  # noqa: E501
from metal.types.plan_list import PlanList  # noqa: E501
from metal.types.project import Project  # noqa: E501
from metal.types.project_create_from_root_input import ProjectCreateFromRootInput  # noqa: E501
from metal.types.project_create_input import ProjectCreateInput  # noqa: E501
from metal.types.project_list import ProjectList  # noqa: E501
from metal.types.project_update_input import ProjectUpdateInput  # noqa: E501
from metal.types.ssh_key import SSHKey  # noqa: E501
from metal.types.ssh_key_input import SSHKeyInput  # noqa: E501
from metal.types.ssh_key_list import SSHKeyList  # noqa: E501
from metal.types.spot_market_request import SpotMarketRequest  # noqa: E501
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput  # noqa: E501
from metal.types.spot_market_request_list import SpotMarketRequestList  # noqa: E501
from metal.types.transfer_request import TransferRequest  # noqa: E501
from metal.types.transfer_request_input import TransferRequestInput  # noqa: E501
from metal.types.virtual_network import VirtualNetwork  # noqa: E501
from metal.types.virtual_network_create_input import VirtualNetworkCreateInput  # noqa: E501
from metal.types.virtual_network_list import VirtualNetworkList  # noqa: E501
from metal import util


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


def create_organization_project(id, project):  # noqa: E501
    """Create a project for the organization

    Creates a new project for the organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param project: Project to create
    :type project: dict | bytes

    :rtype: Project
    """
    if connexion.request.is_json:
        project = ProjectCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_project(project):  # noqa: E501
    """Create a project

    Creates a new project for the user default organization. If the user don&#39;t have an organization, a new one will be created. # noqa: E501

    :param project: Project to create
    :type project: dict | bytes

    :rtype: Project
    """
    if connexion.request.is_json:
        project = ProjectCreateFromRootInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_project_invitation(project_id, invitation):  # noqa: E501
    """Create an invitation for a project

    In order to add a user to a project, they must first be invited. # noqa: E501

    :param project_id: Project UUID
    :type project_id: 
    :param invitation: Invitation to create
    :type invitation: dict | bytes

    :rtype: Invitation
    """
    if connexion.request.is_json:
        invitation = InvitationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


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


def create_spot_market_request(id, spot_market_request):  # noqa: E501
    """Create a spot market request

    Creates a new spot market request.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have. For example, if you require a server with a TPM chip, you may specify &#x60;{ \&quot;features\&quot;: { \&quot;tpm\&quot;: \&quot;required\&quot; } }&#x60; (or &#x60;{ \&quot;features\&quot;: [\&quot;tpm\&quot;] }&#x60; in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param spot_market_request: Spot Market Request to create
    :type spot_market_request: dict | bytes

    :rtype: SpotMarketRequest
    """
    if connexion.request.is_json:
        spot_market_request = SpotMarketRequestCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_transfer_request(id, transfer_request):  # noqa: E501
    """Create a transfer request

    Organization owners can transfer their projects to other organizations. # noqa: E501

    :param id: UUID of the project to be transferred
    :type id: 
    :param transfer_request: Transfer Request to create
    :type transfer_request: dict | bytes

    :rtype: TransferRequest
    """
    if connexion.request.is_json:
        transfer_request = TransferRequestInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_virtual_network(id, virtual_network):  # noqa: E501
    """Create an virtual network

    Creates an virtual network. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param virtual_network: Virtual Network to create
    :type virtual_network: dict | bytes

    :rtype: VirtualNetwork
    """
    if connexion.request.is_json:
        virtual_network = VirtualNetworkCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_project(id):  # noqa: E501
    """Delete the project

    Deletes the project. # noqa: E501

    :param id: Project UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_batches_by_project(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all batches by project

    Returns all batches for the given project # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: BatchesList
    """
    return 'do some magic!'


def find_bgp_config_by_project(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a bgp config

    Returns a bgp config # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: BgpConfig
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


def find_ip_reservation_customdata(project_id, id):  # noqa: E501
    """Retrieve the custom metadata of an IP Reservation

    Provides the custom metadata stored for this IP Reservation in json format # noqa: E501

    :param project_id: Project UUID
    :type project_id: 
    :param id: Ip Reservation UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_ip_reservations(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all ip reservations

    Provides a list of IP resevations for a single project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: IPReservationList
    """
    return 'do some magic!'


def find_organization_projects(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all projects of an organization

    Returns a collection of projects that belong to the organization. # noqa: E501

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

    :rtype: ProjectList
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


def find_project_bgp_sessions(id):  # noqa: E501
    """Retrieve all BGP sessions for project

    Provides a listing of available BGP sessions for the project. # noqa: E501

    :param id: Project UUID
    :type id: 

    :rtype: BgpSessionList
    """
    return 'do some magic!'


def find_project_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a project

    Returns a single project if the user has access # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Project
    """
    return 'do some magic!'


def find_project_customdata(id):  # noqa: E501
    """Retrieve the custom metadata of a project

    Provides the custom metadata stored for this project in json format # noqa: E501

    :param id: Project UUID
    :type id: 

    :rtype: None
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


def find_project_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve project&#39;s events

    Returns a list of events for a single project # noqa: E501

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

    :rtype: EventList
    """
    return 'do some magic!'


def find_project_hardware_reservations(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all hardware reservations for a given project

    Provides a collection of hardware reservations for a given project. # noqa: E501

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

    :rtype: HardwareReservationList
    """
    return 'do some magic!'


def find_project_invitations(project_id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve project invitations

    Returns all invitations in a project. # noqa: E501

    :param project_id: Project UUID
    :type project_id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: InvitationList
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


def find_project_memberships(project_id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve project memberships

    Returns all memberships in a project. # noqa: E501

    :param project_id: Project UUID
    :type project_id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: MembershipList
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


def find_projects(include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all projects

    Returns a collection of projects that the current user is a member of. # noqa: E501

    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: ProjectList
    """
    return 'do some magic!'


def find_virtual_networks(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all virtual networks

    Provides a list of virtual networks for a single project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: VirtualNetworkList
    """
    return 'do some magic!'


def list_spot_market_requests(id):  # noqa: E501
    """List spot market requests

    View all spot market requests for a given project. # noqa: E501

    :param id: Project UUID
    :type id: 

    :rtype: SpotMarketRequestList
    """
    return 'do some magic!'


def request_bgp_config(id, bgp_config_request):  # noqa: E501
    """Requesting bgp config

    Requests to enable bgp configuration for a project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param bgp_config_request: BGP config Request to create
    :type bgp_config_request: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        bgp_config_request = BgpConfigRequestInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def request_ip_reservation(id, ip_reservation_request):  # noqa: E501
    """Requesting IP reservations

    Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a &#x60;state&#x60; of &#x60;pending&#x60;. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the &#x60;fail_on_approval_required&#x60; parameter set to &#x60;true&#x60; in the request. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param ip_reservation_request: IP Reservation Request to create
    :type ip_reservation_request: dict | bytes

    :rtype: IPReservation
    """
    if connexion.request.is_json:
        ip_reservation_request = IPReservationRequestInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def update_project(id, project):  # noqa: E501
    """Update the project

    Updates the project. # noqa: E501

    :param id: Project UUID
    :type id: 
    :param project: Project to update
    :type project: dict | bytes

    :rtype: Project
    """
    if connexion.request.is_json:
        project = ProjectUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
