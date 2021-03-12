# OpenapiClient::OrganizationsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_organization**](OrganizationsApi.md#create_organization) | **POST** /organizations | Create an organization |
| [**create_organization_invitation**](OrganizationsApi.md#create_organization_invitation) | **POST** /organizations/{id}/invitations | Create an invitation for an organization |
| [**create_organization_project**](OrganizationsApi.md#create_organization_project) | **POST** /organizations/{id}/projects | Create a project for the organization |
| [**create_payment_method**](OrganizationsApi.md#create_payment_method) | **POST** /organizations/{id}/payment-methods | Create a payment method for the given organization |
| [**delete_organization**](OrganizationsApi.md#delete_organization) | **DELETE** /organizations/{id} | Delete the organization |
| [**find_facilities_by_organization**](OrganizationsApi.md#find_facilities_by_organization) | **GET** /organizations/{id}/facilities | Retrieve all facilities visible by the organization |
| [**find_operating_systems_by_organization**](OrganizationsApi.md#find_operating_systems_by_organization) | **GET** /organizations/{id}/operating-systems | Retrieve all operating systems visible by the organization |
| [**find_organization_by_id**](OrganizationsApi.md#find_organization_by_id) | **GET** /organizations/{id} | Retrieve an organization&#39;s details |
| [**find_organization_customdata**](OrganizationsApi.md#find_organization_customdata) | **GET** /organizations/{id}/customdata | Retrieve the custom metadata of an organization |
| [**find_organization_devices**](OrganizationsApi.md#find_organization_devices) | **GET** /organizations/{id}/devices | Retrieve all devices of an organization |
| [**find_organization_events**](OrganizationsApi.md#find_organization_events) | **GET** /organizations/{id}/events | Retrieve organization&#39;s events |
| [**find_organization_invitations**](OrganizationsApi.md#find_organization_invitations) | **GET** /organizations/{id}/invitations | Retrieve organization invitations |
| [**find_organization_payment_methods**](OrganizationsApi.md#find_organization_payment_methods) | **GET** /organizations/{id}/payment-methods | Retrieve all payment methods of an organization |
| [**find_organization_projects**](OrganizationsApi.md#find_organization_projects) | **GET** /organizations/{id}/projects | Retrieve all projects of an organization |
| [**find_organization_transfers**](OrganizationsApi.md#find_organization_transfers) | **GET** /organizations/{id}/transfers | Retrieve all project transfer requests from or to an organization |
| [**find_organizations**](OrganizationsApi.md#find_organizations) | **GET** /organizations | Retrieve all organizations |
| [**find_plans_by_organization**](OrganizationsApi.md#find_plans_by_organization) | **GET** /organizations/{id}/plans | Retrieve all plans visible by the organization |
| [**update_organization**](OrganizationsApi.md#update_organization) | **PUT** /organizations/{id} | Update the organization |


## create_organization

> <Organization> create_organization(organization)

Create an organization

Creates an organization.

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

api_instance = OpenapiClient::OrganizationsApi.new
organization = OpenapiClient::OrganizationInput.new # OrganizationInput | Organization to create

begin
  # Create an organization
  result = api_instance.create_organization(organization)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->create_organization: #{e}"
end
```

#### Using the create_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Organization>, Integer, Hash)> create_organization_with_http_info(organization)

```ruby
begin
  # Create an organization
  data, status_code, headers = api_instance.create_organization_with_http_info(organization)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Organization>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->create_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization** | [**OrganizationInput**](OrganizationInput.md) | Organization to create |  |

### Return type

[**Organization**](Organization.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
invitation = OpenapiClient::InvitationInput.new({invitee: 'invitee_example'}) # InvitationInput | Invitation to create

begin
  # Create an invitation for an organization
  result = api_instance.create_organization_invitation(id, invitation)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->create_organization_invitation: #{e}"
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
  puts "Error when calling OrganizationsApi->create_organization_invitation_with_http_info: #{e}"
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


## create_organization_project

> <Project> create_organization_project(id, project)

Create a project for the organization

Creates a new project for the organization

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
project = OpenapiClient::ProjectCreateInput.new({name: 'name_example'}) # ProjectCreateInput | Project to create

begin
  # Create a project for the organization
  result = api_instance.create_organization_project(id, project)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->create_organization_project: #{e}"
end
```

#### Using the create_organization_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Project>, Integer, Hash)> create_organization_project_with_http_info(id, project)

```ruby
begin
  # Create a project for the organization
  data, status_code, headers = api_instance.create_organization_project_with_http_info(id, project)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Project>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->create_organization_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **project** | [**ProjectCreateInput**](ProjectCreateInput.md) | Project to create |  |

### Return type

[**Project**](Project.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
payment_method = OpenapiClient::PaymentMethodCreateInput.new({name: 'name_example', nonce: 'nonce_example'}) # PaymentMethodCreateInput | Payment Method to create

begin
  # Create a payment method for the given organization
  result = api_instance.create_payment_method(id, payment_method)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->create_payment_method: #{e}"
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
  puts "Error when calling OrganizationsApi->create_payment_method_with_http_info: #{e}"
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


## delete_organization

> delete_organization(id)

Delete the organization

Deletes the organization.

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID

begin
  # Delete the organization
  api_instance.delete_organization(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->delete_organization: #{e}"
end
```

#### Using the delete_organization_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_organization_with_http_info(id)

```ruby
begin
  # Delete the organization
  data, status_code, headers = api_instance.delete_organization_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->delete_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_facilities_by_organization

> <FacilityList> find_facilities_by_organization(id, opts)

Retrieve all facilities visible by the organization

Returns a listing of available datacenters for the given organization

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all facilities visible by the organization
  result = api_instance.find_facilities_by_organization(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_facilities_by_organization: #{e}"
end
```

#### Using the find_facilities_by_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<FacilityList>, Integer, Hash)> find_facilities_by_organization_with_http_info(id, opts)

```ruby
begin
  # Retrieve all facilities visible by the organization
  data, status_code, headers = api_instance.find_facilities_by_organization_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <FacilityList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_facilities_by_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**FacilityList**](FacilityList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_operating_systems_by_organization

> <Array<OperatingSystem>> find_operating_systems_by_organization(id, opts)

Retrieve all operating systems visible by the organization

Returns a listing of available operating systems for the given organization

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all operating systems visible by the organization
  result = api_instance.find_operating_systems_by_organization(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_operating_systems_by_organization: #{e}"
end
```

#### Using the find_operating_systems_by_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Array<OperatingSystem>>, Integer, Hash)> find_operating_systems_by_organization_with_http_info(id, opts)

```ruby
begin
  # Retrieve all operating systems visible by the organization
  data, status_code, headers = api_instance.find_operating_systems_by_organization_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Array<OperatingSystem>>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_operating_systems_by_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Array&lt;OperatingSystem&gt;**](OperatingSystem.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organization_by_id

> <Organization> find_organization_by_id(id, opts)

Retrieve an organization's details

Returns a single organization's details, if the user is authorized to view it.

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve an organization's details
  result = api_instance.find_organization_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_by_id: #{e}"
end
```

#### Using the find_organization_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Organization>, Integer, Hash)> find_organization_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve an organization's details
  data, status_code, headers = api_instance.find_organization_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Organization>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Organization**](Organization.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organization_customdata

> find_organization_customdata(id)

Retrieve the custom metadata of an organization

Provides the custom metadata stored for this organization in json format

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID

begin
  # Retrieve the custom metadata of an organization
  api_instance.find_organization_customdata(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_customdata: #{e}"
end
```

#### Using the find_organization_customdata_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> find_organization_customdata_with_http_info(id)

```ruby
begin
  # Retrieve the custom metadata of an organization
  data, status_code, headers = api_instance.find_organization_customdata_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_customdata_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_organization_devices

> <DeviceList> find_organization_devices(id, opts)

Retrieve all devices of an organization

Provides a collection of devices for a given organization.

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all devices of an organization
  result = api_instance.find_organization_devices(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_devices: #{e}"
end
```

#### Using the find_organization_devices_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<DeviceList>, Integer, Hash)> find_organization_devices_with_http_info(id, opts)

```ruby
begin
  # Retrieve all devices of an organization
  data, status_code, headers = api_instance.find_organization_devices_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <DeviceList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_devices_with_http_info: #{e}"
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

[**DeviceList**](DeviceList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organization_events

> <EventList> find_organization_events(id, opts)

Retrieve organization's events

Returns a list of events for a single organization

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve organization's events
  result = api_instance.find_organization_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_events: #{e}"
end
```

#### Using the find_organization_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_organization_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve organization's events
  data, status_code, headers = api_instance.find_organization_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_events_with_http_info: #{e}"
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

[**EventList**](EventList.md)

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

api_instance = OpenapiClient::OrganizationsApi.new
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
  puts "Error when calling OrganizationsApi->find_organization_invitations: #{e}"
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
  puts "Error when calling OrganizationsApi->find_organization_invitations_with_http_info: #{e}"
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

api_instance = OpenapiClient::OrganizationsApi.new
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
  puts "Error when calling OrganizationsApi->find_organization_payment_methods: #{e}"
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
  puts "Error when calling OrganizationsApi->find_organization_payment_methods_with_http_info: #{e}"
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


## find_organization_projects

> <ProjectList> find_organization_projects(id, opts)

Retrieve all projects of an organization

Returns a collection of projects that belong to the organization.

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all projects of an organization
  result = api_instance.find_organization_projects(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_projects: #{e}"
end
```

#### Using the find_organization_projects_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<ProjectList>, Integer, Hash)> find_organization_projects_with_http_info(id, opts)

```ruby
begin
  # Retrieve all projects of an organization
  data, status_code, headers = api_instance.find_organization_projects_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <ProjectList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_projects_with_http_info: #{e}"
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

[**ProjectList**](ProjectList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organization_transfers

> <TransferRequestList> find_organization_transfers(id, opts)

Retrieve all project transfer requests from or to an organization

Provides a collection of project transfer requests from or to the organization.

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all project transfer requests from or to an organization
  result = api_instance.find_organization_transfers(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_transfers: #{e}"
end
```

#### Using the find_organization_transfers_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<TransferRequestList>, Integer, Hash)> find_organization_transfers_with_http_info(id, opts)

```ruby
begin
  # Retrieve all project transfer requests from or to an organization
  data, status_code, headers = api_instance.find_organization_transfers_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <TransferRequestList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organization_transfers_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**TransferRequestList**](TransferRequestList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_organizations

> <OrganizationList> find_organizations(opts)

Retrieve all organizations

Returns a list of organizations that are accessible to the current user.

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

api_instance = OpenapiClient::OrganizationsApi.new
opts = {
  personal: 'include', # String | Include, exclude or show only personal organizations.
  without_projects: 'include', # String | Include, exclude or show only organizations that have no projects.
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve all organizations
  result = api_instance.find_organizations(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organizations: #{e}"
end
```

#### Using the find_organizations_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<OrganizationList>, Integer, Hash)> find_organizations_with_http_info(opts)

```ruby
begin
  # Retrieve all organizations
  data, status_code, headers = api_instance.find_organizations_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <OrganizationList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_organizations_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **personal** | **String** | Include, exclude or show only personal organizations. | [optional] |
| **without_projects** | **String** | Include, exclude or show only organizations that have no projects. | [optional] |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**OrganizationList**](OrganizationList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_plans_by_organization

> <PlanList> find_plans_by_organization(id, opts)

Retrieve all plans visible by the organization

Returns a listing of available plans for the given organization

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all plans visible by the organization
  result = api_instance.find_plans_by_organization(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_plans_by_organization: #{e}"
end
```

#### Using the find_plans_by_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<PlanList>, Integer, Hash)> find_plans_by_organization_with_http_info(id, opts)

```ruby
begin
  # Retrieve all plans visible by the organization
  data, status_code, headers = api_instance.find_plans_by_organization_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <PlanList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->find_plans_by_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**PlanList**](PlanList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_organization

> <Organization> update_organization(id, organization)

Update the organization

Updates the organization.

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

api_instance = OpenapiClient::OrganizationsApi.new
id = TODO # String | Organization UUID
organization = OpenapiClient::OrganizationInput.new # OrganizationInput | Organization to update

begin
  # Update the organization
  result = api_instance.update_organization(id, organization)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->update_organization: #{e}"
end
```

#### Using the update_organization_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Organization>, Integer, Hash)> update_organization_with_http_info(id, organization)

```ruby
begin
  # Update the organization
  data, status_code, headers = api_instance.update_organization_with_http_info(id, organization)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Organization>
rescue OpenapiClient::ApiError => e
  puts "Error when calling OrganizationsApi->update_organization_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Organization UUID |  |
| **organization** | [**OrganizationInput**](OrganizationInput.md) | Organization to update |  |

### Return type

[**Organization**](Organization.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

