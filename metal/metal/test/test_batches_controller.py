# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.batch import Batch  # noqa: E501
from metal.types.batches_list import BatchesList  # noqa: E501
from metal.types.instances_batch_create_input import InstancesBatchCreateInput  # noqa: E501
from metal.test import BaseTestCase


class TestBatchesController(BaseTestCase):
    """BatchesController integration test stubs"""

    def test_create_device_batch(self):
        """Test case for create_device_batch

        Create a devices batch
        """
        batch = {
  "batches" : [ {
    "user_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "ip_addresses" : [ {
      "address_family" : 4.0,
      "public" : false,
      "ip_reservations" : [ "ip_reservations", "ip_reservations" ],
      "cidr" : 28.0
    }, {
      "address_family" : 4.0,
      "public" : false,
      "ip_reservations" : [ "ip_reservations", "ip_reservations" ],
      "cidr" : 28.0
    } ],
    "description" : "description",
    "hostnames" : [ "hostnames", "hostnames" ],
    "termination_time" : "2000-01-23T04:56:07.000+00:00",
    "tags" : [ "tags", "tags" ],
    "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "userdata" : "userdata",
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "operating_system" : "operating_system",
    "billing_cycle" : "billing_cycle",
    "always_pxe" : true,
    "customdata" : "{}",
    "locked" : true,
    "plan" : "plan"
  }, {
    "user_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "ip_addresses" : [ {
      "address_family" : 4.0,
      "public" : false,
      "ip_reservations" : [ "ip_reservations", "ip_reservations" ],
      "cidr" : 28.0
    }, {
      "address_family" : 4.0,
      "public" : false,
      "ip_reservations" : [ "ip_reservations", "ip_reservations" ],
      "cidr" : 28.0
    } ],
    "description" : "description",
    "hostnames" : [ "hostnames", "hostnames" ],
    "termination_time" : "2000-01-23T04:56:07.000+00:00",
    "tags" : [ "tags", "tags" ],
    "project_ssh_keys" : [ "046b6c7f-0b8a-43b9-b35d-6489e6daee91", "046b6c7f-0b8a-43b9-b35d-6489e6daee91" ],
    "userdata" : "userdata",
    "features" : [ "features", "features" ],
    "hostname" : "hostname",
    "operating_system" : "operating_system",
    "billing_cycle" : "billing_cycle",
    "always_pxe" : true,
    "customdata" : "{}",
    "locked" : true,
    "plan" : "plan"
  } ]
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/devices/batch'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(batch),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_batch(self):
        """Test case for delete_batch

        Delete the Batch
        """
        remove_associated_instances = True
        headers = { 
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/batches/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers,
            data=json.dumps(remove_associated_instances),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_batch_by_id(self):
        """Test case for find_batch_by_id

        Retrieve a Batch
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/batches/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_batches_by_project(self):
        """Test case for find_batches_by_project

        Retrieve all batches by project
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/batches'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
