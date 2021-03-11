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
from metal.model.staff_facility_little import StaffFacilityLittle
from metal.model.staff_plan import StaffPlan
globals()['StaffFacilityLittle'] = StaffFacilityLittle
globals()['StaffPlan'] = StaffPlan
from metal.model.staff_plan_version import StaffPlanVersion


class TestStaffPlanVersion(unittest.TestCase):
    """StaffPlanVersion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStaffPlanVersion(self):
        """Test StaffPlanVersion"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StaffPlanVersion()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()