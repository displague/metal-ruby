# OpenapiClient::PasswordResetTokensApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_password_reset_token**](PasswordResetTokensApi.md#create_password_reset_token) | **POST** /reset-password | Create a password reset token |
| [**reset_password**](PasswordResetTokensApi.md#reset_password) | **DELETE** /reset-password | Reset current user password |


## create_password_reset_token

> create_password_reset_token(email)

Create a password reset token

Creates a password reset token

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

api_instance = OpenapiClient::PasswordResetTokensApi.new
email = 'email_example' # String | Email of user to create password reset token

begin
  # Create a password reset token
  api_instance.create_password_reset_token(email)
rescue OpenapiClient::ApiError => e
  puts "Error when calling PasswordResetTokensApi->create_password_reset_token: #{e}"
end
```

#### Using the create_password_reset_token_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> create_password_reset_token_with_http_info(email)

```ruby
begin
  # Create a password reset token
  data, status_code, headers = api_instance.create_password_reset_token_with_http_info(email)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling PasswordResetTokensApi->create_password_reset_token_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **email** | **String** | Email of user to create password reset token |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## reset_password

> <NewPassword> reset_password

Reset current user password

Resets current user password.

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

api_instance = OpenapiClient::PasswordResetTokensApi.new

begin
  # Reset current user password
  result = api_instance.reset_password
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PasswordResetTokensApi->reset_password: #{e}"
end
```

#### Using the reset_password_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<NewPassword>, Integer, Hash)> reset_password_with_http_info

```ruby
begin
  # Reset current user password
  data, status_code, headers = api_instance.reset_password_with_http_info
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <NewPassword>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PasswordResetTokensApi->reset_password_with_http_info: #{e}"
end
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**NewPassword**](NewPassword.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

