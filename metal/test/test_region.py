"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import metal
from metal.model.facility import Facility
globals()['Facility'] = Facility
from metal.model.region import Region


class TestRegion(unittest.TestCase):
    """Region unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRegion(self):
        """Test Region"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Region()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()