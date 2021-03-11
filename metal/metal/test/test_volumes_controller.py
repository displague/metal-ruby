# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from metal.types.event_list import EventList  # noqa: E501
from metal.types.snapshot_policy import SnapshotPolicy  # noqa: E501
from metal.types.volume import Volume  # noqa: E501
from metal.types.volume_attachment import VolumeAttachment  # noqa: E501
from metal.types.volume_attachment_input import VolumeAttachmentInput  # noqa: E501
from metal.types.volume_attachment_list import VolumeAttachmentList  # noqa: E501
from metal.types.volume_create_input import VolumeCreateInput  # noqa: E501
from metal.types.volume_list import VolumeList  # noqa: E501
from metal.types.volume_snapshot_list import VolumeSnapshotList  # noqa: E501
from metal.types.volume_update_input import VolumeUpdateInput  # noqa: E501
from metal.test import BaseTestCase


class TestVolumesController(BaseTestCase):
    """VolumesController integration test stubs"""

    def test_clone_volume(self):
        """Test case for clone_volume

        Clone volume/snapshot
        """
        query_string = [('snapshot_timestamp', 'snapshot_timestamp_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/clone'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_volume(self):
        """Test case for create_volume

        Create a volume
        """
        volume = {
  "size" : 0,
  "snapshot_policies" : {
    "snapshot_frequency" : "snapshot_frequency",
    "snapshot_count" : 6
  },
  "description" : "description",
  "billing_cycle" : "billing_cycle",
  "customdata" : "{}",
  "locked" : true,
  "facility" : "facility",
  "plan" : "plan"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/projects/{id}/storage'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(volume),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_volume_attachment(self):
        """Test case for create_volume_attachment

        Attach your volume
        """
        attachment = {
  "device_id" : "046b6c7f-0b8a-43b9-b35d-6489e6daee91"
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/attachments'.format(id='id_example'),
            method='POST',
            headers=headers,
            data=json.dumps(attachment),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_create_volume_snapshot_policy(self):
        """Test case for create_volume_snapshot_policy

        Create a volume snapshot policy
        """
        query_string = [('snapshot_count', 56),
                        ('snapshot_frequency', 'snapshot_frequency_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/snapshot-policies'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_volume(self):
        """Test case for delete_volume

        Delete the volume
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_volume_attachment(self):
        """Test case for delete_volume_attachment

        Detach volume
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/attachments/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_volume_snapshot(self):
        """Test case for delete_volume_snapshot

        Delete volume snapshot
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{volume_id}/snapshots/{id}'.format(volume_id='volume_id_example', id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_volume_snapshot_policy(self):
        """Test case for delete_volume_snapshot_policy

        Delete the volume snapshot policy
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/snapshot-policies/{id}'.format(id='id_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volume_attachment_by_id(self):
        """Test case for find_volume_attachment_by_id

        Retrieve an attachment
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/attachments/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volume_attachments(self):
        """Test case for find_volume_attachments

        Retrieve all volume attachment
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/attachments'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volume_by_id(self):
        """Test case for find_volume_by_id

        Retrieve a volume
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volume_customdata(self):
        """Test case for find_volume_customdata

        Retrieve the custom metadata of a storage volume
        """
        headers = { 
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/customdata'.format(id='id_example'),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volume_events(self):
        """Test case for find_volume_events

        Retrieve volume's events
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
            '/metal/v1/volumes/{id}/events'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volume_snapshots(self):
        """Test case for find_volume_snapshots

        Retrieve all volume snapshot
        """
        query_string = [('include', ['include_example']),
                        ('exclude', ['exclude_example'])]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/snapshots'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_find_volumes(self):
        """Test case for find_volumes

        Retrieve all volumes
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
            '/metal/v1/projects/{id}/storage'.format(id='id_example'),
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_restore_volume(self):
        """Test case for restore_volume

        Restore volume
        """
        query_string = [('restore_point', 'restore_point_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}/restore'.format(id='id_example'),
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_volume(self):
        """Test case for update_volume

        Update the volume
        """
        volume = {
  "size" : 0,
  "description" : "description",
  "billing_cycle" : "billing_cycle",
  "customdata" : "{}",
  "locked" : true
}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            data=json.dumps(volume),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_volume_snapshot_policy(self):
        """Test case for update_volume_snapshot_policy

        Update the volume snapshot policy
        """
        query_string = [('snapshot_count', 56),
                        ('snapshot_frequency', 'snapshot_frequency_example')]
        headers = { 
            'Accept': 'application/json',
            'x_auth_token': 'special-key',
        }
        response = self.client.open(
            '/metal/v1/storage/snapshot-policies/{id}'.format(id='id_example'),
            method='PUT',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
