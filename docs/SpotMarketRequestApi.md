# OpenapiClient::SpotMarketRequestApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_spot_market_request**](SpotMarketRequestApi.md#create_spot_market_request) | **POST** /projects/{id}/spot-market-requests | Create a spot market request |
| [**delete_spot_market_request**](SpotMarketRequestApi.md#delete_spot_market_request) | **DELETE** /spot-market-requests/{id} | Delete the spot market request |
| [**find_spot_market_request_by_id**](SpotMarketRequestApi.md#find_spot_market_request_by_id) | **GET** /spot-market-requests/{id} | Retrieve a spot market request |
| [**list_spot_market_requests**](SpotMarketRequestApi.md#list_spot_market_requests) | **GET** /projects/{id}/spot-market-requests | List spot market requests |


## create_spot_market_request

> <SpotMarketRequest> create_spot_market_request(id, spot_market_request)

Create a spot market request

Creates a new spot market request.  Type-specific options (such as operating_system for baremetal devices) should be included in the main data structure alongside hostname and plan.  The features attribute allows you to optionally specify what features your server should have. For example, if you require a server with a TPM chip, you may specify `{ \"features\": { \"tpm\": \"required\" } }` (or `{ \"features\": [\"tpm\"] }` in shorthand).  The request will fail if there are no available servers matching your criteria. Alternatively, if you do not require a certain feature, but would prefer to be assigned a server with that feature if there are any available, you may specify that feature with a preferred value (see the example request below).  The request will not fail if we have no servers with that feature in our inventory.

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

api_instance = OpenapiClient::SpotMarketRequestApi.new
id = TODO # String | Project UUID
spot_market_request = OpenapiClient::SpotMarketRequestCreateInput.new # SpotMarketRequestCreateInput | Spot Market Request to create

begin
  # Create a spot market request
  result = api_instance.create_spot_market_request(id, spot_market_request)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->create_spot_market_request: #{e}"
end
```

#### Using the create_spot_market_request_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotMarketRequest>, Integer, Hash)> create_spot_market_request_with_http_info(id, spot_market_request)

```ruby
begin
  # Create a spot market request
  data, status_code, headers = api_instance.create_spot_market_request_with_http_info(id, spot_market_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotMarketRequest>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->create_spot_market_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **spot_market_request** | [**SpotMarketRequestCreateInput**](SpotMarketRequestCreateInput.md) | Spot Market Request to create |  |

### Return type

[**SpotMarketRequest**](SpotMarketRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_spot_market_request

> delete_spot_market_request(id, opts)

Delete the spot market request

Deletes the spot market request.

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

api_instance = OpenapiClient::SpotMarketRequestApi.new
id = TODO # String | SpotMarketRequest UUID
opts = {
  force_termination: true # Boolean | Terminate associated spot instances
}

begin
  # Delete the spot market request
  api_instance.delete_spot_market_request(id, opts)
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->delete_spot_market_request: #{e}"
end
```

#### Using the delete_spot_market_request_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_spot_market_request_with_http_info(id, opts)

```ruby
begin
  # Delete the spot market request
  data, status_code, headers = api_instance.delete_spot_market_request_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->delete_spot_market_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | SpotMarketRequest UUID |  |
| **force_termination** | **Boolean** | Terminate associated spot instances | [optional] |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_spot_market_request_by_id

> <SpotMarketRequest> find_spot_market_request_by_id(id, opts)

Retrieve a spot market request

Returns a single spot market request

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

api_instance = OpenapiClient::SpotMarketRequestApi.new
id = TODO # String | SpotMarketRequest UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a spot market request
  result = api_instance.find_spot_market_request_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->find_spot_market_request_by_id: #{e}"
end
```

#### Using the find_spot_market_request_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotMarketRequest>, Integer, Hash)> find_spot_market_request_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a spot market request
  data, status_code, headers = api_instance.find_spot_market_request_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotMarketRequest>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->find_spot_market_request_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | SpotMarketRequest UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SpotMarketRequest**](SpotMarketRequest.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_spot_market_requests

> <SpotMarketRequestList> list_spot_market_requests(id)

List spot market requests

View all spot market requests for a given project.

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

api_instance = OpenapiClient::SpotMarketRequestApi.new
id = TODO # String | Project UUID

begin
  # List spot market requests
  result = api_instance.list_spot_market_requests(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->list_spot_market_requests: #{e}"
end
```

#### Using the list_spot_market_requests_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SpotMarketRequestList>, Integer, Hash)> list_spot_market_requests_with_http_info(id)

```ruby
begin
  # List spot market requests
  data, status_code, headers = api_instance.list_spot_market_requests_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SpotMarketRequestList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SpotMarketRequestApi->list_spot_market_requests_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |

### Return type

[**SpotMarketRequestList**](SpotMarketRequestList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

