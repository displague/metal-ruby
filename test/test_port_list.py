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
from metal.types.port_list import PortList  # noqa: E501
from metal.rest import ApiException

class TestPortList(unittest.TestCase):
    """PortList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PortList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.port_list.PortList()  # noqa: E501
        if include_optional :
            return PortList(
                ports = [
                    metal.models.port.Port(
                        id = '', 
                        type = '', 
                        name = '', 
                        data = metal.models.data.data(), 
                        disbond_operation_supported = True, 
                        hardware = metal.models.href.Href(
                            href = '', ), 
                        virtual_networks = [
                            metal.models.href.Href(
                                href = '', )
                            ], 
                        connected_port = metal.models.href.Href(
                            href = '', ), 
                        href = '', )
                    ]
            )
        else :
            return PortList(
        )

    def testPortList(self):
        """Test PortList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()