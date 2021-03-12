# OpenapiClient::OperatingSystemVersionsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_operating_system_version**](OperatingSystemVersionsApi.md#find_operating_system_version) | **GET** /operating-system-versions | Retrieve all operating system versions |


## find_operating_system_version

> <Array<OperatingSystem>> find_operating_system_version

Retrieve all operating system versions

Provides a listing of available operating system versions.

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

api_instance = OpenapiClient::OperatingSystemVersionsApi.new

begin
  # Retrieve all operating system versions
  result = api_instance.find_operating_system_version
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OperatingSystemVersionsApi->find_operating_system_version: #{e}"
end
```

#### Using the find_operating_system_version_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<OperatingSystem>>, Integer, Hash)> find_operating_system_version_with_http_info

```ruby
begin
  # Retrieve all operating system versions
  data, status_code, headers = api_instance.find_operating_system_version_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<OperatingSystem>>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OperatingSystemVersionsApi->find_operating_system_version_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**Array&lt;OperatingSystem&gt;**](OperatingSystem.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

