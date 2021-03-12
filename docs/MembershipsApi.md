# OpenapiClient::MembershipsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**delete_membership**](MembershipsApi.md#delete_membership) | **DELETE** /memberships/{id} | Delete the membership |
| [**find_membership_by_id**](MembershipsApi.md#find_membership_by_id) | **GET** /memberships/{id} | Retrieve a membership |
| [**find_project_memberships**](MembershipsApi.md#find_project_memberships) | **GET** /projects/{project_id}/memberships | Retrieve project memberships |
| [**update_membership**](MembershipsApi.md#update_membership) | **PUT** /memberships/{id} | Update the membership |


## delete_membership

> delete_membership(id)

Delete the membership

Deletes the membership.

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

api_instance = OpenapiClient::MembershipsApi.new
id = TODO # String | Membership UUID

begin
  # Delete the membership
  api_instance.delete_membership(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->delete_membership: #{e}"
end
```

#### Using the delete_membership_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_membership_with_http_info(id)

```ruby
begin
  # Delete the membership
  data, status_code, headers = api_instance.delete_membership_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->delete_membership_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Membership UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_membership_by_id

> <Membership> find_membership_by_id(id, opts)

Retrieve a membership

Returns a single membership.

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

api_instance = OpenapiClient::MembershipsApi.new
id = TODO # String | Membership UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a membership
  result = api_instance.find_membership_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->find_membership_by_id: #{e}"
end
```

#### Using the find_membership_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Membership>, Integer, Hash)> find_membership_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a membership
  data, status_code, headers = api_instance.find_membership_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Membership>
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->find_membership_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Membership UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Membership**](Membership.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_memberships

> <MembershipList> find_project_memberships(project_id, opts)

Retrieve project memberships

Returns all memberships in a project.

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

api_instance = OpenapiClient::MembershipsApi.new
project_id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve project memberships
  result = api_instance.find_project_memberships(project_id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->find_project_memberships: #{e}"
end
```

#### Using the find_project_memberships_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<MembershipList>, Integer, Hash)> find_project_memberships_with_http_info(project_id, opts)

```ruby
begin
  # Retrieve project memberships
  data, status_code, headers = api_instance.find_project_memberships_with_http_info(project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <MembershipList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->find_project_memberships_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**MembershipList**](MembershipList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_membership

> <Membership> update_membership(id, membership)

Update the membership

Updates the membership.

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

api_instance = OpenapiClient::MembershipsApi.new
id = TODO # String | Membership UUID
membership = OpenapiClient::MembershipInput.new # MembershipInput | Membership to update

begin
  # Update the membership
  result = api_instance.update_membership(id, membership)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->update_membership: #{e}"
end
```

#### Using the update_membership_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Membership>, Integer, Hash)> update_membership_with_http_info(id, membership)

```ruby
begin
  # Update the membership
  data, status_code, headers = api_instance.update_membership_with_http_info(id, membership)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Membership>
rescue OpenapiClient::ApiError => e
  puts "Error when calling MembershipsApi->update_membership_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Membership UUID |  |
| **membership** | [**MembershipInput**](MembershipInput.md) | Membership to update |  |

### Return type

[**Membership**](Membership.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

