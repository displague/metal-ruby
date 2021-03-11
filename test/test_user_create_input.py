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
from metal.types.user_create_input import UserCreateInput  # noqa: E501
from metal.rest import ApiException

class TestUserCreateInput(unittest.TestCase):
    """UserCreateInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test UserCreateInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.user_create_input.UserCreateInput()  # noqa: E501
        if include_optional :
            return UserCreateInput(
                first_name = '', 
                last_name = '', 
                phone_number = '', 
                timezone = '', 
                password = '', 
                level = '', 
                title = '', 
                company_name = '', 
                company_url = '', 
                verified_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                social_accounts = None, 
                two_factor_auth = '', 
                avatar = bytes(b'blah'), 
                emails = [
                    metal.models.email_input.EmailInput(
                        address = '', 
                        default = True, )
                    ], 
                locked = True, 
                customdata = None
            )
        else :
            return UserCreateInput(
                first_name = '',
                last_name = '',
                emails = [
                    metal.models.email_input.EmailInput(
                        address = '', 
                        default = True, )
                    ],
        )

    def testUserCreateInput(self):
        """Test UserCreateInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()