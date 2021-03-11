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
from metal.types.user import User  # noqa: E501
from metal.rest import ApiException

class TestUser(unittest.TestCase):
    """User unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test User
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.user.User()  # noqa: E501
        if include_optional :
            return User(
                id = '', 
                short_id = '', 
                first_name = '', 
                last_name = '', 
                full_name = '', 
                email = '', 
                avatar_url = '', 
                avatar_thumb_url = '', 
                two_factor_auth = '', 
                max_projects = 56, 
                max_organizations = 56, 
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                timezone = '', 
                fraud_score = '', 
                last_login_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                emails = [
                    metal.models.href.Href(
                        href = '', )
                    ], 
                href = '', 
                phone_number = '', 
                customdata = None
            )
        else :
            return User(
        )

    def testUser(self):
        """Test User"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
