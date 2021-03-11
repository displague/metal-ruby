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
from metal.types.volume_list import VolumeList  # noqa: E501
from metal.rest import ApiException

class TestVolumeList(unittest.TestCase):
    """VolumeList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test VolumeList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.volume_list.VolumeList()  # noqa: E501
        if include_optional :
            return VolumeList(
                volumes = [
                    metal.models.volume.Volume(
                        id = '', 
                        name = '', 
                        description = '', 
                        size = 56, 
                        locked = True, 
                        billing_cycle = '', 
                        state = '', 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        project = metal.models.href.Href(
                            href = '', ), 
                        facility = metal.models.href.Href(
                            href = '', ), 
                        snapshot_policies = [
                            metal.models.href.Href(
                                href = '', )
                            ], 
                        attachments = [
                            metal.models.href.Href(
                                href = '', )
                            ], 
                        plan = metal.models.plan.Plan(
                            id = '', 
                            slug = '', 
                            name = '', 
                            description = '', 
                            line = '', 
                            specs = metal.models.specs.specs(), 
                            pricing = metal.models.pricing.pricing(), 
                            legacy = True, 
                            class = '', 
                            available_in = [
                                metal.models.href.Href(
                                    href = '', )
                                ], ), 
                        href = '', 
                        customdata = metal.models.customdata.customdata(), )
                    ], 
                meta = metal.models.meta.Meta(
                    first = metal.models.href.Href(
                        href = '', ), 
                    previous = metal.models.href.Href(
                        href = '', ), 
                    self = metal.models.href.Href(
                        href = '', ), 
                    next = metal.models.href.Href(
                        href = '', ), 
                    last = metal.models.href.Href(
                        href = '', ), 
                    total = 56, )
            )
        else :
            return VolumeList(
        )

    def testVolumeList(self):
        """Test VolumeList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
