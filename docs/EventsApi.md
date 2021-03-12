# OpenapiClient::EventsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**find_connection_events**](EventsApi.md#find_connection_events) | **GET** /connections/{connection_id}/events | Retrieve connection events |
| [**find_connection_port_events**](EventsApi.md#find_connection_port_events) | **GET** /connections/{connection_id}/ports/{id}/events | Retrieve connection port events |
| [**find_device_events**](EventsApi.md#find_device_events) | **GET** /devices/{id}/events | Retrieve device&#39;s events |
| [**find_event_by_id**](EventsApi.md#find_event_by_id) | **GET** /events/{id} | Retrieve an event |
| [**find_events**](EventsApi.md#find_events) | **GET** /events | Retrieve current user&#39;s events |
| [**find_organization_events**](EventsApi.md#find_organization_events) | **GET** /organizations/{id}/events | Retrieve organization&#39;s events |
| [**find_project_events**](EventsApi.md#find_project_events) | **GET** /projects/{id}/events | Retrieve project&#39;s events |
| [**find_virtual_circuit_events**](EventsApi.md#find_virtual_circuit_events) | **GET** /virtual-circuit/{id}/events | Retrieve connection events |
| [**find_volume_events**](EventsApi.md#find_volume_events) | **GET** /volumes/{id}/events | Retrieve volume&#39;s events |


## find_connection_events

> <Event> find_connection_events(connection_id, opts)

Retrieve connection events

Returns a list of the connection events

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

api_instance = OpenapiClient::EventsApi.new
connection_id = TODO # String | Connection UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve connection events
  result = api_instance.find_connection_events(connection_id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_connection_events: #{e}"
end
```

#### Using the find_connection_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Event>, Integer, Hash)> find_connection_events_with_http_info(connection_id, opts)

```ruby
begin
  # Retrieve connection events
  data, status_code, headers = api_instance.find_connection_events_with_http_info(connection_id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Event>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_connection_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | Connection UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**Event**](Event.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_connection_port_events

> <Event> find_connection_port_events(connection_id, id, opts)

Retrieve connection port events

Returns a list of the connection port events

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

api_instance = OpenapiClient::EventsApi.new
connection_id = TODO # String | Connection UUID
id = TODO # String | Connection Port UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve connection port events
  result = api_instance.find_connection_port_events(connection_id, id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_connection_port_events: #{e}"
end
```

#### Using the find_connection_port_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Event>, Integer, Hash)> find_connection_port_events_with_http_info(connection_id, id, opts)

```ruby
begin
  # Retrieve connection port events
  data, status_code, headers = api_instance.find_connection_port_events_with_http_info(connection_id, id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Event>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_connection_port_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | Connection UUID |  |
| **id** | [**String**](.md) | Connection Port UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**Event**](Event.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_device_events

> <EventList> find_device_events(id, opts)

Retrieve device's events

Returns a list of events pertaining to a specific device

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

api_instance = OpenapiClient::EventsApi.new
id = TODO # String | Device UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve device's events
  result = api_instance.find_device_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_device_events: #{e}"
end
```

#### Using the find_device_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_device_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve device's events
  data, status_code, headers = api_instance.find_device_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_device_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Device UUID |  |
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


## find_event_by_id

> <Event> find_event_by_id(id, opts)

Retrieve an event

Returns a single event if the user has access

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

api_instance = OpenapiClient::EventsApi.new
id = TODO # String | Event UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve an event
  result = api_instance.find_event_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_event_by_id: #{e}"
end
```

#### Using the find_event_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Event>, Integer, Hash)> find_event_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve an event
  data, status_code, headers = api_instance.find_event_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Event>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_event_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Event UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Event**](Event.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_events

> <EventList> find_events(opts)

Retrieve current user's events

Returns a list of the current user’s events

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

api_instance = OpenapiClient::EventsApi.new
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve current user's events
  result = api_instance.find_events(opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_events: #{e}"
end
```

#### Using the find_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_events_with_http_info(opts)

```ruby
begin
  # Retrieve current user's events
  data, status_code, headers = api_instance.find_events_with_http_info(opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_events_with_http_info: #{e}"
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

[**EventList**](EventList.md)

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

api_instance = OpenapiClient::EventsApi.new
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
  puts "Error when calling EventsApi->find_organization_events: #{e}"
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
  puts "Error when calling EventsApi->find_organization_events_with_http_info: #{e}"
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


## find_project_events

> <EventList> find_project_events(id, opts)

Retrieve project's events

Returns a list of events for a single project

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

api_instance = OpenapiClient::EventsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve project's events
  result = api_instance.find_project_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_project_events: #{e}"
end
```

#### Using the find_project_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_project_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve project's events
  data, status_code, headers = api_instance.find_project_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_project_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
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


## find_virtual_circuit_events

> <Event> find_virtual_circuit_events(id, opts)

Retrieve connection events

Returns a list of the virtual circuit events

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

api_instance = OpenapiClient::EventsApi.new
id = TODO # String | Virtual Circuit UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve connection events
  result = api_instance.find_virtual_circuit_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_virtual_circuit_events: #{e}"
end
```

#### Using the find_virtual_circuit_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Event>, Integer, Hash)> find_virtual_circuit_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve connection events
  data, status_code, headers = api_instance.find_virtual_circuit_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Event>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_virtual_circuit_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Circuit UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |
| **page** | **Integer** | Page to return | [optional][default to 1] |
| **per_page** | **Integer** | Items returned per page | [optional][default to 10] |

### Return type

[**Event**](Event.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_volume_events

> <EventList> find_volume_events(id, opts)

Retrieve volume's events

Returns a list of the current volume’s events

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

api_instance = OpenapiClient::EventsApi.new
id = TODO # String | Volume UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'], # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
  page: 56, # Integer | Page to return
  per_page: 56 # Integer | Items returned per page
}

begin
  # Retrieve volume's events
  result = api_instance.find_volume_events(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_volume_events: #{e}"
end
```

#### Using the find_volume_events_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<EventList>, Integer, Hash)> find_volume_events_with_http_info(id, opts)

```ruby
begin
  # Retrieve volume's events
  data, status_code, headers = api_instance.find_volume_events_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <EventList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling EventsApi->find_volume_events_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Volume UUID |  |
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

