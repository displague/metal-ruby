# coding: utf-8

"""
    Metal API

    This is the API for Equinix Metal Product. Interact with your devices, user account, and projects.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: support@equinixmetal.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import metal
from metal.types.staff_server_rack import StaffServerRack  # noqa: E501
from metal.rest import ApiException

class TestStaffServerRack(unittest.TestCase):
    """StaffServerRack unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test StaffServerRack
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.staff_server_rack.StaffServerRack()  # noqa: E501
        if include_optional :
            return StaffServerRack(
                id = '', 
                slot_number = 56, 
                server_rack = metal.models.staff::server_rack.Staff::ServerRack(
                    id = '', 
                    slot_number = 56, 
                    server_rack = metal.models.staff::server_rack.Staff::ServerRack(
                        id = '', 
                        slot_number = 56, 
                        hardware = None, ), 
                    hardware = None, ), 
                hardware = None
            )
        else :
            return StaffServerRack(
        )

    def testStaffServerRack(self):
        """Test StaffServerRack"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()