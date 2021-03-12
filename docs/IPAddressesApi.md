# OpenapiClient::IPAddressesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_ip_assignment**](IPAddressesApi.md#create_ip_assignment) | **POST** /devices/{id}/ips | Create a ip assignment |
| [**delete_ip_address**](IPAddressesApi.md#delete_ip_address) | **DELETE** /ips/{id} | Unassign an ip address |
| [**find_ip_address_by_id**](IPAddressesApi.md#find_ip_address_by_id) | **GET** /ips/{id} | Retrieve an ip address |
| [**find_ip_address_customdata**](IPAddressesApi.md#find_ip_address_customdata) | **GET** /ips/{id}/customdata | Retrieve the custom metadata of an IP Reservation or IP Assignment |
| [**find_ip_assignments**](IPAddressesApi.md#find_ip_assignments) | **GET** /devices/{id}/ips | Retrieve all ip assignments |
| [**find_ip_availabilities**](IPAddressesApi.md#find_ip_availabilities) | **GET** /ips/{id}/available | Retrieve all available subnets of a particular reservation |
| [**find_ip_reservations**](IPAddressesApi.md#find_ip_reservations) | **GET** /projects/{id}/ips | Retrieve all ip reservations |
| [**request_ip_reservation**](IPAddressesApi.md#request_ip_reservation) | **POST** /projects/{id}/ips | Requesting IP reservations |


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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | Device UUID
ip_assignment = OpenapiClient::IPAssignmentInput.new({address: 'address_example'}) # IPAssignmentInput | IPAssignment to create

begin
  # Create a ip assignment
  result = api_instance.create_ip_assignment(id, ip_assignment)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->create_ip_assignment: #{e}"
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
  puts "Error when calling IPAddressesApi->create_ip_assignment_with_http_info: #{e}"
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


## delete_ip_address

> delete_ip_address(id)

Unassign an ip address

Note! This call can be used to un-assign an IP assignment or delete an IP reservation. Un-assign an IP address record. Use the assignment UUID you get after attaching the IP. This will remove the relationship between an IP and the device and will make the IP address available to be assigned to another device. Delete and IP reservation. Use the reservation UUID you get after adding the IP to the project. This will permanently delete the IP block reservation from the project.

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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | IP Address UUID

begin
  # Unassign an ip address
  api_instance.delete_ip_address(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->delete_ip_address: #{e}"
end
```

#### Using the delete_ip_address_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_ip_address_with_http_info(id)

```ruby
begin
  # Unassign an ip address
  data, status_code, headers = api_instance.delete_ip_address_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->delete_ip_address_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | IP Address UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_ip_address_by_id

> <IPAssignment> find_ip_address_by_id(id, opts)

Retrieve an ip address

Returns a single ip address if the user has access.

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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | IP Address UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve an ip address
  result = api_instance.find_ip_address_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_address_by_id: #{e}"
end
```

#### Using the find_ip_address_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPAssignment>, Integer, Hash)> find_ip_address_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve an ip address
  data, status_code, headers = api_instance.find_ip_address_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPAssignment>
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_address_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | IP Address UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**IPAssignment**](IPAssignment.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_ip_address_customdata

> find_ip_address_customdata(id)

Retrieve the custom metadata of an IP Reservation or IP Assignment

Provides the custom metadata stored for this IP Reservation or IP Assignment in json format

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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | Ip Reservation UUID

begin
  # Retrieve the custom metadata of an IP Reservation or IP Assignment
  api_instance.find_ip_address_customdata(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_address_customdata: #{e}"
end
```

#### Using the find_ip_address_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_ip_address_customdata_with_http_info(id)

```ruby
begin
  # Retrieve the custom metadata of an IP Reservation or IP Assignment
  data, status_code, headers = api_instance.find_ip_address_customdata_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_address_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Ip Reservation UUID |  |

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

api_instance = OpenapiClient::IPAddressesApi.new
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
  puts "Error when calling IPAddressesApi->find_ip_assignments: #{e}"
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
  puts "Error when calling IPAddressesApi->find_ip_assignments_with_http_info: #{e}"
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


## find_ip_availabilities

> <IPAvailabilitiesList> find_ip_availabilities(id, cidr)

Retrieve all available subnets of a particular reservation

Provides a list of IP resevations for a single project.

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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | IP Reservation UUID
cidr = '20' # String | Size of subnets in bits

begin
  # Retrieve all available subnets of a particular reservation
  result = api_instance.find_ip_availabilities(id, cidr)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_availabilities: #{e}"
end
```

#### Using the find_ip_availabilities_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPAvailabilitiesList>, Integer, Hash)> find_ip_availabilities_with_http_info(id, cidr)

```ruby
begin
  # Retrieve all available subnets of a particular reservation
  data, status_code, headers = api_instance.find_ip_availabilities_with_http_info(id, cidr)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPAvailabilitiesList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_availabilities_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | IP Reservation UUID |  |
| **cidr** | **String** | Size of subnets in bits |  |

### Return type

[**IPAvailabilitiesList**](IPAvailabilitiesList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_ip_reservations

> <IPReservationList> find_ip_reservations(id, opts)

Retrieve all ip reservations

Provides a list of IP resevations for a single project.

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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all ip reservations
  result = api_instance.find_ip_reservations(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_reservations: #{e}"
end
```

#### Using the find_ip_reservations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPReservationList>, Integer, Hash)> find_ip_reservations_with_http_info(id, opts)

```ruby
begin
  # Retrieve all ip reservations
  data, status_code, headers = api_instance.find_ip_reservations_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPReservationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->find_ip_reservations_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**IPReservationList**](IPReservationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request_ip_reservation

> <IPReservation> request_ip_reservation(id, ip_reservation_request)

Requesting IP reservations

Request more IP space for a project in order to have additional IP addresses to assign to devices.  If the request is within the max quota, an IP reservation will be created. If the project will exceed its IP quota, a request will be submitted for review, and will return an IP Reservation with a `state` of `pending`. You can automatically have the request fail with HTTP status 422 instead of triggering the review process by providing the `fail_on_approval_required` parameter set to `true` in the request.

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

api_instance = OpenapiClient::IPAddressesApi.new
id = TODO # String | Project UUID
ip_reservation_request = OpenapiClient::IPReservationRequestInput.new({type: 'type_example', quantity: 37}) # IPReservationRequestInput | IP Reservation Request to create

begin
  # Requesting IP reservations
  result = api_instance.request_ip_reservation(id, ip_reservation_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->request_ip_reservation: #{e}"
end
```

#### Using the request_ip_reservation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<IPReservation>, Integer, Hash)> request_ip_reservation_with_http_info(id, ip_reservation_request)

```ruby
begin
  # Requesting IP reservations
  data, status_code, headers = api_instance.request_ip_reservation_with_http_info(id, ip_reservation_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <IPReservation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling IPAddressesApi->request_ip_reservation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **ip_reservation_request** | [**IPReservationRequestInput**](IPReservationRequestInput.md) | IP Reservation Request to create |  |

### Return type

[**IPReservation**](IPReservation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

