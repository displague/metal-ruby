# OpenapiClient::EmailsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_email**](EmailsApi.md#create_email) | **POST** /emails | Create an email |
| [**delete_email**](EmailsApi.md#delete_email) | **DELETE** /emails/{id} | Delete the email |
| [**find_email_by_id**](EmailsApi.md#find_email_by_id) | **GET** /emails/{id} | Retrieve an email |
| [**update_email**](EmailsApi.md#update_email) | **PUT** /emails/{id} | Update the email |


## create_email

> <Email> create_email(email)

Create an email

Add a new email address to the current user.

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

api_instance = OpenapiClient::EmailsApi.new
email = OpenapiClient::CreateEmailInput.new({address: 'address_example'}) # CreateEmailInput | Email to create

begin
  # Create an email
  result = api_instance.create_email(email)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->create_email: #{e}"
end
```

#### Using the create_email_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Email>, Integer, Hash)> create_email_with_http_info(email)

```ruby
begin
  # Create an email
  data, status_code, headers = api_instance.create_email_with_http_info(email)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Email>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->create_email_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **email** | [**CreateEmailInput**](CreateEmailInput.md) | Email to create |  |

### Return type

[**Email**](Email.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_email

> delete_email(id)

Delete the email

Deletes the email.

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

api_instance = OpenapiClient::EmailsApi.new
id = TODO # String | Email UUID

begin
  # Delete the email
  api_instance.delete_email(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->delete_email: #{e}"
end
```

#### Using the delete_email_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_email_with_http_info(id)

```ruby
begin
  # Delete the email
  data, status_code, headers = api_instance.delete_email_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->delete_email_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Email UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_email_by_id

> <Email> find_email_by_id(id, opts)

Retrieve an email

Provides one of the user’s emails.

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

api_instance = OpenapiClient::EmailsApi.new
id = TODO # String | Email UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve an email
  result = api_instance.find_email_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->find_email_by_id: #{e}"
end
```

#### Using the find_email_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Email>, Integer, Hash)> find_email_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve an email
  data, status_code, headers = api_instance.find_email_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Email>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->find_email_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Email UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Email**](Email.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_email

> <Email> update_email(id, email)

Update the email

Updates the email.

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

api_instance = OpenapiClient::EmailsApi.new
id = TODO # String | Email UUID
email = OpenapiClient::UpdateEmailInput.new # UpdateEmailInput | email to update

begin
  # Update the email
  result = api_instance.update_email(id, email)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->update_email: #{e}"
end
```

#### Using the update_email_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Email>, Integer, Hash)> update_email_with_http_info(id, email)

```ruby
begin
  # Update the email
  data, status_code, headers = api_instance.update_email_with_http_info(id, email)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Email>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EmailsApi->update_email_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Email UUID |  |
| **email** | [**UpdateEmailInput**](UpdateEmailInput.md) | email to update |  |

### Return type

[**Email**](Email.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

