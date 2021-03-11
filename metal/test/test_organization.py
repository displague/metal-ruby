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
from metal.model.address import Address
from metal.model.entitlement import Entitlement
from metal.model.href import Href
globals()['Address'] = Address
globals()['Entitlement'] = Entitlement
globals()['Href'] = Href
from metal.model.organization import Organization


class TestOrganization(unittest.TestCase):
    """Organization unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganization(self):
        """Test Organization"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Organization()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()