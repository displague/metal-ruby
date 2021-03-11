# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.transfer_request import TransferRequest  # noqa: E501
from metal.types.transfer_request_input import TransferRequestInput  # noqa: E501
from metal.types.transfer_request_list import TransferRequestList  # noqa: E501
from metal.test import BaseTestCase


class TestTransferRequestsController(BaseTestCase):
    """TransferRequestsController integration test stubs"""

    def test_accept_transfer_request(self):
        """Test case for accept_transfer_request

        Accept a transfer request
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/transfers/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_transfer_request(self):
        """Test case for create_transfer_request

        Create a transfer request
        """
        transfer_request = {
  "target_organization_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/transfers'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(transfer_request),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_decline_transfer_request(self):
        """Test case for decline_transfer_request

        Decline a transfer request
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/transfers/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_organization_transfers(self):
        """Test case for find_organization_transfers

        Retrieve all project transfer requests from or to an organization
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/organizations/{id}/transfers'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_transfer_request_by_id(self):
        """Test case for find_transfer_request_by_id

        View a transfer request
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/transfers/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
