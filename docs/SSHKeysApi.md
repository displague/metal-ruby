# OpenapiClient::SSHKeysApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_project_ssh_key**](SSHKeysApi.md#create_project_ssh_key) | **POST** /projects/{id}/ssh-keys | Create a ssh key for the given project |
| [**create_ssh_key**](SSHKeysApi.md#create_ssh_key) | **POST** /ssh-keys | Create a ssh key for the current user |
| [**delete_ssh_key**](SSHKeysApi.md#delete_ssh_key) | **DELETE** /ssh-keys/{id} | Delete the ssh key |
| [**find_device_ssh_keys**](SSHKeysApi.md#find_device_ssh_keys) | **GET** /devices/{id}/ssh-keys | Retrieve a device&#39;s ssh keys |
| [**find_project_ssh_keys**](SSHKeysApi.md#find_project_ssh_keys) | **GET** /projects/{id}/ssh-keys | Retrieve a project&#39;s ssh keys |
| [**find_ssh_key_by_id**](SSHKeysApi.md#find_ssh_key_by_id) | **GET** /ssh-keys/{id} | Retrieve a ssh key |
| [**find_ssh_keys**](SSHKeysApi.md#find_ssh_keys) | **GET** /ssh-keys | Retrieve all ssh keys |
| [**update_ssh_key**](SSHKeysApi.md#update_ssh_key) | **PUT** /ssh-keys/{id} | Update the ssh key |


## create_project_ssh_key

> <SSHKey> create_project_ssh_key(id, ssh_key)

Create a ssh key for the given project

Creates a ssh key.

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

api_instance = OpenapiClient::SSHKeysApi.new
id = TODO # String | Project UUID
ssh_key = OpenapiClient::SSHKeyInput.new # SSHKeyInput | ssh key to create

begin
  # Create a ssh key for the given project
  result = api_instance.create_project_ssh_key(id, ssh_key)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->create_project_ssh_key: #{e}"
end
```

#### Using the create_project_ssh_key_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKey>, Integer, Hash)> create_project_ssh_key_with_http_info(id, ssh_key)

```ruby
begin
  # Create a ssh key for the given project
  data, status_code, headers = api_instance.create_project_ssh_key_with_http_info(id, ssh_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKey>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->create_project_ssh_key_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **ssh_key** | [**SSHKeyInput**](SSHKeyInput.md) | ssh key to create |  |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_ssh_key

> <SSHKey> create_ssh_key(ssh_key)

Create a ssh key for the current user

Creates a ssh key.

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

api_instance = OpenapiClient::SSHKeysApi.new
ssh_key = OpenapiClient::SSHKeyInput.new # SSHKeyInput | ssh key to create

begin
  # Create a ssh key for the current user
  result = api_instance.create_ssh_key(ssh_key)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->create_ssh_key: #{e}"
end
```

#### Using the create_ssh_key_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKey>, Integer, Hash)> create_ssh_key_with_http_info(ssh_key)

```ruby
begin
  # Create a ssh key for the current user
  data, status_code, headers = api_instance.create_ssh_key_with_http_info(ssh_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKey>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->create_ssh_key_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **ssh_key** | [**SSHKeyInput**](SSHKeyInput.md) | ssh key to create |  |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_ssh_key

> delete_ssh_key(id)

Delete the ssh key

Deletes the ssh key.

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

api_instance = OpenapiClient::SSHKeysApi.new
id = TODO # String | ssh key UUID

begin
  # Delete the ssh key
  api_instance.delete_ssh_key(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->delete_ssh_key: #{e}"
end
```

#### Using the delete_ssh_key_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_ssh_key_with_http_info(id)

```ruby
begin
  # Delete the ssh key
  data, status_code, headers = api_instance.delete_ssh_key_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->delete_ssh_key_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | ssh key UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_device_ssh_keys

> <SSHKeyList> find_device_ssh_keys(id, opts)

Retrieve a device's ssh keys

Returns a collection of the device's ssh keys.

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

api_instance = OpenapiClient::SSHKeysApi.new
id = TODO # String | Project UUID
opts = {
  search_string: 'search_string_example', # String | Search by key, label, or fingerprint
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a device's ssh keys
  result = api_instance.find_device_ssh_keys(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_device_ssh_keys: #{e}"
end
```

#### Using the find_device_ssh_keys_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKeyList>, Integer, Hash)> find_device_ssh_keys_with_http_info(id, opts)

```ruby
begin
  # Retrieve a device's ssh keys
  data, status_code, headers = api_instance.find_device_ssh_keys_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKeyList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_device_ssh_keys_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **search_string** | **String** | Search by key, label, or fingerprint | [optional] |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SSHKeyList**](SSHKeyList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_ssh_keys

> <SSHKeyList> find_project_ssh_keys(id, opts)

Retrieve a project's ssh keys

Returns a collection of the project's ssh keys.

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

api_instance = OpenapiClient::SSHKeysApi.new
id = TODO # String | Project UUID
opts = {
  search_string: 'search_string_example', # String | Search by key, label, or fingerprint
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a project's ssh keys
  result = api_instance.find_project_ssh_keys(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_project_ssh_keys: #{e}"
end
```

#### Using the find_project_ssh_keys_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKeyList>, Integer, Hash)> find_project_ssh_keys_with_http_info(id, opts)

```ruby
begin
  # Retrieve a project's ssh keys
  data, status_code, headers = api_instance.find_project_ssh_keys_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKeyList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_project_ssh_keys_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **search_string** | **String** | Search by key, label, or fingerprint | [optional] |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SSHKeyList**](SSHKeyList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_ssh_key_by_id

> <SSHKey> find_ssh_key_by_id(id, opts)

Retrieve a ssh key

Returns a single ssh key if the user has access

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

api_instance = OpenapiClient::SSHKeysApi.new
id = TODO # String | SSH Key UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a ssh key
  result = api_instance.find_ssh_key_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_ssh_key_by_id: #{e}"
end
```

#### Using the find_ssh_key_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKey>, Integer, Hash)> find_ssh_key_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a ssh key
  data, status_code, headers = api_instance.find_ssh_key_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKey>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_ssh_key_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | SSH Key UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_ssh_keys

> <SSHKeyList> find_ssh_keys(opts)

Retrieve all ssh keys

Returns a collection of the user’s ssh keys.

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

api_instance = OpenapiClient::SSHKeysApi.new
opts = {
  search_string: 'search_string_example', # String | Search by key, label, or fingerprint
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all ssh keys
  result = api_instance.find_ssh_keys(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_ssh_keys: #{e}"
end
```

#### Using the find_ssh_keys_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKeyList>, Integer, Hash)> find_ssh_keys_with_http_info(opts)

```ruby
begin
  # Retrieve all ssh keys
  data, status_code, headers = api_instance.find_ssh_keys_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKeyList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->find_ssh_keys_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **search_string** | **String** | Search by key, label, or fingerprint | [optional] |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**SSHKeyList**](SSHKeyList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_ssh_key

> <SSHKey> update_ssh_key(id, ssh_key)

Update the ssh key

Updates the ssh key.

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

api_instance = OpenapiClient::SSHKeysApi.new
id = TODO # String | SSH Key UUID
ssh_key = OpenapiClient::SSHKeyInput.new # SSHKeyInput | ssh key to update

begin
  # Update the ssh key
  result = api_instance.update_ssh_key(id, ssh_key)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->update_ssh_key: #{e}"
end
```

#### Using the update_ssh_key_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<SSHKey>, Integer, Hash)> update_ssh_key_with_http_info(id, ssh_key)

```ruby
begin
  # Update the ssh key
  data, status_code, headers = api_instance.update_ssh_key_with_http_info(id, ssh_key)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <SSHKey>
rescue OpenapiClient::ApiError => e
  puts "Error when calling SSHKeysApi->update_ssh_key_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | SSH Key UUID |  |
| **ssh_key** | [**SSHKeyInput**](SSHKeyInput.md) | ssh key to update |  |

### Return type

[**SSHKey**](SSHKey.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

