# OpenapiClient::UsagesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_device_usages**](UsagesApi.md#find_device_usages) | **GET** /devices/{id}/usages | Retrieve all usages for device |
| [**find_project_usage**](UsagesApi.md#find_project_usage) | **GET** /projects/{id}/usages | Retrieve all usages for project |


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

api_instance = OpenapiClient::UsagesApi.new
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
  puts "Error when calling UsagesApi->find_device_usages: #{e}"
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
  puts "Error when calling UsagesApi->find_device_usages_with_http_info: #{e}"
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

api_instance = OpenapiClient::UsagesApi.new
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
  puts "Error when calling UsagesApi->find_project_usage: #{e}"
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
  puts "Error when calling UsagesApi->find_project_usage_with_http_info: #{e}"
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

