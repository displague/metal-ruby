# OpenapiClient::VolumesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**clone_volume**](VolumesApi.md#clone_volume) | **POST** /storage/{id}/clone | Clone volume/snapshot |
| [**create_volume**](VolumesApi.md#create_volume) | **POST** /projects/{id}/storage | Create a volume |
| [**create_volume_attachment**](VolumesApi.md#create_volume_attachment) | **POST** /storage/{id}/attachments | Attach your volume |
| [**create_volume_snapshot_policy**](VolumesApi.md#create_volume_snapshot_policy) | **POST** /storage/{id}/snapshot-policies | Create a volume snapshot policy |
| [**delete_volume**](VolumesApi.md#delete_volume) | **DELETE** /storage/{id} | Delete the volume |
| [**delete_volume_attachment**](VolumesApi.md#delete_volume_attachment) | **DELETE** /storage/attachments/{id} | Detach volume |
| [**delete_volume_snapshot**](VolumesApi.md#delete_volume_snapshot) | **DELETE** /storage/{volume_id}/snapshots/{id} | Delete volume snapshot |
| [**delete_volume_snapshot_policy**](VolumesApi.md#delete_volume_snapshot_policy) | **DELETE** /storage/snapshot-policies/{id} | Delete the volume snapshot policy |
| [**find_volume_attachment_by_id**](VolumesApi.md#find_volume_attachment_by_id) | **GET** /storage/attachments/{id} | Retrieve an attachment |
| [**find_volume_attachments**](VolumesApi.md#find_volume_attachments) | **GET** /storage/{id}/attachments | Retrieve all volume attachment |
| [**find_volume_by_id**](VolumesApi.md#find_volume_by_id) | **GET** /storage/{id} | Retrieve a volume |
| [**find_volume_customdata**](VolumesApi.md#find_volume_customdata) | **GET** /storage/{id}/customdata | Retrieve the custom metadata of a storage volume |
| [**find_volume_events**](VolumesApi.md#find_volume_events) | **GET** /volumes/{id}/events | Retrieve volume&#39;s events |
| [**find_volume_snapshots**](VolumesApi.md#find_volume_snapshots) | **GET** /storage/{id}/snapshots | Retrieve all volume snapshot |
| [**find_volumes**](VolumesApi.md#find_volumes) | **GET** /projects/{id}/storage | Retrieve all volumes |
| [**restore_volume**](VolumesApi.md#restore_volume) | **POST** /storage/{id}/restore | Restore volume |
| [**update_volume**](VolumesApi.md#update_volume) | **PUT** /storage/{id} | Update the volume |
| [**update_volume_snapshot_policy**](VolumesApi.md#update_volume_snapshot_policy) | **PUT** /storage/snapshot-policies/{id} | Update the volume snapshot policy |


## clone_volume

> <Volume> clone_volume(id, opts)

Clone volume/snapshot

Clone your volume or snapshot into a new volume. To clone the volume, send an empty body. To promote a volume snapshot into a new volume, include the snapshot_timestamp attribute in the request body.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
opts = {
  snapshot_timestamp: 'snapshot_timestamp_example' # String | snapshot timestamp
}

begin
  # Clone volume/snapshot
  result = api_instance.clone_volume(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->clone_volume: #{e}"
end
```

#### Using the clone_volume_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Volume>, Integer, Hash)> clone_volume_with_http_info(id, opts)

```ruby
begin
  # Clone volume/snapshot
  data, status_code, headers = api_instance.clone_volume_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Volume>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->clone_volume_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **snapshot_timestamp** | **String** | snapshot timestamp | [optional] |

### Return type

[**Volume**](Volume.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_volume

> <Volume> create_volume(id, volume)

Create a volume

Creates a new volume in our datacenter. The valid attribute values for `plan` and `facility` are:           \"facility\": \"ams1\", \"ewr1\", \"nrt1\", \"sjc1\"          \"plan\": \"storage_1\" (Standard), \"storage_2\" (Performance)

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Project UUID
volume = OpenapiClient::VolumeCreateInput.new({facility: 'facility_example', plan: 'plan_example', size: 37}) # VolumeCreateInput | Volume to create

begin
  # Create a volume
  result = api_instance.create_volume(id, volume)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->create_volume: #{e}"
end
```

#### Using the create_volume_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Volume>, Integer, Hash)> create_volume_with_http_info(id, volume)

```ruby
begin
  # Create a volume
  data, status_code, headers = api_instance.create_volume_with_http_info(id, volume)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Volume>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->create_volume_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **volume** | [**VolumeCreateInput**](VolumeCreateInput.md) | Volume to create |  |

### Return type

[**Volume**](Volume.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_volume_attachment

> <VolumeAttachment> create_volume_attachment(id, attachment)

Attach your volume

Attach your volume to a device.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
attachment = OpenapiClient::VolumeAttachmentInput.new({device_id: 'device_id_example'}) # VolumeAttachmentInput | Device to attach

begin
  # Attach your volume
  result = api_instance.create_volume_attachment(id, attachment)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->create_volume_attachment: #{e}"
end
```

#### Using the create_volume_attachment_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VolumeAttachment>, Integer, Hash)> create_volume_attachment_with_http_info(id, attachment)

```ruby
begin
  # Attach your volume
  data, status_code, headers = api_instance.create_volume_attachment_with_http_info(id, attachment)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VolumeAttachment>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->create_volume_attachment_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **attachment** | [**VolumeAttachmentInput**](VolumeAttachmentInput.md) | Device to attach |  |

### Return type

[**VolumeAttachment**](VolumeAttachment.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_volume_snapshot_policy

> <SnapshotPolicy> create_volume_snapshot_policy(id, snapshot_frequency, opts)

Create a volume snapshot policy

Creates a new snapshot policy of your volume.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
snapshot_frequency = '1min' # String | Snapshot frequency
opts = {
  snapshot_count: 56 # Integer | Snapshot count
}

begin
  # Create a volume snapshot policy
  result = api_instance.create_volume_snapshot_policy(id, snapshot_frequency, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->create_volume_snapshot_policy: #{e}"
end
```

#### Using the create_volume_snapshot_policy_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SnapshotPolicy>, Integer, Hash)> create_volume_snapshot_policy_with_http_info(id, snapshot_frequency, opts)

```ruby
begin
  # Create a volume snapshot policy
  data, status_code, headers = api_instance.create_volume_snapshot_policy_with_http_info(id, snapshot_frequency, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SnapshotPolicy>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->create_volume_snapshot_policy_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **snapshot_frequency** | **String** | Snapshot frequency |  |
| **snapshot_count** | **Integer** | Snapshot count | [optional] |

### Return type

[**SnapshotPolicy**](SnapshotPolicy.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delete_volume

> delete_volume(id)

Delete the volume

Deletes the volume.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID

begin
  # Delete the volume
  api_instance.delete_volume(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume: #{e}"
end
```

#### Using the delete_volume_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_volume_with_http_info(id)

```ruby
begin
  # Delete the volume
  data, status_code, headers = api_instance.delete_volume_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete_volume_attachment

> delete_volume_attachment(id)

Detach volume

Detach volume.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Attachment UUID

begin
  # Detach volume
  api_instance.delete_volume_attachment(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_attachment: #{e}"
end
```

#### Using the delete_volume_attachment_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_volume_attachment_with_http_info(id)

```ruby
begin
  # Detach volume
  data, status_code, headers = api_instance.delete_volume_attachment_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_attachment_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Attachment UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete_volume_snapshot

> delete_volume_snapshot(volume_id, id)

Delete volume snapshot

Delete volume snapshot.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
volume_id = TODO # String | Volume UUID
id = TODO # String | Snapshot UUID

begin
  # Delete volume snapshot
  api_instance.delete_volume_snapshot(volume_id, id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_snapshot: #{e}"
end
```

#### Using the delete_volume_snapshot_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_volume_snapshot_with_http_info(volume_id, id)

```ruby
begin
  # Delete volume snapshot
  data, status_code, headers = api_instance.delete_volume_snapshot_with_http_info(volume_id, id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_snapshot_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **volume_id** | [**String**](.md) | Volume UUID |  |
| **id** | [**String**](.md) | Snapshot UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## delete_volume_snapshot_policy

> delete_volume_snapshot_policy(id)

Delete the volume snapshot policy

Deletes the volume snapshot policy.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Snapshot Policy UUID

begin
  # Delete the volume snapshot policy
  api_instance.delete_volume_snapshot_policy(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_snapshot_policy: #{e}"
end
```

#### Using the delete_volume_snapshot_policy_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_volume_snapshot_policy_with_http_info(id)

```ruby
begin
  # Delete the volume snapshot policy
  data, status_code, headers = api_instance.delete_volume_snapshot_policy_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->delete_volume_snapshot_policy_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Snapshot Policy UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_volume_attachment_by_id

> <VolumeAttachment> find_volume_attachment_by_id(id, opts)

Retrieve an attachment

Returns a single attachment if the user has access

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Attachment UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve an attachment
  result = api_instance.find_volume_attachment_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_attachment_by_id: #{e}"
end
```

#### Using the find_volume_attachment_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VolumeAttachment>, Integer, Hash)> find_volume_attachment_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve an attachment
  data, status_code, headers = api_instance.find_volume_attachment_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VolumeAttachment>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_attachment_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Attachment UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**VolumeAttachment**](VolumeAttachment.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_volume_attachments

> <VolumeAttachmentList> find_volume_attachments(id, opts)

Retrieve all volume attachment

Returns a list of the current volume’s attachments.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all volume attachment
  result = api_instance.find_volume_attachments(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_attachments: #{e}"
end
```

#### Using the find_volume_attachments_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VolumeAttachmentList>, Integer, Hash)> find_volume_attachments_with_http_info(id, opts)

```ruby
begin
  # Retrieve all volume attachment
  data, status_code, headers = api_instance.find_volume_attachments_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VolumeAttachmentList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_attachments_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**VolumeAttachmentList**](VolumeAttachmentList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_volume_by_id

> <Volume> find_volume_by_id(id, opts)

Retrieve a volume

Returns a single volume if the user has access

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a volume
  result = api_instance.find_volume_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_by_id: #{e}"
end
```

#### Using the find_volume_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Volume>, Integer, Hash)> find_volume_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a volume
  data, status_code, headers = api_instance.find_volume_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Volume>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Volume**](Volume.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_volume_customdata

> find_volume_customdata(id)

Retrieve the custom metadata of a storage volume

Provides the custom metadata stored for this storage volume in json format

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Storage Volume UUID

begin
  # Retrieve the custom metadata of a storage volume
  api_instance.find_volume_customdata(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_customdata: #{e}"
end
```

#### Using the find_volume_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_volume_customdata_with_http_info(id)

```ruby
begin
  # Retrieve the custom metadata of a storage volume
  data, status_code, headers = api_instance.find_volume_customdata_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Storage Volume UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_volume_events

> <EventList> find_volume_events(id, opts)

Retrieve volume's events

Returns a list of the current volume’s events

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve volume's events
  result = api_instance.find_volume_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_events: #{e}"
end
```

#### Using the find_volume_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_volume_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve volume's events
  data, status_code, headers = api_instance.find_volume_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**EventList**](EventList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_volume_snapshots

> <VolumeSnapshotList> find_volume_snapshots(id, opts)

Retrieve all volume snapshot

Returns a list of the current volume’s snapshots. To create Volume Snapshots, please check the Volume Snapshot Policies feature.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all volume snapshot
  result = api_instance.find_volume_snapshots(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_snapshots: #{e}"
end
```

#### Using the find_volume_snapshots_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VolumeSnapshotList>, Integer, Hash)> find_volume_snapshots_with_http_info(id, opts)

```ruby
begin
  # Retrieve all volume snapshot
  data, status_code, headers = api_instance.find_volume_snapshots_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VolumeSnapshotList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volume_snapshots_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**VolumeSnapshotList**](VolumeSnapshotList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_volumes

> <VolumeList> find_volumes(id, opts)

Retrieve all volumes

Returns a list of the current projects’s volumes.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all volumes
  result = api_instance.find_volumes(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volumes: #{e}"
end
```

#### Using the find_volumes_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VolumeList>, Integer, Hash)> find_volumes_with_http_info(id, opts)

```ruby
begin
  # Retrieve all volumes
  data, status_code, headers = api_instance.find_volumes_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VolumeList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->find_volumes_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**VolumeList**](VolumeList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## restore_volume

> <Volume> restore_volume(id, restore_point)

Restore volume

Restore the volume to the given snapshot.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
restore_point = 'restore_point_example' # String | restore point

begin
  # Restore volume
  result = api_instance.restore_volume(id, restore_point)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->restore_volume: #{e}"
end
```

#### Using the restore_volume_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Volume>, Integer, Hash)> restore_volume_with_http_info(id, restore_point)

```ruby
begin
  # Restore volume
  data, status_code, headers = api_instance.restore_volume_with_http_info(id, restore_point)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Volume>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->restore_volume_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **restore_point** | **String** | restore point |  |

### Return type

[**Volume**](Volume.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_volume

> <Volume> update_volume(id, volume)

Update the volume

Updates the volume.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Volume UUID
volume = OpenapiClient::VolumeUpdateInput.new # VolumeUpdateInput | Volume to update

begin
  # Update the volume
  result = api_instance.update_volume(id, volume)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->update_volume: #{e}"
end
```

#### Using the update_volume_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Volume>, Integer, Hash)> update_volume_with_http_info(id, volume)

```ruby
begin
  # Update the volume
  data, status_code, headers = api_instance.update_volume_with_http_info(id, volume)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Volume>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->update_volume_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
| **volume** | [**VolumeUpdateInput**](VolumeUpdateInput.md) | Volume to update |  |

### Return type

[**Volume**](Volume.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## update_volume_snapshot_policy

> <SnapshotPolicy> update_volume_snapshot_policy(id, snapshot_frequency, opts)

Update the volume snapshot policy

Updates the volume snapshot policy.

### Examples

```ruby
require 'time'
require 'openapi_client'
# setup authorization
OpenapiClient.configure do |config|
  # Configure API key authorization: x_auth_token
  config.api_key['x_auth_token'] = 'YOUR API KEY'
  # Uncomment the following line to set a prefix for the API key, e.g. 'Bearer' (defaults to nil)
  # config.api_key_prefix['x_auth_token'] = 'Bearer'
end

api_instance = OpenapiClient::VolumesApi.new
id = TODO # String | Snapshot Policy UUID
snapshot_frequency = '1min' # String | Snapshot frequency
opts = {
  snapshot_count: 56 # Integer | Snapshot count
}

begin
  # Update the volume snapshot policy
  result = api_instance.update_volume_snapshot_policy(id, snapshot_frequency, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->update_volume_snapshot_policy: #{e}"
end
```

#### Using the update_volume_snapshot_policy_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SnapshotPolicy>, Integer, Hash)> update_volume_snapshot_policy_with_http_info(id, snapshot_frequency, opts)

```ruby
begin
  # Update the volume snapshot policy
  data, status_code, headers = api_instance.update_volume_snapshot_policy_with_http_info(id, snapshot_frequency, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SnapshotPolicy>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VolumesApi->update_volume_snapshot_policy_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Snapshot Policy UUID |  |
| **snapshot_frequency** | **String** | Snapshot frequency |  |
| **snapshot_count** | **Integer** | Snapshot count | [optional] |

### Return type

[**SnapshotPolicy**](SnapshotPolicy.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

