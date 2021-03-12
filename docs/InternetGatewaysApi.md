# OpenapiClient::InternetGatewaysApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_internet_gateway**](InternetGatewaysApi.md#create_internet_gateway) | **POST** /virtual-networks/{id}/internet-gateways | Create an internet gateway |


## create_internet_gateway

> <InternetGateway> create_internet_gateway(id, length)

Create an internet gateway

Creates an internet gateway.

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

api_instance = OpenapiClient::InternetGatewaysApi.new
id = TODO # String | Virtual Network UUID
length = 'length_example' # String | IP Reservation length

begin
  # Create an internet gateway
  result = api_instance.create_internet_gateway(id, length)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InternetGatewaysApi->create_internet_gateway: #{e}"
end
```

#### Using the create_internet_gateway_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InternetGateway>, Integer, Hash)> create_internet_gateway_with_http_info(id, length)

```ruby
begin
  # Create an internet gateway
  data, status_code, headers = api_instance.create_internet_gateway_with_http_info(id, length)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InternetGateway>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InternetGatewaysApi->create_internet_gateway_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Network UUID |  |
| **length** | **String** | IP Reservation length |  |

### Return type

[**InternetGateway**](InternetGateway.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

