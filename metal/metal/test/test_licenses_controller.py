# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.license import License  # noqa: E501
from metal.types.license_create_input import LicenseCreateInput  # noqa: E501
from metal.types.license_list import LicenseList  # noqa: E501
from metal.types.license_update_input import LicenseUpdateInput  # noqa: E501
from metal.test import BaseTestCase


class TestLicensesController(BaseTestCase):
    """LicensesController integration test stubs"""

    def test_create_license(self):
        """Test case for create_license

        Create a License
        """
        license = {
  "size" : 0.8008281904610115,
  "licensee_product_id" : "licensee_product_id",
  "description" : "description"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/licenses'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(license),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_license(self):
        """Test case for delete_license

        Delete the license
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/licenses/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_license_by_id(self):
        """Test case for find_license_by_id

        Retrieve a license
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/licenses/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_project_licenses(self):
        """Test case for find_project_licenses

        Retrieve all licenses
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
            '/metal/v1/projects/{id}/licenses'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_license(self):
        """Test case for update_license

        Update the license
        """
        license = {
  "size" : 0.8008281904610115,
  "description" : "description"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/licenses/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(license),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
