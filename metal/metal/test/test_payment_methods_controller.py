# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.payment_method import PaymentMethod  # noqa: E501
from metal.types.payment_method_create_input import PaymentMethodCreateInput  # noqa: E501
from metal.types.payment_method_list import PaymentMethodList  # noqa: E501
from metal.types.payment_method_update_input import PaymentMethodUpdateInput  # noqa: E501
from metal.test import BaseTestCase


class TestPaymentMethodsController(BaseTestCase):
    """PaymentMethodsController integration test stubs"""

    def test_create_payment_method(self):
        """Test case for create_payment_method

        Create a payment method for the given organization
        """
        payment_method = {
  "default" : true,
  "name" : "name",
  "nonce" : "nonce"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/payment-methods'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(payment_method),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_payment_method(self):
        """Test case for delete_payment_method

        Delete the payment method
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/payment-methods/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_payment_methods(self):
        """Test case for find_organization_payment_methods

        Retrieve all payment methods of an organization
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example']),
                        ('page', 1),
                        ('per_page', 10)]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/payment-methods'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_payment_method_by_id(self):
        """Test case for find_payment_method_by_id

        Retrieve a payment method
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/payment-methods/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_payment_method(self):
        """Test case for update_payment_method

        Update the payment method
        """
        payment_method = {
  "expiration_year" : 0,
  "default" : true,
  "name" : "name",
  "expiration_month" : "expiration_month",
  "billing_address" : "{}",
  "cardholder_name" : "cardholder_name"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/payment-methods/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(payment_method),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
