# OpenapiClient::TwoFactorAuthApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**disable_tfa_app**](TwoFactorAuthApi.md#disable_tfa_app) | **DELETE** /user/otp/app | Disable two factor authentication |
| [**disable_tfa_sms**](TwoFactorAuthApi.md#disable_tfa_sms) | **DELETE** /user/otp/sms | Disable two factor authentication |
| [**enable_tfa_app**](TwoFactorAuthApi.md#enable_tfa_app) | **POST** /user/otp/app | Enable two factor auth using app |
| [**enable_tfa_sms**](TwoFactorAuthApi.md#enable_tfa_sms) | **POST** /user/otp/sms | Enable two factor auth using sms |


## disable_tfa_app

> disable_tfa_app

Disable two factor authentication

Disables two factor authentication.

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

api_instance = OpenapiClient::TwoFactorAuthApi.new

begin
  # Disable two factor authentication
  api_instance.disable_tfa_app
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->disable_tfa_app: #{e}"
end
```

#### Using the disable_tfa_app_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> disable_tfa_app_with_http_info

```ruby
begin
  # Disable two factor authentication
  data, status_code, headers = api_instance.disable_tfa_app_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->disable_tfa_app_with_http_info: #{e}"
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


## disable_tfa_sms

> disable_tfa_sms

Disable two factor authentication

Disables two factor authentication.

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

api_instance = OpenapiClient::TwoFactorAuthApi.new

begin
  # Disable two factor authentication
  api_instance.disable_tfa_sms
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->disable_tfa_sms: #{e}"
end
```

#### Using the disable_tfa_sms_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> disable_tfa_sms_with_http_info

```ruby
begin
  # Disable two factor authentication
  data, status_code, headers = api_instance.disable_tfa_sms_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->disable_tfa_sms_with_http_info: #{e}"
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


## enable_tfa_app

> enable_tfa_app

Enable two factor auth using app

Enables two factor authentication using authenticator app.

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

api_instance = OpenapiClient::TwoFactorAuthApi.new

begin
  # Enable two factor auth using app
  api_instance.enable_tfa_app
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->enable_tfa_app: #{e}"
end
```

#### Using the enable_tfa_app_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> enable_tfa_app_with_http_info

```ruby
begin
  # Enable two factor auth using app
  data, status_code, headers = api_instance.enable_tfa_app_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->enable_tfa_app_with_http_info: #{e}"
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


## enable_tfa_sms

> enable_tfa_sms

Enable two factor auth using sms

Enables two factor authentication with sms.

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

api_instance = OpenapiClient::TwoFactorAuthApi.new

begin
  # Enable two factor auth using sms
  api_instance.enable_tfa_sms
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->enable_tfa_sms: #{e}"
end
```

#### Using the enable_tfa_sms_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> enable_tfa_sms_with_http_info

```ruby
begin
  # Enable two factor auth using sms
  data, status_code, headers = api_instance.enable_tfa_sms_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling TwoFactorAuthApi->enable_tfa_sms_with_http_info: #{e}"
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

