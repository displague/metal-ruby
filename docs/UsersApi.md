# OpenapiClient::UsersApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_current_user**](UsersApi.md#find_current_user) | **GET** /user | Retrieve the current user |
| [**find_invitations**](UsersApi.md#find_invitations) | **GET** /invitations | Retrieve current user invitations |
| [**find_user_by_id**](UsersApi.md#find_user_by_id) | **GET** /users/{id} | Retrieve a user |
| [**find_user_customdata**](UsersApi.md#find_user_customdata) | **GET** /users/{id}/customdata | Retrieve the custom metadata of a user |
| [**find_users**](UsersApi.md#find_users) | **GET** /users | Retrieve all users |
| [**update_current_user**](UsersApi.md#update_current_user) | **PUT** /user | Update the current user |


## find_current_user

> <User> find_current_user(opts)

Retrieve the current user

Returns the user object for the currently logged-in user.

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

api_instance = OpenapiClient::UsersApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve the current user
  result = api_instance.find_current_user(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_current_user: #{e}"
end
```

#### Using the find_current_user_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<User>, Integer, Hash)> find_current_user_with_http_info(opts)

```ruby
begin
  # Retrieve the current user
  data, status_code, headers = api_instance.find_current_user_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <User>
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_current_user_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**User**](User.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_invitations

> <InvitationList> find_invitations(opts)

Retrieve current user invitations

Returns all invitations in current user.

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

api_instance = OpenapiClient::UsersApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve current user invitations
  result = api_instance.find_invitations(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_invitations: #{e}"
end
```

#### Using the find_invitations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InvitationList>, Integer, Hash)> find_invitations_with_http_info(opts)

```ruby
begin
  # Retrieve current user invitations
  data, status_code, headers = api_instance.find_invitations_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InvitationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_invitations_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**InvitationList**](InvitationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_user_by_id

> <User> find_user_by_id(id, opts)

Retrieve a user

Returns a single user if the user has access

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

api_instance = OpenapiClient::UsersApi.new
id = TODO # String | User UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a user
  result = api_instance.find_user_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_user_by_id: #{e}"
end
```

#### Using the find_user_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<User>, Integer, Hash)> find_user_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a user
  data, status_code, headers = api_instance.find_user_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <User>
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_user_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | User UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**User**](User.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_user_customdata

> find_user_customdata(id)

Retrieve the custom metadata of a user

Provides the custom metadata stored for this user in json format

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

api_instance = OpenapiClient::UsersApi.new
id = TODO # String | User UUID

begin
  # Retrieve the custom metadata of a user
  api_instance.find_user_customdata(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_user_customdata: #{e}"
end
```

#### Using the find_user_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_user_customdata_with_http_info(id)

```ruby
begin
  # Retrieve the custom metadata of a user
  data, status_code, headers = api_instance.find_user_customdata_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_user_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | User UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_users

> <UserList> find_users(opts)

Retrieve all users

Returns a list of users that the are accessible to the current user (all users in the current user’s projects, essentially).

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

api_instance = OpenapiClient::UsersApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all users
  result = api_instance.find_users(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_users: #{e}"
end
```

#### Using the find_users_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<UserList>, Integer, Hash)> find_users_with_http_info(opts)

```ruby
begin
  # Retrieve all users
  data, status_code, headers = api_instance.find_users_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <UserList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->find_users_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**UserList**](UserList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_current_user

> <User> update_current_user(user)

Update the current user

Updates the currently logged-in user.

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

api_instance = OpenapiClient::UsersApi.new
user = OpenapiClient::UserUpdateInput.new # UserUpdateInput | User to update

begin
  # Update the current user
  result = api_instance.update_current_user(user)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->update_current_user: #{e}"
end
```

#### Using the update_current_user_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<User>, Integer, Hash)> update_current_user_with_http_info(user)

```ruby
begin
  # Update the current user
  data, status_code, headers = api_instance.update_current_user_with_http_info(user)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <User>
rescue OpenapiClient::ApiError => e
  puts "Error when calling UsersApi->update_current_user_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **user** | [**UserUpdateInput**](UserUpdateInput.md) | User to update |  |

### Return type

[**User**](User.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

