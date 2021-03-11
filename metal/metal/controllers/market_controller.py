import connexion
import six

from metal.types.spot_market_prices_list import SpotMarketPricesList  # noqa: E501
from metal.types.spot_prices_history_report import SpotPricesHistoryReport  # noqa: E501
from metal import util


def find_spot_market_prices(facility=None, plan=None):  # noqa: E501
    """Get current spot market prices

    Get Equinix Metal current spot market prices. # noqa: E501

    :param facility: Facility to check spot market prices
    :type facility: str
    :param plan: Plan to check spot market prices
    :type plan: str

    :rtype: SpotMarketPricesList
    """
    return 'do some magic!'


def find_spot_market_prices_history(facility, plan, _from, until):  # noqa: E501
    """Get spot market prices for a given period of time

    Get spot market prices for a given plan and facility in a fixed period of time  *Note: In the &#x60;200&#x60; response, the property &#x60;datapoints&#x60; contains arrays of &#x60;[float, integer]&#x60;.* # noqa: E501

    :param facility: Facility to check spot market prices
    :type facility: str
    :param plan: Plan to check spot market prices
    :type plan: str
    :param _from: Timestamp from range
    :type _from: str
    :param until: Timestamp to range
    :type until: str

    :rtype: SpotPricesHistoryReport
    """
    return 'do some magic!'
