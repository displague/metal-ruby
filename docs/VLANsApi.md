# OpenapiClient::VLANsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

| Method | HTTP request | Description |
| ------ | ------------ | ----------- |
| [**assign_native_vlan**](VLANsApi.md#assign_native_vlan) | **POST** /ports/{id}/native-vlan | Assign a native VLAN |
| [**create_internet_gateway**](VLANsApi.md#create_internet_gateway) | **POST** /virtual-networks/{id}/internet-gateways | Create an internet gateway |
| [**create_virtual_network**](VLANsApi.md#create_virtual_network) | **POST** /projects/{id}/virtual-networks | Create an virtual network |
| [**delete_native_vlan**](VLANsApi.md#delete_native_vlan) | **DELETE** /ports/{id}/native-vlan | Remove native VLAN |
| [**delete_virtual_network**](VLANsApi.md#delete_virtual_network) | **DELETE** /virtual-networks/{id} | Delete a virtual network |
| [**find_virtual_networks**](VLANsApi.md#find_virtual_networks) | **GET** /projects/{id}/virtual-networks | Retrieve all virtual networks |
| [**get_virtual_network**](VLANsApi.md#get_virtual_network) | **GET** /virtual-networks/{id} | Get a virtual network |


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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Port UUID
vnid = 'vnid_example' # String | UUID or VNID of the virtual network to assign

begin
  # Assign a native VLAN
  result = api_instance.assign_native_vlan(id, vnid)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->assign_native_vlan: #{e}"
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
  puts "Error when calling VLANsApi->assign_native_vlan_with_http_info: #{e}"
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


## create_internet_gateway

> <InternetGateway> create_internet_gateway(id, length)

Create an internet gateway

Creates an internet gateway.

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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Virtual Network UUID
length = 'length_example' # String | IP Reservation length

begin
  # Create an internet gateway
  result = api_instance.create_internet_gateway(id, length)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->create_internet_gateway: #{e}"
end
```

#### Using the create_internet_gateway_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<InternetGateway>, Integer, Hash)> create_internet_gateway_with_http_info(id, length)

```ruby
begin
  # Create an internet gateway
  data, status_code, headers = api_instance.create_internet_gateway_with_http_info(id, length)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <InternetGateway>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->create_internet_gateway_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Network UUID |  |
| **length** | **String** | IP Reservation length |  |

### Return type

[**InternetGateway**](InternetGateway.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## create_virtual_network

> <VirtualNetwork> create_virtual_network(id, virtual_network)

Create an virtual network

Creates an virtual network.

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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Project UUID
virtual_network = OpenapiClient::VirtualNetworkCreateInput.new # VirtualNetworkCreateInput | Virtual Network to create

begin
  # Create an virtual network
  result = api_instance.create_virtual_network(id, virtual_network)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->create_virtual_network: #{e}"
end
```

#### Using the create_virtual_network_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualNetwork>, Integer, Hash)> create_virtual_network_with_http_info(id, virtual_network)

```ruby
begin
  # Create an virtual network
  data, status_code, headers = api_instance.create_virtual_network_with_http_info(id, virtual_network)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualNetwork>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->create_virtual_network_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **virtual_network** | [**VirtualNetworkCreateInput**](VirtualNetworkCreateInput.md) | Virtual Network to create |  |

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Port UUID

begin
  # Remove native VLAN
  result = api_instance.delete_native_vlan(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->delete_native_vlan: #{e}"
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
  puts "Error when calling VLANsApi->delete_native_vlan_with_http_info: #{e}"
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


## delete_virtual_network

> <VirtualNetwork> delete_virtual_network(id)

Delete a virtual network

Deletes a virtual network.

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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Virtual Network UUID

begin
  # Delete a virtual network
  result = api_instance.delete_virtual_network(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->delete_virtual_network: #{e}"
end
```

#### Using the delete_virtual_network_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualNetwork>, Integer, Hash)> delete_virtual_network_with_http_info(id)

```ruby
begin
  # Delete a virtual network
  data, status_code, headers = api_instance.delete_virtual_network_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualNetwork>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->delete_virtual_network_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Network UUID |  |

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## find_virtual_networks

> <VirtualNetworkList> find_virtual_networks(id, opts)

Retrieve all virtual networks

Provides a list of virtual networks for a single project.

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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Project UUID
opts = {
  include: ['inner_example'], # Array<String> | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects.
  exclude: ['inner_example'] # Array<String> | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects.
}

begin
  # Retrieve all virtual networks
  result = api_instance.find_virtual_networks(id, opts)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->find_virtual_networks: #{e}"
end
```

#### Using the find_virtual_networks_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualNetworkList>, Integer, Hash)> find_virtual_networks_with_http_info(id, opts)

```ruby
begin
  # Retrieve all virtual networks
  data, status_code, headers = api_instance.find_virtual_networks_with_http_info(id, opts)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualNetworkList>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->find_virtual_networks_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Project UUID |  |
| **include** | [**Array&lt;String&gt;**](String.md) | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] |
| **exclude** | [**Array&lt;String&gt;**](String.md) | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] |

### Return type

[**VirtualNetworkList**](VirtualNetworkList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json


## get_virtual_network

> <VirtualNetwork> get_virtual_network(id)

Get a virtual network

Get a virtual network.

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

api_instance = OpenapiClient::VLANsApi.new
id = TODO # String | Virtual Network UUID

begin
  # Get a virtual network
  result = api_instance.get_virtual_network(id)
  p result
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->get_virtual_network: #{e}"
end
```

#### Using the get_virtual_network_with_http_info variant

This returns an Array which contains the response data, status code and headers.

> <Array(<VirtualNetwork>, Integer, Hash)> get_virtual_network_with_http_info(id)

```ruby
begin
  # Get a virtual network
  data, status_code, headers = api_instance.get_virtual_network_with_http_info(id)
  p status_code # => 2xx
  p headers # => { ... }
  p data # => <VirtualNetwork>
rescue OpenapiClient::ApiError => e
  puts "Error when calling VLANsApi->get_virtual_network_with_http_info: #{e}"
end
```

### Parameters

| Name | Type | Description | Notes |
| ---- | ---- | ----------- | ----- |
| **id** | [**String**](.md) | Virtual Network UUID |  |

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

