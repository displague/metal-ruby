# OpenapiClient::OtpsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_ensure_otp**](OtpsApi.md#find_ensure_otp) | **POST** /user/otp/verify/{otp} | Verify user by providing an OTP |
| [**find_recovery_codes**](OtpsApi.md#find_recovery_codes) | **GET** /user/otp/recovery-codes | Retrieve my recovery codes |
| [**receive_codes**](OtpsApi.md#receive_codes) | **POST** /user/otp/sms/receive | Receive an OTP per sms |
| [**regenerate_codes**](OtpsApi.md#regenerate_codes) | **POST** /user/otp/recovery-codes | Generate new recovery codes |


## find_ensure_otp

> find_ensure_otp(otp)

Verify user by providing an OTP

It verifies the user once a valid OTP is provided. It gives back a session token, essentially logging in the user.

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

api_instance = OpenapiClient::OtpsApi.new
otp = 'otp_example' # String | OTP

begin
  # Verify user by providing an OTP
  api_instance.find_ensure_otp(otp)
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->find_ensure_otp: #{e}"
end
```

#### Using the find_ensure_otp_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_ensure_otp_with_http_info(otp)

```ruby
begin
  # Verify user by providing an OTP
  data, status_code, headers = api_instance.find_ensure_otp_with_http_info(otp)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->find_ensure_otp_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **otp** | **String** | OTP |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_recovery_codes

> <RecoveryCodeList> find_recovery_codes

Retrieve my recovery codes

Returns my recovery codes.

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

api_instance = OpenapiClient::OtpsApi.new

begin
  # Retrieve my recovery codes
  result = api_instance.find_recovery_codes
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->find_recovery_codes: #{e}"
end
```

#### Using the find_recovery_codes_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<RecoveryCodeList>, Integer, Hash)> find_recovery_codes_with_http_info

```ruby
begin
  # Retrieve my recovery codes
  data, status_code, headers = api_instance.find_recovery_codes_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <RecoveryCodeList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->find_recovery_codes_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**RecoveryCodeList**](RecoveryCodeList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## receive_codes

> receive_codes

Receive an OTP per sms

Sends an OTP to the user's mobile phone.

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

api_instance = OpenapiClient::OtpsApi.new

begin
  # Receive an OTP per sms
  api_instance.receive_codes
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->receive_codes: #{e}"
end
```

#### Using the receive_codes_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> receive_codes_with_http_info

```ruby
begin
  # Receive an OTP per sms
  data, status_code, headers = api_instance.receive_codes_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->receive_codes_with_http_info: #{e}"
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


## regenerate_codes

> <RecoveryCodeList> regenerate_codes

Generate new recovery codes

Generate a new set of recovery codes.

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

api_instance = OpenapiClient::OtpsApi.new

begin
  # Generate new recovery codes
  result = api_instance.regenerate_codes
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->regenerate_codes: #{e}"
end
```

#### Using the regenerate_codes_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<RecoveryCodeList>, Integer, Hash)> regenerate_codes_with_http_info

```ruby
begin
  # Generate new recovery codes
  data, status_code, headers = api_instance.regenerate_codes_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <RecoveryCodeList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OtpsApi->regenerate_codes_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**RecoveryCodeList**](RecoveryCodeList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

