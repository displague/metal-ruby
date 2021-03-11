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
from metal.types.volume_update_input import VolumeUpdateInput  # noqa: E501
from metal.rest import ApiException

class TestVolumeUpdateInput(unittest.TestCase):
    """VolumeUpdateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VolumeUpdateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.volume_update_input.VolumeUpdateInput()  # noqa: E501
        if include_optional :
            return VolumeUpdateInput(
                description = '', 
                size = 56, 
                locked = True, 
                billing_cycle = '', 
                customdata = None
            )
        else :
            return VolumeUpdateInput(
        )

    def testVolumeUpdateInput(self):
        """Test VolumeUpdateInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
