# OpenapiClient::ConnectionsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**create_connection_port_virtual_circuit**](ConnectionsApi.md#create_connection_port_virtual_circuit) | **POST** /connections/{connection_id}/ports/{port_id}/virtual-circuits | Create a new Virtual Circuit |
| [**create_organization_interconnection**](ConnectionsApi.md#create_organization_interconnection) | **POST** /organizations/{organization_id}/connections | Request a new connection for the organization |
| [**create_project_interconnection**](ConnectionsApi.md#create_project_interconnection) | **POST** /projects/{project_id}/connections | Request a new connection for the project&#39;s organization |
| [**delete_interconnection**](ConnectionsApi.md#delete_interconnection) | **DELETE** /connections/{connection_id} | Delete connection |
| [**delete_virtual_circuit**](ConnectionsApi.md#delete_virtual_circuit) | **DELETE** /virtual-circuits/{id} | Delete a virtual circuit |
| [**find_connection_events**](ConnectionsApi.md#find_connection_events) | **GET** /connections/{connection_id}/events | Retrieve connection events |
| [**find_connection_port_events**](ConnectionsApi.md#find_connection_port_events) | **GET** /connections/{connection_id}/ports/{id}/events | Retrieve connection port events |
| [**find_virtual_circuit_events**](ConnectionsApi.md#find_virtual_circuit_events) | **GET** /virtual-circuit/{id}/events | Retrieve connection events |
| [**get_connection_port**](ConnectionsApi.md#get_connection_port) | **GET** /connections/{connection_id}/ports/{id} | Get a connection port |
| [**get_interconnection**](ConnectionsApi.md#get_interconnection) | **GET** /connections/{connection_id} | Get connection |
| [**get_virtual_circuit**](ConnectionsApi.md#get_virtual_circuit) | **GET** /virtual-circuits/{id} | Get a virtual circuit |
| [**list_connection_port_virtual_circuits**](ConnectionsApi.md#list_connection_port_virtual_circuits) | **GET** /connections/{connection_id}/ports/{port_id}/virtual-circuits | List a connection port&#39;s virtual circuits |
| [**list_connection_ports**](ConnectionsApi.md#list_connection_ports) | **GET** /connections/{connection_id}/ports | List a connection&#39;s ports |
| [**organization_list_interconnections**](ConnectionsApi.md#organization_list_interconnections) | **GET** /organizations/{organization_id}/connections | List organization connections |
| [**project_list_interconnections**](ConnectionsApi.md#project_list_interconnections) | **GET** /projects/{project_id}/connections | List project connections |
| [**update_interconnection**](ConnectionsApi.md#update_interconnection) | **PUT** /connections/{connection_id} | Update connection |
| [**update_virtual_circuit**](ConnectionsApi.md#update_virtual_circuit) | **PUT** /virtual-circuits/{id} | Update a virtual circuit |


## create_connection_port_virtual_circuit

> <VirtualCircuitList> create_connection_port_virtual_circuit(connection_id, port_id, virtual_circuit)

Create a new Virtual Circuit

Create a new Virtual Circuit on a dedicated connection using a Virtual Network record and an NNI VLAN value.

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | UUID of the connection
port_id = TODO # String | UUID of the connection port
virtual_circuit = OpenapiClient::VirtualCircuitCreateInput.new # VirtualCircuitCreateInput | Virtual Circuit details

begin
  # Create a new Virtual Circuit
  result = api_instance.create_connection_port_virtual_circuit(connection_id, port_id, virtual_circuit)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->create_connection_port_virtual_circuit: #{e}"
end
```

#### Using the create_connection_port_virtual_circuit_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualCircuitList>, Integer, Hash)> create_connection_port_virtual_circuit_with_http_info(connection_id, port_id, virtual_circuit)

```ruby
begin
  # Create a new Virtual Circuit
  data, status_code, headers = api_instance.create_connection_port_virtual_circuit_with_http_info(connection_id, port_id, virtual_circuit)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualCircuitList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->create_connection_port_virtual_circuit_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | UUID of the connection |  |
| **port_id** | [**String**](.md) | UUID of the connection port |  |
| **virtual_circuit** | [**VirtualCircuitCreateInput**](VirtualCircuitCreateInput.md) | Virtual Circuit details |  |

### Return type

[**VirtualCircuitList**](VirtualCircuitList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_organization_interconnection

> <Interconnection> create_organization_interconnection(organization_id, connection)

Request a new connection for the organization

Creates a new connection request. A Project ID must be specified in the request body for connections on shared ports.

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

api_instance = OpenapiClient::ConnectionsApi.new
organization_id = TODO # String | UUID of the organization
connection = OpenapiClient::InterconnectionCreateInput.new({name: 'name_example', facility: 'facility_example', type: 'type_example', redundancy: 'redundancy_example'}) # InterconnectionCreateInput | Connection details

begin
  # Request a new connection for the organization
  result = api_instance.create_organization_interconnection(organization_id, connection)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->create_organization_interconnection: #{e}"
end
```

#### Using the create_organization_interconnection_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Interconnection>, Integer, Hash)> create_organization_interconnection_with_http_info(organization_id, connection)

```ruby
begin
  # Request a new connection for the organization
  data, status_code, headers = api_instance.create_organization_interconnection_with_http_info(organization_id, connection)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Interconnection>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->create_organization_interconnection_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | [**String**](.md) | UUID of the organization |  |
| **connection** | [**InterconnectionCreateInput**](InterconnectionCreateInput.md) | Connection details |  |

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## create_project_interconnection

> <Interconnection> create_project_interconnection(project_id, connection)

Request a new connection for the project's organization

Creates a new connection request

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

api_instance = OpenapiClient::ConnectionsApi.new
project_id = TODO # String | UUID of the project
connection = OpenapiClient::InterconnectionCreateInput.new({name: 'name_example', facility: 'facility_example', type: 'type_example', redundancy: 'redundancy_example'}) # InterconnectionCreateInput | Connection details

begin
  # Request a new connection for the project's organization
  result = api_instance.create_project_interconnection(project_id, connection)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->create_project_interconnection: #{e}"
end
```

#### Using the create_project_interconnection_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Interconnection>, Integer, Hash)> create_project_interconnection_with_http_info(project_id, connection)

```ruby
begin
  # Request a new connection for the project's organization
  data, status_code, headers = api_instance.create_project_interconnection_with_http_info(project_id, connection)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Interconnection>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->create_project_interconnection_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | UUID of the project |  |
| **connection** | [**InterconnectionCreateInput**](InterconnectionCreateInput.md) | Connection details |  |

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_interconnection

> <Interconnection> delete_interconnection(connection_id)

Delete connection

Delete a connection, its associated ports and virtual circuits.

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | Connection UUID

begin
  # Delete connection
  result = api_instance.delete_interconnection(connection_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->delete_interconnection: #{e}"
end
```

#### Using the delete_interconnection_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Interconnection>, Integer, Hash)> delete_interconnection_with_http_info(connection_id)

```ruby
begin
  # Delete connection
  data, status_code, headers = api_instance.delete_interconnection_with_http_info(connection_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Interconnection>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->delete_interconnection_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | Connection UUID |  |

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## delete_virtual_circuit

> <VirtualCircuit> delete_virtual_circuit(id)

Delete a virtual circuit

Delete a virtual circuit from a dedicated port.

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

api_instance = OpenapiClient::ConnectionsApi.new
id = TODO # String | Virtual Circuit UUID

begin
  # Delete a virtual circuit
  result = api_instance.delete_virtual_circuit(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->delete_virtual_circuit: #{e}"
end
```

#### Using the delete_virtual_circuit_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualCircuit>, Integer, Hash)> delete_virtual_circuit_with_http_info(id)

```ruby
begin
  # Delete a virtual circuit
  data, status_code, headers = api_instance.delete_virtual_circuit_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualCircuit>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->delete_virtual_circuit_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Circuit UUID |  |

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


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

api_instance = OpenapiClient::ConnectionsApi.new
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
  puts "Error when calling ConnectionsApi->find_connection_events: #{e}"
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
  puts "Error when calling ConnectionsApi->find_connection_events_with_http_info: #{e}"
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

api_instance = OpenapiClient::ConnectionsApi.new
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
  puts "Error when calling ConnectionsApi->find_connection_port_events: #{e}"
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
  puts "Error when calling ConnectionsApi->find_connection_port_events_with_http_info: #{e}"
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

api_instance = OpenapiClient::ConnectionsApi.new
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
  puts "Error when calling ConnectionsApi->find_virtual_circuit_events: #{e}"
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
  puts "Error when calling ConnectionsApi->find_virtual_circuit_events_with_http_info: #{e}"
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


## get_connection_port

> <InterconnectionPort> get_connection_port(connection_id, id)

Get a connection port

Get the details of an connection port.

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | UUID of the connection
id = TODO # String | Port UUID

begin
  # Get a connection port
  result = api_instance.get_connection_port(connection_id, id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->get_connection_port: #{e}"
end
```

#### Using the get_connection_port_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InterconnectionPort>, Integer, Hash)> get_connection_port_with_http_info(connection_id, id)

```ruby
begin
  # Get a connection port
  data, status_code, headers = api_instance.get_connection_port_with_http_info(connection_id, id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InterconnectionPort>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->get_connection_port_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | UUID of the connection |  |
| **id** | [**String**](.md) | Port UUID |  |

### Return type

[**InterconnectionPort**](InterconnectionPort.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_interconnection

> <Interconnection> get_interconnection(connection_id)

Get connection

Get the details of a connection

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | Connection UUID

begin
  # Get connection
  result = api_instance.get_interconnection(connection_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->get_interconnection: #{e}"
end
```

#### Using the get_interconnection_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Interconnection>, Integer, Hash)> get_interconnection_with_http_info(connection_id)

```ruby
begin
  # Get connection
  data, status_code, headers = api_instance.get_interconnection_with_http_info(connection_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Interconnection>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->get_interconnection_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | Connection UUID |  |

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_virtual_circuit

> <VirtualCircuit> get_virtual_circuit(id)

Get a virtual circuit

Get the details of a virtual circuit

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

api_instance = OpenapiClient::ConnectionsApi.new
id = TODO # String | Virtual Circuit UUID

begin
  # Get a virtual circuit
  result = api_instance.get_virtual_circuit(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->get_virtual_circuit: #{e}"
end
```

#### Using the get_virtual_circuit_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualCircuit>, Integer, Hash)> get_virtual_circuit_with_http_info(id)

```ruby
begin
  # Get a virtual circuit
  data, status_code, headers = api_instance.get_virtual_circuit_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualCircuit>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->get_virtual_circuit_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Circuit UUID |  |

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_connection_port_virtual_circuits

> <VirtualCircuitList> list_connection_port_virtual_circuits(connection_id, port_id)

List a connection port's virtual circuits

List the virtual circuit record(s) associatiated with a particular connection port.

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | UUID of the connection
port_id = TODO # String | UUID of the connection port

begin
  # List a connection port's virtual circuits
  result = api_instance.list_connection_port_virtual_circuits(connection_id, port_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->list_connection_port_virtual_circuits: #{e}"
end
```

#### Using the list_connection_port_virtual_circuits_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualCircuitList>, Integer, Hash)> list_connection_port_virtual_circuits_with_http_info(connection_id, port_id)

```ruby
begin
  # List a connection port's virtual circuits
  data, status_code, headers = api_instance.list_connection_port_virtual_circuits_with_http_info(connection_id, port_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualCircuitList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->list_connection_port_virtual_circuits_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | UUID of the connection |  |
| **port_id** | [**String**](.md) | UUID of the connection port |  |

### Return type

[**VirtualCircuitList**](VirtualCircuitList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## list_connection_ports

> <InterconnectionPortList> list_connection_ports(connection_id)

List a connection's ports

List the ports associated to an connection.

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | UUID of the connection

begin
  # List a connection's ports
  result = api_instance.list_connection_ports(connection_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->list_connection_ports: #{e}"
end
```

#### Using the list_connection_ports_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InterconnectionPortList>, Integer, Hash)> list_connection_ports_with_http_info(connection_id)

```ruby
begin
  # List a connection's ports
  data, status_code, headers = api_instance.list_connection_ports_with_http_info(connection_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InterconnectionPortList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->list_connection_ports_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | UUID of the connection |  |

### Return type

[**InterconnectionPortList**](InterconnectionPortList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## organization_list_interconnections

> <InterconnectionList> organization_list_interconnections(organization_id)

List organization connections

List the connections belonging to the organization

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

api_instance = OpenapiClient::ConnectionsApi.new
organization_id = TODO # String | UUID of the organization

begin
  # List organization connections
  result = api_instance.organization_list_interconnections(organization_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->organization_list_interconnections: #{e}"
end
```

#### Using the organization_list_interconnections_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InterconnectionList>, Integer, Hash)> organization_list_interconnections_with_http_info(organization_id)

```ruby
begin
  # List organization connections
  data, status_code, headers = api_instance.organization_list_interconnections_with_http_info(organization_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InterconnectionList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->organization_list_interconnections_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **organization_id** | [**String**](.md) | UUID of the organization |  |

### Return type

[**InterconnectionList**](InterconnectionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## project_list_interconnections

> <InterconnectionList> project_list_interconnections(project_id)

List project connections

List the connections belonging to the project

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

api_instance = OpenapiClient::ConnectionsApi.new
project_id = TODO # String | UUID of the project

begin
  # List project connections
  result = api_instance.project_list_interconnections(project_id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->project_list_interconnections: #{e}"
end
```

#### Using the project_list_interconnections_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InterconnectionList>, Integer, Hash)> project_list_interconnections_with_http_info(project_id)

```ruby
begin
  # List project connections
  data, status_code, headers = api_instance.project_list_interconnections_with_http_info(project_id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InterconnectionList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->project_list_interconnections_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **project_id** | [**String**](.md) | UUID of the project |  |

### Return type

[**InterconnectionList**](InterconnectionList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## update_interconnection

> <Interconnection> update_interconnection(connection_id, connection)

Update connection

Update the details of a connection

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

api_instance = OpenapiClient::ConnectionsApi.new
connection_id = TODO # String | Connection UUID
connection = OpenapiClient::InterconnectionUpdateInput.new # InterconnectionUpdateInput | Updated connection details

begin
  # Update connection
  result = api_instance.update_interconnection(connection_id, connection)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->update_interconnection: #{e}"
end
```

#### Using the update_interconnection_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Interconnection>, Integer, Hash)> update_interconnection_with_http_info(connection_id, connection)

```ruby
begin
  # Update connection
  data, status_code, headers = api_instance.update_interconnection_with_http_info(connection_id, connection)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Interconnection>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->update_interconnection_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **connection_id** | [**String**](.md) | Connection UUID |  |
| **connection** | [**InterconnectionUpdateInput**](InterconnectionUpdateInput.md) | Updated connection details |  |

### Return type

[**Interconnection**](Interconnection.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## update_virtual_circuit

> <VirtualCircuit> update_virtual_circuit(id, virtual_circuit)

Update a virtual circuit

Update the details of a virtual circuit.

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

api_instance = OpenapiClient::ConnectionsApi.new
id = TODO # String | Virtual Circuit UUID
virtual_circuit = OpenapiClient::VirtualCircuitUpdateInput.new # VirtualCircuitUpdateInput | Updated Virtual Circuit details

begin
  # Update a virtual circuit
  result = api_instance.update_virtual_circuit(id, virtual_circuit)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->update_virtual_circuit: #{e}"
end
```

#### Using the update_virtual_circuit_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualCircuit>, Integer, Hash)> update_virtual_circuit_with_http_info(id, virtual_circuit)

```ruby
begin
  # Update a virtual circuit
  data, status_code, headers = api_instance.update_virtual_circuit_with_http_info(id, virtual_circuit)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualCircuit>
rescue OpenapiClient::ApiError => e
  puts "Error when calling ConnectionsApi->update_virtual_circuit_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Circuit UUID |  |
| **virtual_circuit** | [**VirtualCircuitUpdateInput**](VirtualCircuitUpdateInput.md) | Updated Virtual Circuit details |  |

### Return type

[**VirtualCircuit**](VirtualCircuit.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

