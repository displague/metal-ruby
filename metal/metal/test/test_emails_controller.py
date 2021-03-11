# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.create_email_input import CreateEmailInput  # noqa: E501
from metal.types.email import Email  # noqa: E501
from metal.types.update_email_input import UpdateEmailInput  # noqa: E501
from metal.test import BaseTestCase


class TestEmailsController(BaseTestCase):
    """EmailsController integration test stubs"""

    def test_create_email(self):
        """Test case for create_email

        Create an email
        """
        email = {
  "address" : "address"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/emails',
            method='POST',
            headers=headers,
            data=json.dumps(email),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_email(self):
        """Test case for delete_email

        Delete the email
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/emails/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_email_by_id(self):
        """Test case for find_email_by_id

        Retrieve an email
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/emails/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_email(self):
        """Test case for update_email

        Update the email
        """
        email = {
  "default" : true
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/emails/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(email),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
