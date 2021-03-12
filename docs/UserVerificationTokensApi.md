# OpenapiClient::UserVerificationTokensApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**consume_verification_request**](UserVerificationTokensApi.md#consume_verification_request) | **PUT** /verify-email | Verify a user using an email verification token |
| [**create_validation_request**](UserVerificationTokensApi.md#create_validation_request) | **POST** /verify-email | Create an email verification request |


## consume_verification_request

> consume_verification_request(token)

Verify a user using an email verification token

Consumes an email verification token and verifies the user associated with it.

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

api_instance = OpenapiClient::UserVerificationTokensApi.new
token = 'token_example' # String | User verification token

begin
  # Verify a user using an email verification token
  api_instance.consume_verification_request(token)
rescue OpenapiClient::ApiError => e
  puts "Error when calling UserVerificationTokensApi->consume_verification_request: #{e}"
end
```

#### Using the consume_verification_request_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> consume_verification_request_with_http_info(token)

```ruby
begin
  # Verify a user using an email verification token
  data, status_code, headers = api_instance.consume_verification_request_with_http_info(token)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling UserVerificationTokensApi->consume_verification_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **token** | **String** | User verification token |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## create_validation_request

> create_validation_request(login)

Create an email verification request

Creates an email verification request

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

api_instance = OpenapiClient::UserVerificationTokensApi.new
login = 'login_example' # String | Email for verification request

begin
  # Create an email verification request
  api_instance.create_validation_request(login)
rescue OpenapiClient::ApiError => e
  puts "Error when calling UserVerificationTokensApi->create_validation_request: #{e}"
end
```

#### Using the create_validation_request_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> create_validation_request_with_http_info(login)

```ruby
begin
  # Create an email verification request
  data, status_code, headers = api_instance.create_validation_request_with_http_info(login)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling UserVerificationTokensApi->create_validation_request_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **login** | **String** | Email for verification request |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

