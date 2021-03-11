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
from metal.types.regions_list import RegionsList  # noqa: E501
from metal.rest import ApiException

class TestRegionsList(unittest.TestCase):
    """RegionsList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test RegionsList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.regions_list.RegionsList()  # noqa: E501
        if include_optional :
            return RegionsList(
                regions = [
                    metal.models.region.Region(
                        id = '', 
                        name = '', 
                        facility = metal.models.facility.Facility(
                            id = '', 
                            name = '', 
                            code = '', 
                            features = [
                                ''
                                ], 
                            address = metal.models.address.Address(
                                address = '', 
                                address2 = '', 
                                city = '', 
                                state = '', 
                                zip_code = '', 
                                country = '', 
                                coordinates = metal.models.coordinates.Coordinates(
                                    latitude = '', 
                                    longitude = '', ), ), ), )
                    ]
            )
        else :
            return RegionsList(
        )

    def testRegionsList(self):
        """Test RegionsList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
