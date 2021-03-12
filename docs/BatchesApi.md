# OpenapiClient::BatchesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_device_batch**](BatchesApi.md#create_device_batch) | **POST** /projects/{id}/devices/batch | Create a devices batch |
| [**delete_batch**](BatchesApi.md#delete_batch) | **DELETE** /batches/{id} | Delete the Batch |
| [**find_batch_by_id**](BatchesApi.md#find_batch_by_id) | **GET** /batches/{id} | Retrieve a Batch |
| [**find_batches_by_project**](BatchesApi.md#find_batches_by_project) | **GET** /projects/{id}/batches | Retrieve all batches by project |


## create_device_batch

> <BatchesList> create_device_batch(id, batch)

Create a devices batch

Creates new devices in batch and provisions them in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\": \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility `{ \"facility\": \"f1\" }` , or you can instruct to create the device in the best available datacenter `{ \"facility\": \"any\" }`. Additionally it is possible to set a prioritized location selection.  For example `{ \"facility\": [\"f3\", \"f2\", \"any\"] }` will try to assign to the facility f3, if there are no available f2, and so on. If \"any\" is not specified for \"facility\", the request will fail unless it can assign in the selected locations.  With `{ \"facility\": \"any\" }` you have the option to diversify to indicate how many facilities you are willing to be spread across. For this purpose use parameter: `facility_diversity_level = N`.  For example:  `{ \"facilities\": [\"sjc1\", \"ewr1\", \"any\"] ,  \"facility_diversity_level\" = 1, \"quantity\" = 10 }` will assign 10 devices into the same facility, trying first in \"sjc1\", and if there aren’t available, it will try in  \"ewr1\", otherwise any other.  The `ip_addresses` attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": true }, { \"address_family\": 4, \"public\": false }, { \"address_family\": 6, \"public\": true }] }` was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": false }] }`.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, `{ \"ip_addresses\": [..., {\"address_family\": 4, \"public\": true, \"ip_reservations\": [\"uuid1\", \"uuid2\"]}] }`  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy.

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

api_instance = OpenapiClient::BatchesApi.new
id = TODO # String | Project UUID
batch = OpenapiClient::InstancesBatchCreateInput.new # InstancesBatchCreateInput | Batches to create

begin
  # Create a devices batch
  result = api_instance.create_device_batch(id, batch)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->create_device_batch: #{e}"
end
```

#### Using the create_device_batch_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BatchesList>, Integer, Hash)> create_device_batch_with_http_info(id, batch)

```ruby
begin
  # Create a devices batch
  data, status_code, headers = api_instance.create_device_batch_with_http_info(id, batch)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BatchesList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->create_device_batch_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **batch** | [**InstancesBatchCreateInput**](InstancesBatchCreateInput.md) | Batches to create |  |

### Return type

[**BatchesList**](BatchesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_batch

> delete_batch(id, remove_associated_instances)

Delete the Batch

Deletes the Batch.

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

api_instance = OpenapiClient::BatchesApi.new
id = TODO # String | Batch UUID
remove_associated_instances = true # Boolean | Default route

begin
  # Delete the Batch
  api_instance.delete_batch(id, remove_associated_instances)
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->delete_batch: #{e}"
end
```

#### Using the delete_batch_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_batch_with_http_info(id, remove_associated_instances)

```ruby
begin
  # Delete the Batch
  data, status_code, headers = api_instance.delete_batch_with_http_info(id, remove_associated_instances)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->delete_batch_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Batch UUID |  |
| **remove_associated_instances** | **Boolean** | Default route |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## find_batch_by_id

> <Batch> find_batch_by_id(id, opts)

Retrieve a Batch

Returns a Batch

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

api_instance = OpenapiClient::BatchesApi.new
id = TODO # String | Batch UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a Batch
  result = api_instance.find_batch_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->find_batch_by_id: #{e}"
end
```

#### Using the find_batch_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Batch>, Integer, Hash)> find_batch_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a Batch
  data, status_code, headers = api_instance.find_batch_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Batch>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->find_batch_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Batch UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Batch**](Batch.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_batches_by_project

> <BatchesList> find_batches_by_project(id, opts)

Retrieve all batches by project

Returns all batches for the given project

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

api_instance = OpenapiClient::BatchesApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all batches by project
  result = api_instance.find_batches_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->find_batches_by_project: #{e}"
end
```

#### Using the find_batches_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BatchesList>, Integer, Hash)> find_batches_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve all batches by project
  data, status_code, headers = api_instance.find_batches_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BatchesList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BatchesApi->find_batches_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**BatchesList**](BatchesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

