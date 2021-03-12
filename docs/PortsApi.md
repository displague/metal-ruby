# OpenapiClient::PortsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**assign_native_vlan**](PortsApi.md#assign_native_vlan) | **POST** /ports/{id}/native-vlan | Assign a native VLAN |
| [**assign_port**](PortsApi.md#assign_port) | **POST** /ports/{id}/assign | Assign a port to virtual network |
| [**bond_port**](PortsApi.md#bond_port) | **POST** /ports/{id}/bond | Enabling bonding |
| [**convert_layer2**](PortsApi.md#convert_layer2) | **POST** /ports/{id}/convert/layer-2 | Convert to Layer 2 |
| [**convert_layer3**](PortsApi.md#convert_layer3) | **POST** /ports/{id}/convert/layer-3 | Convert to Layer 3 |
| [**delete_native_vlan**](PortsApi.md#delete_native_vlan) | **DELETE** /ports/{id}/native-vlan | Remove native VLAN |
| [**disbond_port**](PortsApi.md#disbond_port) | **POST** /ports/{id}/disbond | Disabling bonding |
| [**find_port_by_id**](PortsApi.md#find_port_by_id) | **GET** /ports/{id} | Retrieve a port |
| [**unassign_port**](PortsApi.md#unassign_port) | **POST** /ports/{id}/unassign | Unassign a port |


## assign_native_vlan

> <Port> assign_native_vlan(id, vnid)

Assign a native VLAN

Assigns a virtual network to this port as a \"native VLAN\"

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
vnid = 'vnid_example' # String | UUID or VNID of the virtual network to assign

begin
  # Assign a native VLAN
  result = api_instance.assign_native_vlan(id, vnid)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->assign_native_vlan: #{e}"
end
```

#### Using the assign_native_vlan_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> assign_native_vlan_with_http_info(id, vnid)

```ruby
begin
  # Assign a native VLAN
  data, status_code, headers = api_instance.assign_native_vlan_with_http_info(id, vnid)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->assign_native_vlan_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **vnid** | **String** | UUID or VNID of the virtual network to assign |  |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## assign_port

> <Port> assign_port(id, vnid)

Assign a port to virtual network

Assign a port for a hardware to virtual network.

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
vnid = OpenapiClient::PortAssignInput.new # PortAssignInput | Virtual Network ID

begin
  # Assign a port to virtual network
  result = api_instance.assign_port(id, vnid)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->assign_port: #{e}"
end
```

#### Using the assign_port_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> assign_port_with_http_info(id, vnid)

```ruby
begin
  # Assign a port to virtual network
  data, status_code, headers = api_instance.assign_port_with_http_info(id, vnid)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->assign_port_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **vnid** | [**PortAssignInput**](PortAssignInput.md) | Virtual Network ID |  |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## bond_port

> <Port> bond_port(id, opts)

Enabling bonding

Enabling bonding for one or all ports

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
opts = {
  bulk_enable: true # Boolean | enable both ports
}

begin
  # Enabling bonding
  result = api_instance.bond_port(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->bond_port: #{e}"
end
```

#### Using the bond_port_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> bond_port_with_http_info(id, opts)

```ruby
begin
  # Enabling bonding
  data, status_code, headers = api_instance.bond_port_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->bond_port_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **bulk_enable** | **Boolean** | enable both ports | [optional] |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## convert_layer2

> <Port> convert_layer2(id, opts)

Convert to Layer 2

Converts a bond port to Layer 2. IP assignments of the port will be removed.

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
opts = {
  vnid: OpenapiClient::PortAssignInput.new # PortAssignInput | Virtual Network ID
}

begin
  # Convert to Layer 2
  result = api_instance.convert_layer2(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->convert_layer2: #{e}"
end
```

#### Using the convert_layer2_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> convert_layer2_with_http_info(id, opts)

```ruby
begin
  # Convert to Layer 2
  data, status_code, headers = api_instance.convert_layer2_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->convert_layer2_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **vnid** | [**PortAssignInput**](PortAssignInput.md) | Virtual Network ID | [optional] |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## convert_layer3

> <Port> convert_layer3(id, opts)

Convert to Layer 3

Converts a bond port to Layer 3. VLANs must first be unassigned.

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
opts = {
  request_ips: OpenapiClient::PortConvertLayer3Input.new # PortConvertLayer3Input | IPs to request
}

begin
  # Convert to Layer 3
  result = api_instance.convert_layer3(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->convert_layer3: #{e}"
end
```

#### Using the convert_layer3_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> convert_layer3_with_http_info(id, opts)

```ruby
begin
  # Convert to Layer 3
  data, status_code, headers = api_instance.convert_layer3_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->convert_layer3_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **request_ips** | [**PortConvertLayer3Input**](PortConvertLayer3Input.md) | IPs to request | [optional] |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json


## delete_native_vlan

> <Port> delete_native_vlan(id)

Remove native VLAN

Removes the native VLAN from this port

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID

begin
  # Remove native VLAN
  result = api_instance.delete_native_vlan(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->delete_native_vlan: #{e}"
end
```

#### Using the delete_native_vlan_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> delete_native_vlan_with_http_info(id)

```ruby
begin
  # Remove native VLAN
  data, status_code, headers = api_instance.delete_native_vlan_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->delete_native_vlan_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## disbond_port

> <Port> disbond_port(id, opts)

Disabling bonding

Disabling bonding for one or all ports

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
opts = {
  bulk_disable: true # Boolean | disable both ports
}

begin
  # Disabling bonding
  result = api_instance.disbond_port(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->disbond_port: #{e}"
end
```

#### Using the disbond_port_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> disbond_port_with_http_info(id, opts)

```ruby
begin
  # Disabling bonding
  data, status_code, headers = api_instance.disbond_port_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->disbond_port_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **bulk_disable** | **Boolean** | disable both ports | [optional] |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_port_by_id

> <Port> find_port_by_id(id, opts)

Retrieve a port

Returns a port

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve a port
  result = api_instance.find_port_by_id(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->find_port_by_id: #{e}"
end
```

#### Using the find_port_by_id_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> find_port_by_id_with_http_info(id, opts)

```ruby
begin
  # Retrieve a port
  data, status_code, headers = api_instance.find_port_by_id_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->find_port_by_id_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## unassign_port

> <Port> unassign_port(id, vnid)

Unassign a port

Unassign a port for a hardware.

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

api_instance = OpenapiClient::PortsApi.new
id = TODO # String | Port UUID
vnid = OpenapiClient::PortAssignInput.new # PortAssignInput | Virtual Network ID

begin
  # Unassign a port
  result = api_instance.unassign_port(id, vnid)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->unassign_port: #{e}"
end
```

#### Using the unassign_port_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<Port>, Integer, Hash)> unassign_port_with_http_info(id, vnid)

```ruby
begin
  # Unassign a port
  data, status_code, headers = api_instance.unassign_port_with_http_info(id, vnid)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <Port>
rescue OpenapiClient::ApiError => e
  puts "Error when calling PortsApi->unassign_port_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Port UUID |  |
| **vnid** | [**PortAssignInput**](PortAssignInput.md) | Virtual Network ID |  |

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

