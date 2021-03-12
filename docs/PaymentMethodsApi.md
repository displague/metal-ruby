# OpenapiClient::PaymentMethodsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_payment_method**](PaymentMethodsApi.md#create_payment_method) | **POST** /organizations/{id}/payment-methods | Create a payment method for the given organization |
| [**delete_payment_method**](PaymentMethodsApi.md#delete_payment_method) | **DELETE** /payment-methods/{id} | Delete the payment method |
| [**find_organization_payment_methods**](PaymentMethodsApi.md#find_organization_payment_methods) | **GET** /organizations/{id}/payment-methods | Retrieve all payment methods of an organization |
| [**find_payment_method_by_id**](PaymentMethodsApi.md#find_payment_method_by_id) | **GET** /payment-methods/{id} | Retrieve a payment method |
| [**update_payment_method**](PaymentMethodsApi.md#update_payment_method) | **PUT** /payment-methods/{id} | Update the payment method |


## create_payment_method

> <PaymentMethod> create_payment_method(id, payment_method)

Create a payment method for the given organization

Creates a payment method.

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

api_instance = OpenapiClient::PaymentMethodsApi.new
id = TODO # String | Organization UUID
payment_method = OpenapiClient::PaymentMethodCreateInput.new({name: 'name_example', nonce: 'nonce_example'}) # PaymentMethodCreateInput | Payment Method to create

begin
  # Create a payment method for the given organization
  result = api_instance.create_payment_method(id, payment_method)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->create_payment_method: #{e}"
end
```

#### Using the create_payment_method_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PaymentMethod>, Integer, Hash)> create_payment_method_with_http_info(id, payment_method)

```ruby
begin
  # Create a payment method for the given organization
  data, status_code, headers = api_instance.create_payment_method_with_http_info(id, payment_method)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PaymentMethod>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->create_payment_method_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **payment_method** | [**PaymentMethodCreateInput**](PaymentMethodCreateInput.md) | Payment Method to create |  |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_payment_method

> delete_payment_method(id)

Delete the payment method

Deletes the payment method.

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

api_instance = OpenapiClient::PaymentMethodsApi.new
id = TODO # String | Payment Method UUID

begin
  # Delete the payment method
  api_instance.delete_payment_method(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->delete_payment_method: #{e}"
end
```

#### Using the delete_payment_method_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_payment_method_with_http_info(id)

```ruby
begin
  # Delete the payment method
  data, status_code, headers = api_instance.delete_payment_method_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->delete_payment_method_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Payment Method UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_organization_payment_methods

> <PaymentMethodList> find_organization_payment_methods(id, opts)

Retrieve all payment methods of an organization

Returns all payment methods of an organization.

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

api_instance = OpenapiClient::PaymentMethodsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all payment methods of an organization
  result = api_instance.find_organization_payment_methods(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->find_organization_payment_methods: #{e}"
end
```

#### Using the find_organization_payment_methods_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PaymentMethodList>, Integer, Hash)> find_organization_payment_methods_with_http_info(id, opts)

```ruby
begin
  # Retrieve all payment methods of an organization
  data, status_code, headers = api_instance.find_organization_payment_methods_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PaymentMethodList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->find_organization_payment_methods_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**PaymentMethodList**](PaymentMethodList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_payment_method_by_id

> <PaymentMethod> find_payment_method_by_id(id, opts)

Retrieve a payment method

Returns a payment method

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

api_instance = OpenapiClient::PaymentMethodsApi.new
id = TODO # String | Payment Method UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a payment method
  result = api_instance.find_payment_method_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->find_payment_method_by_id: #{e}"
end
```

#### Using the find_payment_method_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PaymentMethod>, Integer, Hash)> find_payment_method_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a payment method
  data, status_code, headers = api_instance.find_payment_method_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PaymentMethod>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->find_payment_method_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Payment Method UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_payment_method

> <PaymentMethod> update_payment_method(id, payment_method)

Update the payment method

Updates the payment method.

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

api_instance = OpenapiClient::PaymentMethodsApi.new
id = TODO # String | Payment Method UUID
payment_method = OpenapiClient::PaymentMethodUpdateInput.new # PaymentMethodUpdateInput | Payment Method to update

begin
  # Update the payment method
  result = api_instance.update_payment_method(id, payment_method)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->update_payment_method: #{e}"
end
```

#### Using the update_payment_method_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PaymentMethod>, Integer, Hash)> update_payment_method_with_http_info(id, payment_method)

```ruby
begin
  # Update the payment method
  data, status_code, headers = api_instance.update_payment_method_with_http_info(id, payment_method)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PaymentMethod>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PaymentMethodsApi->update_payment_method_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Payment Method UUID |  |
| **payment_method** | [**PaymentMethodUpdateInput**](PaymentMethodUpdateInput.md) | Payment Method to update |  |

### Return type

[**PaymentMethod**](PaymentMethod.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

