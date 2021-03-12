# OpenapiClient::DevicesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_bgp_session**](DevicesApi.md#create_bgp_session) | **POST** /devices/{id}/bgp/sessions | Create a BGP session |
| [**create_device**](DevicesApi.md#create_device) | **POST** /projects/{id}/devices | Create a device |
| [**create_device_batch**](DevicesApi.md#create_device_batch) | **POST** /projects/{id}/devices/batch | Create a devices batch |
| [**create_ip_assignment**](DevicesApi.md#create_ip_assignment) | **POST** /devices/{id}/ips | Create a ip assignment |
| [**delete_device**](DevicesApi.md#delete_device) | **DELETE** /devices/{id} | Delete the device |
| [**find_bgp_sessions**](DevicesApi.md#find_bgp_sessions) | **GET** /devices/{id}/bgp/sessions | Retrieve all BGP sessions |
| [**find_device_by_id**](DevicesApi.md#find_device_by_id) | **GET** /devices/{id} | Retrieve a device |
| [**find_device_customdata**](DevicesApi.md#find_device_customdata) | **GET** /devices/{id}/customdata | Retrieve the custom metadata of an instance |
| [**find_device_events**](DevicesApi.md#find_device_events) | **GET** /devices/{id}/events | Retrieve device&#39;s events |
| [**find_device_usages**](DevicesApi.md#find_device_usages) | **GET** /devices/{id}/usages | Retrieve all usages for device |
| [**find_instance_bandwidth**](DevicesApi.md#find_instance_bandwidth) | **GET** /devices/{id}/bandwidth | Retrieve an instance bandwidth |
| [**find_ip_assignment_customdata**](DevicesApi.md#find_ip_assignment_customdata) | **GET** /devices/{instance_id}/ips/{id}/customdata | Retrieve the custom metadata of an IP Assignment |
| [**find_ip_assignments**](DevicesApi.md#find_ip_assignments) | **GET** /devices/{id}/ips | Retrieve all ip assignments |
| [**find_organization_devices**](DevicesApi.md#find_organization_devices) | **GET** /organizations/{id}/devices | Retrieve all devices of an organization |
| [**find_project_devices**](DevicesApi.md#find_project_devices) | **GET** /projects/{id}/devices | Retrieve all devices of a project |
| [**find_project_usage**](DevicesApi.md#find_project_usage) | **GET** /projects/{id}/usages | Retrieve all usages for project |
| [**find_traffic**](DevicesApi.md#find_traffic) | **GET** /devices/{id}/traffic | Retrieve device traffic |
| [**get_bgp_neighbor_data**](DevicesApi.md#get_bgp_neighbor_data) | **GET** /devices/{id}/bgp/neighbors | Retrieve BGP neighbor data for this device |
| [**perform_action**](DevicesApi.md#perform_action) | **POST** /devices/{id}/actions | Perform an action |
| [**update_device**](DevicesApi.md#update_device) | **PUT** /devices/{id} | Update the device |


## create_bgp_session

> <BgpSession> create_bgp_session(id, bgp_session)

Create a BGP session

Creates a BGP session.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
bgp_session = OpenapiClient::BGPSessionInput.new # BGPSessionInput | BGP session to create

begin
  # Create a BGP session
  result = api_instance.create_bgp_session(id, bgp_session)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_bgp_session: #{e}"
end
```

#### Using the create_bgp_session_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSession>, Integer, Hash)> create_bgp_session_with_http_info(id, bgp_session)

```ruby
begin
  # Create a BGP session
  data, status_code, headers = api_instance.create_bgp_session_with_http_info(id, bgp_session)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSession>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_bgp_session_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **bgp_session** | [**BGPSessionInput**](BGPSessionInput.md) | BGP session to create |  |

### Return type

[**BgpSession**](BgpSession.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_device

> <Device> create_device(id, device)

Create a device

Creates a new device and provisions it in our datacenter.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have.  For example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\": \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.  The facilities attribute specifies in what datacenter you wish to create the device.  You can either specify a single facility `{ \"facility\": \"f1\" }` , or you can instruct to create the device in the best available datacenter `{ \"facility\": \"any\" }`. Additionally it is possible to set a prioritized location selection.  For example `{ \"facility\": [\"f3\", \"f2\", \"any\"] }` will try to assign to the facility f3, if there are no available f2, and so on. If \"any\" is not specified for \"facility\", the request will fail unless it can assign in the selected locations.  The `ip_addresses attribute will allow you to specify the addresses you want created with your device.  To maintain backwards compatibility, If the attribute is not sent in the request, it will be treated as if `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": true }, { \"address_family\": 4, \"public\": false }, { \"address_family\": 6, \"public\": true }] }` was sent.  The private IPv4 address is required and always need to be sent in the array. Not all operating systems support no public IPv4 address, so in those cases you will receive an error message.  For example, to only configure your server with a private IPv4 address, you can send `{ \"ip_addresses\": [{ \"address_family\": 4, \"public\": false }] }`.  Note: when specifying a subnet size larger than a /30, you will need to supply the UUID(s) of existing ip_reservations in your project to assign IPs from.  For example, `{ \"ip_addresses\": [..., {\"address_family\": 4, \"public\": true, \"ip_reservations\": [\"uuid1\", \"uuid2\"]}] }`  To access a server without public IPs, you can use our Out-of-Band console access (SOS) or use another server with public IPs as a proxy. 

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Project UUID
device = OpenapiClient::DeviceCreateInput.new({facility: 'facility_example', plan: 'plan_example', operating_system: 'operating_system_example'}) # DeviceCreateInput | Device to create

begin
  # Create a device
  result = api_instance.create_device(id, device)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_device: #{e}"
end
```

#### Using the create_device_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Device>, Integer, Hash)> create_device_with_http_info(id, device)

```ruby
begin
  # Create a device
  data, status_code, headers = api_instance.create_device_with_http_info(id, device)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Device>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_device_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **device** | [**DeviceCreateInput**](DeviceCreateInput.md) | Device to create |  |

### Return type

[**Device**](Device.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Project UUID
batch = OpenapiClient::InstancesBatchCreateInput.new # InstancesBatchCreateInput | Batches to create

begin
  # Create a devices batch
  result = api_instance.create_device_batch(id, batch)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_device_batch: #{e}"
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
  puts "Error when calling DevicesApi->create_device_batch_with_http_info: #{e}"
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


## create_ip_assignment

> <IPAssignment> create_ip_assignment(id, ip_assignment)

Create a ip assignment

Creates an ip assignment for a device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
ip_assignment = OpenapiClient::IPAssignmentInput.new({address: 'address_example'}) # IPAssignmentInput | IPAssignment to create

begin
  # Create a ip assignment
  result = api_instance.create_ip_assignment(id, ip_assignment)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_ip_assignment: #{e}"
end
```

#### Using the create_ip_assignment_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPAssignment>, Integer, Hash)> create_ip_assignment_with_http_info(id, ip_assignment)

```ruby
begin
  # Create a ip assignment
  data, status_code, headers = api_instance.create_ip_assignment_with_http_info(id, ip_assignment)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPAssignment>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->create_ip_assignment_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **ip_assignment** | [**IPAssignmentInput**](IPAssignmentInput.md) | IPAssignment to create |  |

### Return type

[**IPAssignment**](IPAssignment.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_device

> delete_device(id, opts)

Delete the device

Deletes a device and deprovisions it in our datacenter.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
opts = {
  force_delete: true # Boolean | Force the deletion of the device, by detaching any storage volume still active.
}

begin
  # Delete the device
  api_instance.delete_device(id, opts)
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->delete_device: #{e}"
end
```

#### Using the delete_device_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_device_with_http_info(id, opts)

```ruby
begin
  # Delete the device
  data, status_code, headers = api_instance.delete_device_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->delete_device_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **force_delete** | **Boolean** | Force the deletion of the device, by detaching any storage volume still active. | [optional] |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_bgp_sessions

> <BgpSessionList> find_bgp_sessions(id)

Retrieve all BGP sessions

Provides a listing of available BGP sessions for the device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID

begin
  # Retrieve all BGP sessions
  result = api_instance.find_bgp_sessions(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_bgp_sessions: #{e}"
end
```

#### Using the find_bgp_sessions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSessionList>, Integer, Hash)> find_bgp_sessions_with_http_info(id)

```ruby
begin
  # Retrieve all BGP sessions
  data, status_code, headers = api_instance.find_bgp_sessions_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSessionList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_bgp_sessions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |

### Return type

[**BgpSessionList**](BgpSessionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_device_by_id

> <Device> find_device_by_id(id, opts)

Retrieve a device

Type-specific options (such as facility for baremetal devices) will be included as part of the main data structure.                          State value can be one of: active inactive queued or provisioning

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a device
  result = api_instance.find_device_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_by_id: #{e}"
end
```

#### Using the find_device_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Device>, Integer, Hash)> find_device_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a device
  data, status_code, headers = api_instance.find_device_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Device>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Device**](Device.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_device_customdata

> find_device_customdata(id)

Retrieve the custom metadata of an instance

Provides the custom metadata stored for this instance in json format

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Instance UUID

begin
  # Retrieve the custom metadata of an instance
  api_instance.find_device_customdata(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_customdata: #{e}"
end
```

#### Using the find_device_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_device_customdata_with_http_info(id)

```ruby
begin
  # Retrieve the custom metadata of an instance
  data, status_code, headers = api_instance.find_device_customdata_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Instance UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_device_events

> <EventList> find_device_events(id, opts)

Retrieve device's events

Returns a list of events pertaining to a specific device

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve device's events
  result = api_instance.find_device_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_events: #{e}"
end
```

#### Using the find_device_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_device_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve device's events
  data, status_code, headers = api_instance.find_device_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
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


## find_device_usages

> <DeviceUsageList> find_device_usages(id, opts)

Retrieve all usages for device

Returns all usages for a device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
opts = {
  created_after: 'created_after_example', # String | Filter usages created after this date
  created_before: 'created_before_example' # String | Filter usages created before this date
}

begin
  # Retrieve all usages for device
  result = api_instance.find_device_usages(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_usages: #{e}"
end
```

#### Using the find_device_usages_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeviceUsageList>, Integer, Hash)> find_device_usages_with_http_info(id, opts)

```ruby
begin
  # Retrieve all usages for device
  data, status_code, headers = api_instance.find_device_usages_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeviceUsageList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_device_usages_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **created_after** | **String** | Filter usages created after this date | [optional] |
| **created_before** | **String** | Filter usages created before this date | [optional] |

### Return type

[**DeviceUsageList**](DeviceUsageList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_instance_bandwidth

> find_instance_bandwidth(id, from, _until)

Retrieve an instance bandwidth

Retrieve an instance bandwidth for a given period of time.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
from = 'from_example' # String | Timestamp from range
_until = '_until_example' # String | Timestamp to range

begin
  # Retrieve an instance bandwidth
  api_instance.find_instance_bandwidth(id, from, _until)
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_instance_bandwidth: #{e}"
end
```

#### Using the find_instance_bandwidth_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_instance_bandwidth_with_http_info(id, from, _until)

```ruby
begin
  # Retrieve an instance bandwidth
  data, status_code, headers = api_instance.find_instance_bandwidth_with_http_info(id, from, _until)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_instance_bandwidth_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **from** | **String** | Timestamp from range |  |
| **_until** | **String** | Timestamp to range |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_ip_assignment_customdata

> find_ip_assignment_customdata(instance_id, id)

Retrieve the custom metadata of an IP Assignment

Provides the custom metadata stored for this IP Assignment in json format

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

api_instance = OpenapiClient::DevicesApi.new
instance_id = TODO # String | Instance UUID
id = TODO # String | Ip Assignment UUID

begin
  # Retrieve the custom metadata of an IP Assignment
  api_instance.find_ip_assignment_customdata(instance_id, id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_ip_assignment_customdata: #{e}"
end
```

#### Using the find_ip_assignment_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_ip_assignment_customdata_with_http_info(instance_id, id)

```ruby
begin
  # Retrieve the custom metadata of an IP Assignment
  data, status_code, headers = api_instance.find_ip_assignment_customdata_with_http_info(instance_id, id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_ip_assignment_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **instance_id** | [**String**](.md) | Instance UUID |  |
| **id** | [**String**](.md) | Ip Assignment UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_ip_assignments

> <IPAssignmentList> find_ip_assignments(id, opts)

Retrieve all ip assignments

Returns all ip assignments for a device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all ip assignments
  result = api_instance.find_ip_assignments(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_ip_assignments: #{e}"
end
```

#### Using the find_ip_assignments_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPAssignmentList>, Integer, Hash)> find_ip_assignments_with_http_info(id, opts)

```ruby
begin
  # Retrieve all ip assignments
  data, status_code, headers = api_instance.find_ip_assignments_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPAssignmentList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_ip_assignments_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**IPAssignmentList**](IPAssignmentList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organization_devices

> <DeviceList> find_organization_devices(id, opts)

Retrieve all devices of an organization

Provides a collection of devices for a given organization.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all devices of an organization
  result = api_instance.find_organization_devices(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_organization_devices: #{e}"
end
```

#### Using the find_organization_devices_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeviceList>, Integer, Hash)> find_organization_devices_with_http_info(id, opts)

```ruby
begin
  # Retrieve all devices of an organization
  data, status_code, headers = api_instance.find_organization_devices_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeviceList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_organization_devices_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**DeviceList**](DeviceList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_devices

> <DeviceList> find_project_devices(id, opts)

Retrieve all devices of a project

Provides a collection of devices for a given project.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all devices of a project
  result = api_instance.find_project_devices(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_project_devices: #{e}"
end
```

#### Using the find_project_devices_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeviceList>, Integer, Hash)> find_project_devices_with_http_info(id, opts)

```ruby
begin
  # Retrieve all devices of a project
  data, status_code, headers = api_instance.find_project_devices_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeviceList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_project_devices_with_http_info: #{e}"
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

[**DeviceList**](DeviceList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_usage

> <ProjectUsageList> find_project_usage(id, opts)

Retrieve all usages for project

Returns all usages for a project.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Project UUID
opts = {
  created_after: 'created_after_example', # String | Filter usages created after this date
  created_before: 'created_before_example' # String | Filter usages created before this date
}

begin
  # Retrieve all usages for project
  result = api_instance.find_project_usage(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_project_usage: #{e}"
end
```

#### Using the find_project_usage_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectUsageList>, Integer, Hash)> find_project_usage_with_http_info(id, opts)

```ruby
begin
  # Retrieve all usages for project
  data, status_code, headers = api_instance.find_project_usage_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectUsageList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_project_usage_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **created_after** | **String** | Filter usages created after this date | [optional] |
| **created_before** | **String** | Filter usages created before this date | [optional] |

### Return type

[**ProjectUsageList**](ProjectUsageList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_traffic

> find_traffic(id, direction, timeframe, opts)

Retrieve device traffic

Returns traffic for a specific device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
direction = 'inbound' # String | Traffic direction
timeframe = OpenapiClient::Timeframe.new({started_at: Time.now, ended_at: Time.now}) # Timeframe | Traffic timeframe
opts = {
  interval: 'minute', # String | Traffic interval
  bucket: 'internal' # String | Traffic bucket
}

begin
  # Retrieve device traffic
  api_instance.find_traffic(id, direction, timeframe, opts)
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_traffic: #{e}"
end
```

#### Using the find_traffic_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_traffic_with_http_info(id, direction, timeframe, opts)

```ruby
begin
  # Retrieve device traffic
  data, status_code, headers = api_instance.find_traffic_with_http_info(id, direction, timeframe, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->find_traffic_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **direction** | **String** | Traffic direction |  |
| **timeframe** | [**Timeframe**](Timeframe.md) | Traffic timeframe |  |
| **interval** | **String** | Traffic interval | [optional] |
| **bucket** | **String** | Traffic bucket | [optional] |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## get_bgp_neighbor_data

> <BgpSessionNeighbors> get_bgp_neighbor_data(id)

Retrieve BGP neighbor data for this device

Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID

begin
  # Retrieve BGP neighbor data for this device
  result = api_instance.get_bgp_neighbor_data(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->get_bgp_neighbor_data: #{e}"
end
```

#### Using the get_bgp_neighbor_data_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSessionNeighbors>, Integer, Hash)> get_bgp_neighbor_data_with_http_info(id)

```ruby
begin
  # Retrieve BGP neighbor data for this device
  data, status_code, headers = api_instance.get_bgp_neighbor_data_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSessionNeighbors>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->get_bgp_neighbor_data_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |

### Return type

[**BgpSessionNeighbors**](BgpSessionNeighbors.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## perform_action

> perform_action(id, type)

Perform an action

Performs an action for the given device.  Possible actions include: power_on, power_off, reboot, reinstall, and rescue (reboot the device into rescue OS.)

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
type = 'power_on' # String | Action to perform

begin
  # Perform an action
  api_instance.perform_action(id, type)
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->perform_action: #{e}"
end
```

#### Using the perform_action_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> perform_action_with_http_info(id, type)

```ruby
begin
  # Perform an action
  data, status_code, headers = api_instance.perform_action_with_http_info(id, type)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->perform_action_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **type** | **String** | Action to perform |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## update_device

> <Device> update_device(id, device)

Update the device

Updates the device.

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

api_instance = OpenapiClient::DevicesApi.new
id = TODO # String | Device UUID
device = OpenapiClient::DeviceUpdateInput.new # DeviceUpdateInput | Facility to update

begin
  # Update the device
  result = api_instance.update_device(id, device)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->update_device: #{e}"
end
```

#### Using the update_device_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Device>, Integer, Hash)> update_device_with_http_info(id, device)

```ruby
begin
  # Update the device
  data, status_code, headers = api_instance.update_device_with_http_info(id, device)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Device>
rescue OpenapiClient::ApiError => e
  puts "Error when calling DevicesApi->update_device_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **device** | [**DeviceUpdateInput**](DeviceUpdateInput.md) | Facility to update |  |

### Return type

[**Device**](Device.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

