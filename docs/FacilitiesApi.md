# OpenapiClient::FacilitiesApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_facilities**](FacilitiesApi.md#find_facilities) | **GET** /facilities | Retrieve all facilities |
| [**find_facilities_by_organization**](FacilitiesApi.md#find_facilities_by_organization) | **GET** /organizations/{id}/facilities | Retrieve all facilities visible by the organization |
| [**find_facilities_by_project**](FacilitiesApi.md#find_facilities_by_project) | **GET** /projects/{id}/facilities | Retrieve all facilities visible by the project |


## find_facilities

> <FacilityList> find_facilities(opts)

Retrieve all facilities

Provides a listing of available datacenters where you can provision Packet devices.

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

api_instance = OpenapiClient::FacilitiesApi.new
opts = {
  include: ['address'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['address'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all facilities
  result = api_instance.find_facilities(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling FacilitiesApi->find_facilities: #{e}"
end
```

#### Using the find_facilities_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FacilityList>, Integer, Hash)> find_facilities_with_http_info(opts)

```ruby
begin
  # Retrieve all facilities
  data, status_code, headers = api_instance.find_facilities_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FacilityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling FacilitiesApi->find_facilities_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**FacilityList**](FacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_facilities_by_organization

> <FacilityList> find_facilities_by_organization(id, opts)

Retrieve all facilities visible by the organization

Returns a listing of available datacenters for the given organization

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

api_instance = OpenapiClient::FacilitiesApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all facilities visible by the organization
  result = api_instance.find_facilities_by_organization(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling FacilitiesApi->find_facilities_by_organization: #{e}"
end
```

#### Using the find_facilities_by_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FacilityList>, Integer, Hash)> find_facilities_by_organization_with_http_info(id, opts)

```ruby
begin
  # Retrieve all facilities visible by the organization
  data, status_code, headers = api_instance.find_facilities_by_organization_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FacilityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling FacilitiesApi->find_facilities_by_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**FacilityList**](FacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_facilities_by_project

> <FacilityList> find_facilities_by_project(id, opts)

Retrieve all facilities visible by the project

Returns a listing of available datacenters for the given project

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

api_instance = OpenapiClient::FacilitiesApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all facilities visible by the project
  result = api_instance.find_facilities_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling FacilitiesApi->find_facilities_by_project: #{e}"
end
```

#### Using the find_facilities_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FacilityList>, Integer, Hash)> find_facilities_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve all facilities visible by the project
  data, status_code, headers = api_instance.find_facilities_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FacilityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling FacilitiesApi->find_facilities_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**FacilityList**](FacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

