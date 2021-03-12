# OpenapiClient::BGPApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_bgp_session**](BGPApi.md#create_bgp_session) | **POST** /devices/{id}/bgp/sessions | Create a BGP session |
| [**delete_bgp_session**](BGPApi.md#delete_bgp_session) | **DELETE** /bgp/sessions/{id} | Delete the BGP session |
| [**find_bgp_config_by_project**](BGPApi.md#find_bgp_config_by_project) | **GET** /projects/{id}/bgp-config | Retrieve a bgp config |
| [**find_bgp_session_by_id**](BGPApi.md#find_bgp_session_by_id) | **GET** /bgp/sessions/{id} | Retrieve a BGP session |
| [**find_bgp_sessions**](BGPApi.md#find_bgp_sessions) | **GET** /devices/{id}/bgp/sessions | Retrieve all BGP sessions |
| [**find_project_bgp_sessions**](BGPApi.md#find_project_bgp_sessions) | **GET** /projects/{id}/bgp/sessions | Retrieve all BGP sessions for project |
| [**get_bgp_neighbor_data**](BGPApi.md#get_bgp_neighbor_data) | **GET** /devices/{id}/bgp/neighbors | Retrieve BGP neighbor data for this device |
| [**request_bgp_config**](BGPApi.md#request_bgp_config) | **POST** /projects/{id}/bgp-configs | Requesting bgp config |
| [**update_bgp_session**](BGPApi.md#update_bgp_session) | **PUT** /bgp/sessions/{id} | Update the BGP session |


## create_bgp_session

> <BgpSession> create_bgp_session(id, bgp_session)

Create a BGP session

Creates a BGP session.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | Device UUID
bgp_session = OpenapiClient::BGPSessionInput.new # BGPSessionInput | BGP session to create

begin
  # Create a BGP session
  result = api_instance.create_bgp_session(id, bgp_session)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->create_bgp_session: #{e}"
end
```

#### Using the create_bgp_session_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSession>, Integer, Hash)> create_bgp_session_with_http_info(id, bgp_session)

```ruby
begin
  # Create a BGP session
  data, status_code, headers = api_instance.create_bgp_session_with_http_info(id, bgp_session)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSession>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->create_bgp_session_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
| **bgp_session** | [**BGPSessionInput**](BGPSessionInput.md) | BGP session to create |  |

### Return type

[**BgpSession**](BgpSession.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_bgp_session

> delete_bgp_session(id)

Delete the BGP session

Deletes the BGP session.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | BGP session UUID

begin
  # Delete the BGP session
  api_instance.delete_bgp_session(id)
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->delete_bgp_session: #{e}"
end
```

#### Using the delete_bgp_session_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> delete_bgp_session_with_http_info(id)

```ruby
begin
  # Delete the BGP session
  data, status_code, headers = api_instance.delete_bgp_session_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->delete_bgp_session_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | BGP session UUID |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: Not defined


## find_bgp_config_by_project

> <BgpConfig> find_bgp_config_by_project(id, opts)

Retrieve a bgp config

Returns a bgp config

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a bgp config
  result = api_instance.find_bgp_config_by_project(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_bgp_config_by_project: #{e}"
end
```

#### Using the find_bgp_config_by_project_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpConfig>, Integer, Hash)> find_bgp_config_by_project_with_http_info(id, opts)

```ruby
begin
  # Retrieve a bgp config
  data, status_code, headers = api_instance.find_bgp_config_by_project_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpConfig>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_bgp_config_by_project_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**BgpConfig**](BgpConfig.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_bgp_session_by_id

> <BgpSession> find_bgp_session_by_id(id, opts)

Retrieve a BGP session

Returns a BGP session

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | BGP session UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a BGP session
  result = api_instance.find_bgp_session_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_bgp_session_by_id: #{e}"
end
```

#### Using the find_bgp_session_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSession>, Integer, Hash)> find_bgp_session_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a BGP session
  data, status_code, headers = api_instance.find_bgp_session_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSession>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_bgp_session_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | BGP session UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**BgpSession**](BgpSession.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_bgp_sessions

> <BgpSessionList> find_bgp_sessions(id)

Retrieve all BGP sessions

Provides a listing of available BGP sessions for the device.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | Device UUID

begin
  # Retrieve all BGP sessions
  result = api_instance.find_bgp_sessions(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_bgp_sessions: #{e}"
end
```

#### Using the find_bgp_sessions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSessionList>, Integer, Hash)> find_bgp_sessions_with_http_info(id)

```ruby
begin
  # Retrieve all BGP sessions
  data, status_code, headers = api_instance.find_bgp_sessions_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSessionList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_bgp_sessions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |

### Return type

[**BgpSessionList**](BgpSessionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_project_bgp_sessions

> <BgpSessionList> find_project_bgp_sessions(id)

Retrieve all BGP sessions for project

Provides a listing of available BGP sessions for the project.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | Project UUID

begin
  # Retrieve all BGP sessions for project
  result = api_instance.find_project_bgp_sessions(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_project_bgp_sessions: #{e}"
end
```

#### Using the find_project_bgp_sessions_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSessionList>, Integer, Hash)> find_project_bgp_sessions_with_http_info(id)

```ruby
begin
  # Retrieve all BGP sessions for project
  data, status_code, headers = api_instance.find_project_bgp_sessions_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSessionList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->find_project_bgp_sessions_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |

### Return type

[**BgpSessionList**](BgpSessionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_bgp_neighbor_data

> <BgpSessionNeighbors> get_bgp_neighbor_data(id)

Retrieve BGP neighbor data for this device

Provides a summary of the BGP neighbor data associated to the BGP sessions for this device.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | Device UUID

begin
  # Retrieve BGP neighbor data for this device
  result = api_instance.get_bgp_neighbor_data(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->get_bgp_neighbor_data: #{e}"
end
```

#### Using the get_bgp_neighbor_data_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<BgpSessionNeighbors>, Integer, Hash)> get_bgp_neighbor_data_with_http_info(id)

```ruby
begin
  # Retrieve BGP neighbor data for this device
  data, status_code, headers = api_instance.get_bgp_neighbor_data_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <BgpSessionNeighbors>
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->get_bgp_neighbor_data_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |

### Return type

[**BgpSessionNeighbors**](BgpSessionNeighbors.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## request_bgp_config

> request_bgp_config(id, bgp_config_request)

Requesting bgp config

Requests to enable bgp configuration for a project.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | Project UUID
bgp_config_request = OpenapiClient::BgpConfigRequestInput.new({deployment_type: 'deployment_type_example', asn: 37}) # BgpConfigRequestInput | BGP config Request to create

begin
  # Requesting bgp config
  api_instance.request_bgp_config(id, bgp_config_request)
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->request_bgp_config: #{e}"
end
```

#### Using the request_bgp_config_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> request_bgp_config_with_http_info(id, bgp_config_request)

```ruby
begin
  # Requesting bgp config
  data, status_code, headers = api_instance.request_bgp_config_with_http_info(id, bgp_config_request)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->request_bgp_config_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **bgp_config_request** | [**BgpConfigRequestInput**](BgpConfigRequestInput.md) | BGP config Request to create |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined


## update_bgp_session

> update_bgp_session(id, default_route)

Update the BGP session

Updates the BGP session by either enabling or disabling the default route functionality.

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

api_instance = OpenapiClient::BGPApi.new
id = TODO # String | BGP session UUID
default_route = true # Boolean | Default route

begin
  # Update the BGP session
  api_instance.update_bgp_session(id, default_route)
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->update_bgp_session: #{e}"
end
```

#### Using the update_bgp_session_with_http_info variant

This returns an Array which contains the response data (`nil` in this case), status code and headers.

> <Array(nil, Integer, Hash)> update_bgp_session_with_http_info(id, default_route)

```ruby
begin
  # Update the BGP session
  data, status_code, headers = api_instance.update_bgp_session_with_http_info(id, default_route)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => nil
rescue OpenapiClient::ApiError => e
  puts "Error when calling BGPApi->update_bgp_session_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | BGP session UUID |  |
| **default_route** | **Boolean** | Default route |  |

### Return type

nil (empty response body)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: Not defined

