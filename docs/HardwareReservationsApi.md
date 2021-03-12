# OpenapiClient::HardwareReservationsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_hardware_reservation_by_id**](HardwareReservationsApi.md#find_hardware_reservation_by_id) | **GET** /hardware-reservations/{id} | Retrieve a hardware reservation |
| [**find_project_hardware_reservations**](HardwareReservationsApi.md#find_project_hardware_reservations) | **GET** /projects/{id}/hardware-reservations | Retrieve all hardware reservations for a given project |
| [**hardware_reservations_id_move_post**](HardwareReservationsApi.md#hardware_reservations_id_move_post) | **POST** /hardware-reservations/{id}/move | Move a hardware reservation |


## find_hardware_reservation_by_id

> <Device> find_hardware_reservation_by_id(id, opts)

Retrieve a hardware reservation

Returns a single hardware reservation

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

api_instance = OpenapiClient::HardwareReservationsApi.new
id = TODO # String | HardwareReservation UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a hardware reservation
  result = api_instance.find_hardware_reservation_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling HardwareReservationsApi->find_hardware_reservation_by_id: #{e}"
end
```

#### Using the find_hardware_reservation_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Device>, Integer, Hash)> find_hardware_reservation_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a hardware reservation
  data, status_code, headers = api_instance.find_hardware_reservation_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Device>
rescue OpenapiClient::ApiError => e
  puts "Error when calling HardwareReservationsApi->find_hardware_reservation_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | HardwareReservation UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Device**](Device.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_hardware_reservations

> <HardwareReservationList> find_project_hardware_reservations(id, opts)

Retrieve all hardware reservations for a given project

Provides a collection of hardware reservations for a given project.

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

api_instance = OpenapiClient::HardwareReservationsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all hardware reservations for a given project
  result = api_instance.find_project_hardware_reservations(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling HardwareReservationsApi->find_project_hardware_reservations: #{e}"
end
```

#### Using the find_project_hardware_reservations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HardwareReservationList>, Integer, Hash)> find_project_hardware_reservations_with_http_info(id, opts)

```ruby
begin
  # Retrieve all hardware reservations for a given project
  data, status_code, headers = api_instance.find_project_hardware_reservations_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HardwareReservationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling HardwareReservationsApi->find_project_hardware_reservations_with_http_info: #{e}"
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

[**HardwareReservationList**](HardwareReservationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## hardware_reservations_id_move_post

> <HardwareReservation> hardware_reservations_id_move_post(id, project_id)

Move a hardware reservation

Move a hardware reservation to another project

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

api_instance = OpenapiClient::HardwareReservationsApi.new
id = TODO # String | Hardware Reservation UUID
project_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # String | Project UUID

begin
  # Move a hardware reservation
  result = api_instance.hardware_reservations_id_move_post(id, project_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling HardwareReservationsApi->hardware_reservations_id_move_post: #{e}"
end
```

#### Using the hardware_reservations_id_move_post_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<HardwareReservation>, Integer, Hash)> hardware_reservations_id_move_post_with_http_info(id, project_id)

```ruby
begin
  # Move a hardware reservation
  data, status_code, headers = api_instance.hardware_reservations_id_move_post_with_http_info(id, project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <HardwareReservation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling HardwareReservationsApi->hardware_reservations_id_move_post_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Hardware Reservation UUID |  |
| **project_id** | **String** | Project UUID |  |

### Return type

[**HardwareReservation**](HardwareReservation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

