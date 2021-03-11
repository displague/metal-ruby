# metal.VLANsApi

All URIs are relative to *https://api.equinix.com/metal/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assign_native_vlan**](VLANsApi.md#assign_native_vlan) | **POST** /ports/{id}/native-vlan | Assign a native VLAN
[**create_internet_gateway**](VLANsApi.md#create_internet_gateway) | **POST** /virtual-networks/{id}/internet-gateways | Create an internet gateway
[**create_virtual_network**](VLANsApi.md#create_virtual_network) | **POST** /projects/{id}/virtual-networks | Create an virtual network
[**delete_native_vlan**](VLANsApi.md#delete_native_vlan) | **DELETE** /ports/{id}/native-vlan | Remove native VLAN
[**delete_virtual_network**](VLANsApi.md#delete_virtual_network) | **DELETE** /virtual-networks/{id} | Delete a virtual network
[**find_virtual_networks**](VLANsApi.md#find_virtual_networks) | **GET** /projects/{id}/virtual-networks | Retrieve all virtual networks
[**get_virtual_network**](VLANsApi.md#get_virtual_network) | **GET** /virtual-networks/{id} | Get a virtual network


# **assign_native_vlan**
> Port assign_native_vlan(id, vnid)

Assign a native VLAN

Assigns a virtual network to this port as a \"native VLAN\"

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID
vnid = 'vnid_example' # str | UUID or VNID of the virtual network to assign

    try:
        # Assign a native VLAN
        api_response = api_instance.assign_native_vlan(id, vnid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->assign_native_vlan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 
 **vnid** | **str**| UUID or VNID of the virtual network to assign | 

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_internet_gateway**
> InternetGateway create_internet_gateway(id, length)

Create an internet gateway

Creates an internet gateway.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Virtual Network UUID
length = 'length_example' # str | IP Reservation length

    try:
        # Create an internet gateway
        api_response = api_instance.create_internet_gateway(id, length)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->create_internet_gateway: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Virtual Network UUID | 
 **length** | **str**| IP Reservation length | 

### Return type

[**InternetGateway**](InternetGateway.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_virtual_network**
> VirtualNetwork create_virtual_network(id, virtual_network)

Create an virtual network

Creates an virtual network.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Project UUID
virtual_network = metal.VirtualNetworkCreateInput() # VirtualNetworkCreateInput | Virtual Network to create

    try:
        # Create an virtual network
        api_response = api_instance.create_virtual_network(id, virtual_network)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->create_virtual_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Project UUID | 
 **virtual_network** | [**VirtualNetworkCreateInput**](VirtualNetworkCreateInput.md)| Virtual Network to create | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | created |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_native_vlan**
> Port delete_native_vlan(id)

Remove native VLAN

Removes the native VLAN from this port

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Port UUID

    try:
        # Remove native VLAN
        api_response = api_instance.delete_native_vlan(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->delete_native_vlan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Port UUID | 

### Return type

[**Port**](Port.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_virtual_network**
> VirtualNetwork delete_virtual_network(id)

Delete a virtual network

Deletes a virtual network.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Virtual Network UUID

    try:
        # Delete a virtual network
        api_response = api_instance.delete_virtual_network(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->delete_virtual_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Virtual Network UUID | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_virtual_networks**
> VirtualNetworkList find_virtual_networks(id, include=include, exclude=exclude)

Retrieve all virtual networks

Provides a list of virtual networks for a single project.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Project UUID
include = ['include_example'] # list[str] | Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. (optional)
exclude = ['exclude_example'] # list[str] | Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. (optional)

    try:
        # Retrieve all virtual networks
        api_response = api_instance.find_virtual_networks(id, include=include, exclude=exclude)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->find_virtual_networks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Project UUID | 
 **include** | [**list[str]**](str.md)| Nested attributes to include. Included objects will return their full attributes. Attribute names can be dotted (up to 3 levels) to included deeply nested objects. | [optional] 
 **exclude** | [**list[str]**](str.md)| Nested attributes to exclude. Excluded objects will return only the href attribute. Attribute names can be dotted (up to 3 levels) to exclude deeply nested objects. | [optional] 

### Return type

[**VirtualNetworkList**](VirtualNetworkList.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_virtual_network**
> VirtualNetwork get_virtual_network(id)

Get a virtual network

Get a virtual network.

### Example

* Api Key Authentication (x_auth_token):
```python
from __future__ import print_function
import time
import metal
from metal.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://api.equinix.com/metal/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = metal.Configuration(
    host = "https://api.equinix.com/metal/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: x_auth_token
configuration.api_key['x_auth_token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['x_auth_token'] = 'Bearer'

# Enter a context with an instance of the API client
with metal.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = metal.VLANsApi(api_client)
    id = 'id_example' # str | Virtual Network UUID

    try:
        # Get a virtual network
        api_response = api_instance.get_virtual_network(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling VLANsApi->get_virtual_network: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Virtual Network UUID | 

### Return type

[**VirtualNetwork**](VirtualNetwork.md)

### Authorization

[x_auth_token](../README.md#x_auth_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | ok |  -  |
**401** | unauthorized |  -  |
**403** | forbidden |  -  |
**404** | not found |  -  |
**422** | unprocessable entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

