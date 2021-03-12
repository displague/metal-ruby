# OpenapiClient::InvitationsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**accept_invitation**](InvitationsApi.md#accept_invitation) | **PUT** /invitations/{id} | Accept an invitation |
| [**create_organization_invitation**](InvitationsApi.md#create_organization_invitation) | **POST** /organizations/{id}/invitations | Create an invitation for an organization |
| [**create_project_invitation**](InvitationsApi.md#create_project_invitation) | **POST** /projects/{project_id}/invitations | Create an invitation for a project |
| [**decline_invitation**](InvitationsApi.md#decline_invitation) | **DELETE** /invitations/{id} | Decline an invitation |
| [**find_invitation_by_id**](InvitationsApi.md#find_invitation_by_id) | **GET** /invitations/{id} | View an invitation |
| [**find_invitations**](InvitationsApi.md#find_invitations) | **GET** /invitations | Retrieve current user invitations |
| [**find_organization_invitations**](InvitationsApi.md#find_organization_invitations) | **GET** /organizations/{id}/invitations | Retrieve organization invitations |
| [**find_project_invitations**](InvitationsApi.md#find_project_invitations) | **GET** /projects/{project_id}/invitations | Retrieve project invitations |


## accept_invitation

> <Membership> accept_invitation(id)

Accept an invitation

Accept an invitation.

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

api_instance = OpenapiClient::InvitationsApi.new
id = TODO # String | Invitation UUID

begin
  # Accept an invitation
  result = api_instance.accept_invitation(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->accept_invitation: #{e}"
end
```

#### Using the accept_invitation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Membership>, Integer, Hash)> accept_invitation_with_http_info(id)

```ruby
begin
  # Accept an invitation
  data, status_code, headers = api_instance.accept_invitation_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Membership>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->accept_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Invitation UUID |  |

### Return type

[**Membership**](Membership.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_organization_invitation

> <Invitation> create_organization_invitation(id, invitation)

Create an invitation for an organization

In order to add a user to an organization, they must first be invited. To invite to several projects the parameter `projects_ids:[a,b,c]` can be used

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

api_instance = OpenapiClient::InvitationsApi.new
id = TODO # String | Organization UUID
invitation = OpenapiClient::InvitationInput.new({invitee: 'invitee_example'}) # InvitationInput | Invitation to create

begin
  # Create an invitation for an organization
  result = api_instance.create_organization_invitation(id, invitation)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->create_organization_invitation: #{e}"
end
```

#### Using the create_organization_invitation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Invitation>, Integer, Hash)> create_organization_invitation_with_http_info(id, invitation)

```ruby
begin
  # Create an invitation for an organization
  data, status_code, headers = api_instance.create_organization_invitation_with_http_info(id, invitation)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Invitation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->create_organization_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **invitation** | [**InvitationInput**](InvitationInput.md) | Invitation to create |  |

### Return type

[**Invitation**](Invitation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_project_invitation

> <Invitation> create_project_invitation(project_id, invitation)

Create an invitation for a project

In order to add a user to a project, they must first be invited.

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

api_instance = OpenapiClient::InvitationsApi.new
project_id = TODO # String | Project UUID
invitation = OpenapiClient::InvitationInput.new({invitee: 'invitee_example'}) # InvitationInput | Invitation to create

begin
  # Create an invitation for a project
  result = api_instance.create_project_invitation(project_id, invitation)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->create_project_invitation: #{e}"
end
```

#### Using the create_project_invitation_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Invitation>, Integer, Hash)> create_project_invitation_with_http_info(project_id, invitation)

```ruby
begin
  # Create an invitation for a project
  data, status_code, headers = api_instance.create_project_invitation_with_http_info(project_id, invitation)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Invitation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->create_project_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | Project UUID |  |
| **invitation** | [**InvitationInput**](InvitationInput.md) | Invitation to create |  |

### Return type

[**Invitation**](Invitation.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## decline_invitation

> decline_invitation(id)

Decline an invitation

Decline an invitation.

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

api_instance = OpenapiClient::InvitationsApi.new
id = TODO # String | Invitation UUID

begin
  # Decline an invitation
  api_instance.decline_invitation(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->decline_invitation: #{e}"
end
```

#### Using the decline_invitation_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> decline_invitation_with_http_info(id)

```ruby
begin
  # Decline an invitation
  data, status_code, headers = api_instance.decline_invitation_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->decline_invitation_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Invitation UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_invitation_by_id

> <Invitation> find_invitation_by_id(id, opts)

View an invitation

Returns a single invitation. (It include the `invitable` to maintain backward compatibility but will be removed soon)

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

api_instance = OpenapiClient::InvitationsApi.new
id = TODO # String | Invitation UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # View an invitation
  result = api_instance.find_invitation_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->find_invitation_by_id: #{e}"
end
```

#### Using the find_invitation_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Invitation>, Integer, Hash)> find_invitation_by_id_with_http_info(id, opts)

```ruby
begin
  # View an invitation
  data, status_code, headers = api_instance.find_invitation_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Invitation>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->find_invitation_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Invitation UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Invitation**](Invitation.md)

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

api_instance = OpenapiClient::InvitationsApi.new
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
  puts "Error when calling InvitationsApi->find_invitations: #{e}"
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
  puts "Error when calling InvitationsApi->find_invitations_with_http_info: #{e}"
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


## find_organization_invitations

> <InvitationList> find_organization_invitations(id, opts)

Retrieve organization invitations

Returns all invitations in an organization.

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

api_instance = OpenapiClient::InvitationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve organization invitations
  result = api_instance.find_organization_invitations(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->find_organization_invitations: #{e}"
end
```

#### Using the find_organization_invitations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InvitationList>, Integer, Hash)> find_organization_invitations_with_http_info(id, opts)

```ruby
begin
  # Retrieve organization invitations
  data, status_code, headers = api_instance.find_organization_invitations_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InvitationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->find_organization_invitations_with_http_info: #{e}"
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

[**InvitationList**](InvitationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_invitations

> <InvitationList> find_project_invitations(project_id, opts)

Retrieve project invitations

Returns all invitations in a project.

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

api_instance = OpenapiClient::InvitationsApi.new
project_id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve project invitations
  result = api_instance.find_project_invitations(project_id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->find_project_invitations: #{e}"
end
```

#### Using the find_project_invitations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InvitationList>, Integer, Hash)> find_project_invitations_with_http_info(project_id, opts)

```ruby
begin
  # Retrieve project invitations
  data, status_code, headers = api_instance.find_project_invitations_with_http_info(project_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InvitationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling InvitationsApi->find_project_invitations_with_http_info: #{e}"
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

[**InvitationList**](InvitationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

