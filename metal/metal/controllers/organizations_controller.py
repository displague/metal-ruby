import connexion
import six

from metal.types.device_list import DeviceList  # noqa: E501
from metal.types.event_list import EventList  # noqa: E501
from metal.types.facility_list import FacilityList  # noqa: E501
from metal.types.invitation import Invitation  # noqa: E501
from metal.types.invitation_input import InvitationInput  # noqa: E501
from metal.types.invitation_list import InvitationList  # noqa: E501
from metal.types.operating_system import OperatingSystem  # noqa: E501
from metal.types.organization import Organization  # noqa: E501
from metal.types.organization_input import OrganizationInput  # noqa: E501
from metal.types.organization_list import OrganizationList  # noqa: E501
from metal.types.payment_method import PaymentMethod  # noqa: E501
from metal.types.payment_method_create_input import PaymentMethodCreateInput  # noqa: E501
from metal.types.payment_method_list import PaymentMethodList  # noqa: E501
from metal.types.plan_list import PlanList  # noqa: E501
from metal.types.project import Project  # noqa: E501
from metal.types.project_create_input import ProjectCreateInput  # noqa: E501
from metal.types.project_list import ProjectList  # noqa: E501
from metal.types.transfer_request_list import TransferRequestList  # noqa: E501
from metal import util


def create_organization(organization):  # noqa: E501
    """Create an organization

    Creates an organization. # noqa: E501

    :param organization: Organization to create
    :type organization: dict | bytes

    :rtype: Organization
    """
    if connexion.request.is_json:
        organization = OrganizationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def create_organization_invitation(id, invitation):  # noqa: E501
    """Create an invitation for an organization

    In order to add a user to an organization, they must first be invited. To invite to several projects the parameter &#x60;projects_ids:[a,b,c]&#x60; can be used # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param invitation: Invitation to create
    :type invitation: dict | bytes

    :rtype: Invitation
    """
    if connexion.request.is_json:
        invitation = InvitationInput.from_dict(connexion.request.get_json())  # noqa: E501
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


def create_payment_method(id, payment_method):  # noqa: E501
    """Create a payment method for the given organization

    Creates a payment method. # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param payment_method: Payment Method to create
    :type payment_method: dict | bytes

    :rtype: PaymentMethod
    """
    if connexion.request.is_json:
        payment_method = PaymentMethodCreateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def delete_organization(id):  # noqa: E501
    """Delete the organization

    Deletes the organization. # noqa: E501

    :param id: Organization UUID
    :type id: 

    :rtype: None
    """
    return 'do some magic!'


def find_facilities_by_organization(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all facilities visible by the organization

    Returns a listing of available datacenters for the given organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: FacilityList
    """
    return 'do some magic!'


def find_operating_systems_by_organization(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all operating systems visible by the organization

    Returns a listing of available operating systems for the given organization # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: List[OperatingSystem]
    """
    return 'do some magic!'


def find_organization_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve an organization&#39;s details

    Returns a single organization&#39;s details, if the user is authorized to view it. # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: Organization
    """
    return 'do some magic!'


def find_organization_customdata(id):  # noqa: E501
    """Retrieve the custom metadata of an organization

    Provides the custom metadata stored for this organization in json format # noqa: E501

    :param id: Organization UUID
    :type id: 

    :rtype: None
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


def find_organization_events(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve organization&#39;s events

    Returns a list of events for a single organization # noqa: E501

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

    :rtype: EventList
    """
    return 'do some magic!'


def find_organization_invitations(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve organization invitations

    Returns all invitations in an organization. # noqa: E501

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

    :rtype: InvitationList
    """
    return 'do some magic!'


def find_organization_payment_methods(id, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all payment methods of an organization

    Returns all payment methods of an organization. # noqa: E501

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

    :rtype: PaymentMethodList
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


def find_organization_transfers(id, include=None, exclude=None):  # noqa: E501
    """Retrieve all project transfer requests from or to an organization

    Provides a collection of project transfer requests from or to the organization. # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: TransferRequestList
    """
    return 'do some magic!'


def find_organizations(personal=None, without_projects=None, include=None, exclude=None, page=None, per_page=None):  # noqa: E501
    """Retrieve all organizations

    Returns a list of organizations that are accessible to the current user. # noqa: E501

    :param personal: Include, exclude or show only personal organizations.
    :type personal: str
    :param without_projects: Include, exclude or show only organizations that have no projects.
    :type without_projects: str
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]
    :param page: Page to return
    :type page: int
    :param per_page: Items returned per page
    :type per_page: int

    :rtype: OrganizationList
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


def update_organization(id, organization):  # noqa: E501
    """Update the organization

    Updates the organization. # noqa: E501

    :param id: Organization UUID
    :type id: 
    :param organization: Organization to update
    :type organization: dict | bytes

    :rtype: Organization
    """
    if connexion.request.is_json:
        organization = OrganizationInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
