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
from metal.model.meta import Meta
from metal.model.user import User
globals()['Meta'] = Meta
globals()['User'] = User
from metal.model.user_list import UserList


class TestUserList(unittest.TestCase):
    """UserList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testUserList(self):
        """Test UserList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = UserList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
