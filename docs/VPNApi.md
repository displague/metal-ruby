# OpenapiClient::VPNApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_current_user_vpn_config**](VPNApi.md#find_current_user_vpn_config) | **GET** /user/vpn | Retrieve the client vpn config for current user |
| [**turn_off_current_user_vpn**](VPNApi.md#turn_off_current_user_vpn) | **DELETE** /user/vpn | Turn off vpn for the current user |
| [**turn_on_current_user_vpn**](VPNApi.md#turn_on_current_user_vpn) | **POST** /user/vpn | Turn on vpn for the current user |


## find_current_user_vpn_config

> <VPNConfig> find_current_user_vpn_config(code)

Retrieve the client vpn config for current user

Returns the client vpn config for the currently logged-in user.

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

api_instance = OpenapiClient::VPNApi.new
code = 'ewr1' # String | Facility code

begin
  # Retrieve the client vpn config for current user
  result = api_instance.find_current_user_vpn_config(code)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VPNApi->find_current_user_vpn_config: #{e}"
end
```

#### Using the find_current_user_vpn_config_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VPNConfig>, Integer, Hash)> find_current_user_vpn_config_with_http_info(code)

```ruby
begin
  # Retrieve the client vpn config for current user
  data, status_code, headers = api_instance.find_current_user_vpn_config_with_http_info(code)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VPNConfig>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VPNApi->find_current_user_vpn_config_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **code** | **String** | Facility code |  |

### Return type

[**VPNConfig**](VPNConfig.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## turn_off_current_user_vpn

> turn_off_current_user_vpn

Turn off vpn for the current user

Turns off vpn for the currently logged-in user.

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

api_instance = OpenapiClient::VPNApi.new

begin
  # Turn off vpn for the current user
  api_instance.turn_off_current_user_vpn
rescue OpenapiClient::ApiError => e
  puts "Error when calling VPNApi->turn_off_current_user_vpn: #{e}"
end
```

#### Using the turn_off_current_user_vpn_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> turn_off_current_user_vpn_with_http_info

```ruby
begin
  # Turn off vpn for the current user
  data, status_code, headers = api_instance.turn_off_current_user_vpn_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VPNApi->turn_off_current_user_vpn_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## turn_on_current_user_vpn

> turn_on_current_user_vpn

Turn on vpn for the current user

Turns on vpn for the currently logged-in user.

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

api_instance = OpenapiClient::VPNApi.new

begin
  # Turn on vpn for the current user
  api_instance.turn_on_current_user_vpn
rescue OpenapiClient::ApiError => e
  puts "Error when calling VPNApi->turn_on_current_user_vpn: #{e}"
end
```

#### Using the turn_on_current_user_vpn_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> turn_on_current_user_vpn_with_http_info

```ruby
begin
  # Turn on vpn for the current user
  data, status_code, headers = api_instance.turn_on_current_user_vpn_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling VPNApi->turn_on_current_user_vpn_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

