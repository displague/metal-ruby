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
from metal.types.payment_method_list import PaymentMethodList  # noqa: E501
from metal.rest import ApiException

class TestPaymentMethodList(unittest.TestCase):
    """PaymentMethodList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test PaymentMethodList
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = metal.models.payment_method_list.PaymentMethodList()  # noqa: E501
        if include_optional :
            return PaymentMethodList(
                payment_methods = [
                    metal.models.payment_method.PaymentMethod(
                        id = '', 
                        name = '', 
                        type = '', 
                        default = True, 
                        created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        card_type = '', 
                        expiration_month = '', 
                        expiration_year = '', 
                        cardholder_name = '', 
                        billing_address = metal.models.payment_method_billing_address.PaymentMethodBillingAddress(
                            street_address = '', 
                            postal_code = '', 
                            country_code_alpha2 = '', ), 
                        email = '', 
                        created_by_user = metal.models.href.Href(
                            href = '', ), 
                        organization = metal.models.href.Href(
                            href = '', ), 
                        projects = [
                            metal.models.href.Href(
                                href = '', )
                            ], )
                    ]
            )
        else :
            return PaymentMethodList(
        )

    def testPaymentMethodList(self):
        """Test PaymentMethodList"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
