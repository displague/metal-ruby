# OpenapiClient::TransferRequestsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**accept_transfer_request**](TransferRequestsApi.md#accept_transfer_request) | **PUT** /transfers/{id} | Accept a transfer request |
| [**create_transfer_request**](TransferRequestsApi.md#create_transfer_request) | **POST** /projects/{id}/transfers | Create a transfer request |
| [**decline_transfer_request**](TransferRequestsApi.md#decline_transfer_request) | **DELETE** /transfers/{id} | Decline a transfer request |
| [**find_organization_transfers**](TransferRequestsApi.md#find_organization_transfers) | **GET** /organizations/{id}/transfers | Retrieve all project transfer requests from or to an organization |
| [**find_transfer_request_by_id**](TransferRequestsApi.md#find_transfer_request_by_id) | **GET** /transfers/{id} | View a transfer request |


## accept_transfer_request

> accept_transfer_request(id)

Accept a transfer request

Accept a transfer request.

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

api_instance = OpenapiClient::TransferRequestsApi.new
id = TODO # String | Transfer request UUID

begin
  # Accept a transfer request
  api_instance.accept_transfer_request(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->accept_transfer_request: #{e}"
end
```

#### Using the accept_transfer_request_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> accept_transfer_request_with_http_info(id)

```ruby
begin
  # Accept a transfer request
  data, status_code, headers = api_instance.accept_transfer_request_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->accept_transfer_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Transfer request UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## create_transfer_request

> <TransferRequest> create_transfer_request(id, transfer_request)

Create a transfer request

Organization owners can transfer their projects to other organizations.

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

api_instance = OpenapiClient::TransferRequestsApi.new
id = TODO # String | UUID of the project to be transferred
transfer_request = OpenapiClient::TransferRequestInput.new # TransferRequestInput | Transfer Request to create

begin
  # Create a transfer request
  result = api_instance.create_transfer_request(id, transfer_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->create_transfer_request: #{e}"
end
```

#### Using the create_transfer_request_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransferRequest>, Integer, Hash)> create_transfer_request_with_http_info(id, transfer_request)

```ruby
begin
  # Create a transfer request
  data, status_code, headers = api_instance.create_transfer_request_with_http_info(id, transfer_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransferRequest>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->create_transfer_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | UUID of the project to be transferred |  |
| **transfer_request** | [**TransferRequestInput**](TransferRequestInput.md) | Transfer Request to create |  |

### Return type

[**TransferRequest**](TransferRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## decline_transfer_request

> decline_transfer_request(id)

Decline a transfer request

Decline a transfer request.

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

api_instance = OpenapiClient::TransferRequestsApi.new
id = TODO # String | Transfer request UUID

begin
  # Decline a transfer request
  api_instance.decline_transfer_request(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->decline_transfer_request: #{e}"
end
```

#### Using the decline_transfer_request_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> decline_transfer_request_with_http_info(id)

```ruby
begin
  # Decline a transfer request
  data, status_code, headers = api_instance.decline_transfer_request_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->decline_transfer_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Transfer request UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_organization_transfers

> <TransferRequestList> find_organization_transfers(id, opts)

Retrieve all project transfer requests from or to an organization

Provides a collection of project transfer requests from or to the organization.

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

api_instance = OpenapiClient::TransferRequestsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all project transfer requests from or to an organization
  result = api_instance.find_organization_transfers(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->find_organization_transfers: #{e}"
end
```

#### Using the find_organization_transfers_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransferRequestList>, Integer, Hash)> find_organization_transfers_with_http_info(id, opts)

```ruby
begin
  # Retrieve all project transfer requests from or to an organization
  data, status_code, headers = api_instance.find_organization_transfers_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransferRequestList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->find_organization_transfers_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**TransferRequestList**](TransferRequestList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_transfer_request_by_id

> <TransferRequest> find_transfer_request_by_id(id, opts)

View a transfer request

Returns a single transfer request.

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

api_instance = OpenapiClient::TransferRequestsApi.new
id = TODO # String | Transfer request UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # View a transfer request
  result = api_instance.find_transfer_request_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->find_transfer_request_by_id: #{e}"
end
```

#### Using the find_transfer_request_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransferRequest>, Integer, Hash)> find_transfer_request_by_id_with_http_info(id, opts)

```ruby
begin
  # View a transfer request
  data, status_code, headers = api_instance.find_transfer_request_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransferRequest>
rescue OpenapiClient::ApiError => e
  puts "Error when calling TransferRequestsApi->find_transfer_request_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Transfer request UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**TransferRequest**](TransferRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

