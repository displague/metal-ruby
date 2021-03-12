# OpenapiClient::OperatingSystemsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_operating_systems**](OperatingSystemsApi.md#find_operating_systems) | **GET** /operating-systems | Retrieve all operating systems |
| [**find_operating_systems_by_organization**](OperatingSystemsApi.md#find_operating_systems_by_organization) | **GET** /organizations/{id}/operating-systems | Retrieve all operating systems visible by the organization |


## find_operating_systems

> <Array<OperatingSystem>> find_operating_systems

Retrieve all operating systems

Provides a listing of available operating systems to provision your new device with.

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

api_instance = OpenapiClient::OperatingSystemsApi.new

begin
  # Retrieve all operating systems
  result = api_instance.find_operating_systems
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OperatingSystemsApi->find_operating_systems: #{e}"
end
```

#### Using the find_operating_systems_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<OperatingSystem>>, Integer, Hash)> find_operating_systems_with_http_info

```ruby
begin
  # Retrieve all operating systems
  data, status_code, headers = api_instance.find_operating_systems_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<OperatingSystem>>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OperatingSystemsApi->find_operating_systems_with_http_info: #{e}"
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


## find_operating_systems_by_organization

> <Array<OperatingSystem>> find_operating_systems_by_organization(id, opts)

Retrieve all operating systems visible by the organization

Returns a listing of available operating systems for the given organization

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

api_instance = OpenapiClient::OperatingSystemsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all operating systems visible by the organization
  result = api_instance.find_operating_systems_by_organization(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OperatingSystemsApi->find_operating_systems_by_organization: #{e}"
end
```

#### Using the find_operating_systems_by_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<OperatingSystem>>, Integer, Hash)> find_operating_systems_by_organization_with_http_info(id, opts)

```ruby
begin
  # Retrieve all operating systems visible by the organization
  data, status_code, headers = api_instance.find_operating_systems_by_organization_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<OperatingSystem>>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OperatingSystemsApi->find_operating_systems_by_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Array&lt;OperatingSystem&gt;**](OperatingSystem.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

