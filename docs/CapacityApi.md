# OpenapiClient::CapacityApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**check_capacity_for_facility**](CapacityApi.md#check_capacity_for_facility) | **POST** /capacity | Check capacity |
| [**find_capacity_for_facility**](CapacityApi.md#find_capacity_for_facility) | **GET** /capacity | View capacity |


## check_capacity_for_facility

> <CapacityCheckPerFacilityList> check_capacity_for_facility(facility)

Check capacity

Validates if a deploy can be fulfilled.

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

api_instance = OpenapiClient::CapacityApi.new
facility = OpenapiClient::CapacityInput.new # CapacityInput | Facility to check capacity in

begin
  # Check capacity
  result = api_instance.check_capacity_for_facility(facility)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling CapacityApi->check_capacity_for_facility: #{e}"
end
```

#### Using the check_capacity_for_facility_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CapacityCheckPerFacilityList>, Integer, Hash)> check_capacity_for_facility_with_http_info(facility)

```ruby
begin
  # Check capacity
  data, status_code, headers = api_instance.check_capacity_for_facility_with_http_info(facility)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CapacityCheckPerFacilityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling CapacityApi->check_capacity_for_facility_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **facility** | [**CapacityInput**](CapacityInput.md) | Facility to check capacity in |  |

### Return type

[**CapacityCheckPerFacilityList**](CapacityCheckPerFacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## find_capacity_for_facility

> <CapacityList> find_capacity_for_facility

View capacity

Returns a list of facilities and plans with their current capacity.

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

api_instance = OpenapiClient::CapacityApi.new

begin
  # View capacity
  result = api_instance.find_capacity_for_facility
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling CapacityApi->find_capacity_for_facility: #{e}"
end
```

#### Using the find_capacity_for_facility_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<CapacityList>, Integer, Hash)> find_capacity_for_facility_with_http_info

```ruby
begin
  # View capacity
  data, status_code, headers = api_instance.find_capacity_for_facility_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <CapacityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling CapacityApi->find_capacity_for_facility_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**CapacityList**](CapacityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

