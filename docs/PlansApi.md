# OpenapiClient::PlansApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_plans**](PlansApi.md#find_plans) | **GET** /plans | Retrieve all plans |
| [**find_plans_by_organization**](PlansApi.md#find_plans_by_organization) | **GET** /organizations/{id}/plans | Retrieve all plans visible by the organization |
| [**find_plans_by_project**](PlansApi.md#find_plans_by_project) | **GET** /projects/{id}/plans | Retrieve all plans visible by the project |


## find_plans

> <PlanList> find_plans(opts)

Retrieve all plans

Provides a listing of available plans to provision your device on.

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

api_instance = OpenapiClient::PlansApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all plans
  result = api_instance.find_plans(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PlansApi->find_plans: #{e}"
end
```

#### Using the find_plans_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PlanList>, Integer, Hash)> find_plans_with_http_info(opts)

```ruby
begin
  # Retrieve all plans
  data, status_code, headers = api_instance.find_plans_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PlanList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PlansApi->find_plans_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**PlanList**](PlanList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_plans_by_organization

> <PlanList> find_plans_by_organization(id, opts)

Retrieve all plans visible by the organization

Returns a listing of available plans for the given organization

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

api_instance = OpenapiClient::PlansApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all plans visible by the organization
  result = api_instance.find_plans_by_organization(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PlansApi->find_plans_by_organization: #{e}"
end
```

#### Using the find_plans_by_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PlanList>, Integer, Hash)> find_plans_by_organization_with_http_info(id, opts)

```ruby
begin
  # Retrieve all plans visible by the organization
  data, status_code, headers = api_instance.find_plans_by_organization_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PlanList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PlansApi->find_plans_by_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**PlanList**](PlanList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_plans_by_project

> <PlanList> find_plans_by_project(id, opts)

Retrieve all plans visible by the project

Returns a listing of available plans for the given project

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

api_instance = OpenapiClient::PlansApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all plans visible by the project
  result = api_instance.find_plans_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PlansApi->find_plans_by_project: #{e}"
end
```

#### Using the find_plans_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PlanList>, Integer, Hash)> find_plans_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve all plans visible by the project
  data, status_code, headers = api_instance.find_plans_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PlanList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PlansApi->find_plans_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**PlanList**](PlanList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

