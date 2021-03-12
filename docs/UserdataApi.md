# OpenapiClient::UserdataApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**validate_userdata**](UserdataApi.md#validate_userdata) | **POST** /userdata/validate | Validate user data |


## validate_userdata

> validate_userdata(opts)

Validate user data

Validates user data (Userdata)

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

api_instance = OpenapiClient::UserdataApi.new
opts = {
  userdata: 'userdata_example' # String | Userdata to validate
}

begin
  # Validate user data
  api_instance.validate_userdata(opts)
rescue OpenapiClient::ApiError => e
  puts "Error when calling UserdataApi->validate_userdata: #{e}"
end
```

#### Using the validate_userdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> validate_userdata_with_http_info(opts)

```ruby
begin
  # Validate user data
  data, status_code, headers = api_instance.validate_userdata_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling UserdataApi->validate_userdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **userdata** | **String** | Userdata to validate | [optional] |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined

