import connexion
import six

from metal.types.payment_method import PaymentMethod  # noqa: E501
from metal.types.payment_method_create_input import PaymentMethodCreateInput  # noqa: E501
from metal.types.payment_method_list import PaymentMethodList  # noqa: E501
from metal.types.payment_method_update_input import PaymentMethodUpdateInput  # noqa: E501
from metal import util


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


def delete_payment_method(id):  # noqa: E501
    """Delete the payment method

    Deletes the payment method. # noqa: E501

    :param id: Payment Method UUID
    :type id: 

    :rtype: None
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


def find_payment_method_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a payment method

    Returns a payment method # noqa: E501

    :param id: Payment Method UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: PaymentMethod
    """
    return 'do some magic!'


def update_payment_method(id, payment_method):  # noqa: E501
    """Update the payment method

    Updates the payment method. # noqa: E501

    :param id: Payment Method UUID
    :type id: 
    :param payment_method: Payment Method to update
    :type payment_method: dict | bytes

    :rtype: PaymentMethod
    """
    if connexion.request.is_json:
        payment_method = PaymentMethodUpdateInput.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
