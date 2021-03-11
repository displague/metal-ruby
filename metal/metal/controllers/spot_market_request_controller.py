import connexion
import six

from metal.types.spot_market_request import SpotMarketRequest  # noqa: E501
from metal.types.spot_market_request_create_input import SpotMarketRequestCreateInput  # noqa: E501
from metal.types.spot_market_request_list import SpotMarketRequestList  # noqa: E501
from metal import util


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


def delete_spot_market_request(id, force_termination=None):  # noqa: E501
    """Delete the spot market request

    Deletes the spot market request. # noqa: E501

    :param id: SpotMarketRequest UUID
    :type id: 
    :param force_termination: Terminate associated spot instances
    :type force_termination: bool

    :rtype: None
    """
    return 'do some magic!'


def find_spot_market_request_by_id(id, include=None, exclude=None):  # noqa: E501
    """Retrieve a spot market request

    Returns a single spot market request # noqa: E501

    :param id: SpotMarketRequest UUID
    :type id: 
    :param include: Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
    :type include: List[str]
    :param exclude: Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
    :type exclude: List[str]

    :rtype: SpotMarketRequest
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
